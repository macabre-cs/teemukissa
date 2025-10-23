import sqlite3, secrets, math
from flask import Flask
from flask import redirect, render_template, request, session, abort, make_response, flash, get_flashed_messages
import config, users, tea
import markupsafe

app = Flask(__name__)
app.secret_key = config.secret_key

with app.app_context():
    tea.populate_tea_varieties()

def require_login():
    if "user_id" not in session:
        flash("Sinun täytyy olla kirjautunut sisään!!!!!!!")
        abort(403)

def check_csrf():
    if request.form["csrf_token"] != session["csrf_token"]:
        flash("CSRF-tarkistus epäonnistui >:/")
        abort(403)

def get_paginated_reviews(reviews, page, page_size):
    total_reviews = len(reviews)
    page_count = math.ceil(total_reviews / page_size)

    if page < 1:
        return [], page_count, 1
    if page > page_count:
        return [], page_count, page_count

    start = (page - 1) * page_size
    end = start + page_size
    paginated_reviews = reviews[start:end]

    return paginated_reviews, page_count, page

@app.template_filter()
def show_lines(content):
    content = str(markupsafe.escape(content))
    content = content.replace("\n", "<br />")
    return markupsafe.Markup(content)

@app.route("/")
def index():
    return render_template("index.html", messages=get_flashed_messages())

@app.route("/teatimes")
def show_teatimes():
    varieties = tea.get_tea_varieties()
    return render_template("teatimes.html", varieties=varieties)

@app.route("/tea/<tea_variety>")
@app.route("/tea/<tea_variety>/<int:page>")
def tea_reviews(tea_variety, page=1):
    page_size = 10
    all_reviews = tea.get_reviews(tea_variety)

    reviews, page_count, current_page = get_paginated_reviews(all_reviews, page, page_size)

    comments_count = {review['id']: len(tea.get_comments(review['id'])) for review in reviews}

    return render_template("tea_reviews.html", reviews=reviews, tea_variety=tea_variety, 
                           comments_count=comments_count, page=current_page, page_count=page_count)

@app.route("/review/<int:review_id>")
def view_review(review_id):
    review = tea.get_review(review_id)
    if not review:
        flash("Teehetkeä ei löytynyt.")
        abort(404)

    comments = tea.get_comments(review_id)
    return render_template("review.html", review=review, comments=comments)

@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "GET":
        varieties = tea.get_tea_varieties()
        return render_template("add_review.html", varieties=varieties)
    
    if request.method == "POST":
        check_csrf()
        require_login()
        
        user_id = session["user_id"]
        content = request.form["content"]
        variety = request.form["variety"]
        title = request.form["title"]
        rating = request.form.get("rating")

        if not tea.variety_exists(variety):
            flash("Teelaatua ei löytynyt ?__?")
            abort(403)

        if not users.user_exists(user_id):
            flash("Käyttäjätunnusta ei löytynyt >:(")
            abort(403)

        if not content or len(content) > 5000:
            flash("Teehetken sisältö on liian pitkä tai puuttuu :(")
            abort(403)
        
        if not title or len(title) > 80:
            flash("Teehetken otsikko on liian pitkä tai puuttuu :<")
            abort(403)

        try:
            tea.add_review(variety, title, content, user_id, int(rating))
        except sqlite3.IntegrityError:
            flash("Teehetken lisääminen epäonnistui ;__;")
            abort(403)

        flash("Teehetken lisääminen onnistui! :3")
        return redirect(f"/tea/{variety}")

@app.route("/edit/<int:review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    require_login()

    review = tea.get_review(review_id)
    if not review:
        flash("Teehetkeä ei löytynyt???")
        abort(404)
    
    if review["user_id"] != session["user_id"]:
        flash("Et voi muokata toisten teehetkiä >:(")
        abort(403)

    if request.method == "GET":
        return render_template("edit.html", review=review)

    if request.method == "POST":
        check_csrf()
        content = request.form["content"]
        title = request.form["title"]
        rating = request.form.get("rating")
        if not content or len(content) > 5000:
            flash("Teehetken sisältö on liian pitkä tai puuttuu :(")
            abort(403)
        if not title or len(title) > 80:
            flash("Teehetken otsikko on liian pitkä tai puuttuu :<")
            abort(403)

        tea.update_review(review_id, title, content, rating)
        flash("Teehetken muokkaaminen onnistui! :3")
        return redirect(f"/review/{review["id"]}")

@app.route("/remove/<int:review_id>", methods=["GET", "POST"])
def remove_review(review_id):
    require_login()

    review = tea.get_review(review_id)
    if not review:
        flash("Nani?! Teehetkeä ei löytynyt!!")
        abort(404)

    if review["user_id"] != session["user_id"]:
        flash("Et voi poistaa toisten teehetkiä >:( Tuhma kisu!!")
        abort(403)

    if request.method == "GET":
        return render_template("remove.html", review=review)

    if request.method == "POST":
        check_csrf()
        if "continue" in request.form:
            tea.delete_review(review_id)
            flash("Teehetken poistaminen onnistui! :>")
        return redirect(f"/teatimes")
    
@app.route("/add_comment", methods=["POST"])
def add_comment():
    check_csrf()
    require_login()

    review_id = request.form["review_id"]
    content = request.form["content"]
    user_id = session["user_id"]
    source = request.form["source"]

    review = tea.get_review(review_id)
    if review is None:
        flash("Teehetkeä ei löytynyt :<")
        abort(404)

    if not users.user_exists(user_id):
            flash("Käyttäjätunnusta ei löytynyt >:(")
            abort(403)

    if not content or len(content) > 1000:
        flash("Kommentti on liian pitkä tai puuttuu :<")
        abort(403)

    tea.add_comment(review_id, user_id, content)
    flash("Kommentin lisääminen onnistui! :3")

    if source == "tea":
        return redirect(f"/tea/{review['variety']}")
    elif source == "review":
        return redirect(f"/review/{review['id']}")
    else:
        abort(400)

@app.route("/edit_comment", methods=["POST"])
def edit_comment():
    check_csrf()
    require_login()

    comment_id = request.form.get("comment_id")
    review_id = request.form.get("review_id")
    content = request.form.get("content")

    comment = tea.get_comment(comment_id)
    if comment is None:
        flash("Kommenttia ei löytynyt :<")
        abort(404)

    if not content or len(content) > 5000:
        flash("Kommentti on liian pitkä tai puuttuu :(")
        abort(403)

    if comment["user_id"] != session["user_id"]:
        flash("Et voi muokata toisten kommentteja >:(")
        abort(403)

    tea.edit_comment(comment_id, content)
    flash("Kommentin muokkaaminen onnistui! :3")
    return redirect(f"/review/{review_id}")

@app.route("/delete_comment", methods=["POST"])
def delete_comment():
    check_csrf()
    require_login()

    comment_id = request.form.get("comment_id")
    review_id = request.form.get("review_id")

    comment = tea.get_comment(comment_id)
    if comment is None:
        flash("Kommenttia ei löytynyt :<")
        abort(404)

    if comment["user_id"] != session["user_id"]:
        flash("Et voi poistaa toisten kommentteja >:(")
        abort(403)
    
    tea.delete_comment(comment_id)
    flash("Kommentin poistaminen onnistui! :O")
    return redirect(f"/review/{review_id}")
    
@app.route("/search")
@app.route("/search/<int:page>")
def search(page=1):
    query = request.args.get("query")

    page_size = 10

    if not query:
        return render_template("search.html", query=query, results=[], page=1, page_count=1)

    results = tea.search_reviews(query)

    paginated_results, page_count, current_page = get_paginated_reviews(results, page, page_size)

    if page < 1:
        return redirect(f"/search/1?query={query}")
    if page > page_count:
        return redirect(f"/search/{page_count}?query={query}")

    return render_template("search.html", query=query, results=paginated_results, page=current_page, page_count=page_count)

@app.route("/user/<int:user_id>")
@app.route("/user/<int:user_id>/<int:page>")
def show_user(user_id, page=1):
    profile_user = users.get_user(user_id)
    if not profile_user:
        flash("Käyttäjätunnusta ei löytynyt :<")
        abort(404)
    
    all_reviews = users.get_reviews(user_id)
    reviews, page_count, current_page = get_paginated_reviews(all_reviews, page, 10)

    stats = users.get_stats(user_id)
    logged_in_user = session.get("user_id")
    comments_count = {review['id']: len(tea.get_comments(review['id'])) for review in reviews}

    return render_template("user.html", profile_user=profile_user, reviews=reviews, 
                           logged_in_user=logged_in_user, stats=stats, 
                           comments_count=comments_count, page=current_page, page_count=page_count)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html", filled={})

    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]

        if not username or len(username) > 30:
            flash("Käyttäjätunnus on liian pitkä tai puuttuu!")
            abort(403)
        if not password1 or len(password1) > 30:
            flash("Turvakisu on liian pitkä tai puuttuu!")
            abort(403)
        if not password2 or len(password2) > 30:
            flash("Turvakisu on liian pitkä tai puuttuu!")
            abort(403)

        if password1 != password2:
            flash("Turvakisut eivät ole samat!!!")
            filled = {"username": username}
            return render_template("register.html", filled=filled)
        
        try:
            users.create_user(username, password1)
            flash("Käyttäjätunnuksen luominen onnistui, voit nyt kirjautua sisään :3")
            return redirect("/")
            
        except sqlite3.IntegrityError:
            flash("Käyttäjätunnus on jo varattu :(")
            filled = {"username": username}
            return render_template("register.html", filled=filled)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user_id = users.check_login(username, password)
        if user_id:
            session["user_id"] = user_id
            session["username"] = username
            session["csrf_token"] = secrets.token_hex(16)
            return redirect("/")
        else:
            flash("Väärä käyttäjätunnus tai turvakisu! :<")
            return redirect("/login")
        
@app.route("/add_image", methods=["GET", "POST"])
def add_image():
    require_login()

    if request.method == "GET":
        return render_template("add_image.html")

    if request.method == "POST":
        check_csrf()
        file = request.files["image"]
        if not file.filename.endswith(".jpg"):
            flash("Lähettämäsi tiedosto ei ole jpg-tiedosto! :O")
            return redirect("/add_image")

        image = file.read()
        if len(image) > 100 * 1024:
            flash("Lähettämäsi tiedosto on liian suuri ;)))")
            return redirect("/add_image")

        user_id = session["user_id"]
        users.update_image(user_id, image)
        flash("Kuvan lisääminen onnistui!! :3")
        return redirect("/user/" + str(user_id))
    
@app.route("/image/<int:user_id>")
def show_image(user_id):
    image = users.get_image(user_id)
    if not image:
        flash("Kuvaa ei löytynyt :(")
        abort(404)

    response = make_response(bytes(image))
    response.headers.set("Content-Type", "image/jpeg")
    return response

@app.route("/logout")
def logout():
    session.clear()
    flash("Olet nyt kirjautunut ulos. Nähdään taas pian! :3")
    return redirect("/")