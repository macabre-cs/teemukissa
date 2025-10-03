import sqlite3, secrets
from flask import Flask
from flask import redirect, render_template, request, session, abort, make_response, flash
import config, users, tea
import markupsafe

app = Flask(__name__)
app.secret_key = config.secret_key

with app.app_context():
    tea.populate_tea_varieties()

def require_login():
    if "user_id" not in session:
        abort(403)

def check_csrf():
    if request.form["csrf_token"] != session["csrf_token"]:
        abort(403)

@app.template_filter()
def show_lines(content):
    content = str(markupsafe.escape(content))
    content = content.replace("\n", "<br />")
    return markupsafe.Markup(content)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/teatimes")
def show_teatimes():
    varieties = tea.get_tea_varieties()
    return render_template("teatimes.html", varieties=varieties)

@app.route("/tea/<tea_variety>")
def tea_reviews(tea_variety):
    reviews = tea.get_reviews(tea_variety)
    comments = {review['id']: tea.get_comments(review['id']) for review in reviews}
    return render_template("tea_reviews.html", reviews=reviews, tea_variety=tea_variety, comments=comments)

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

        if not tea.variety_exists(variety):
            abort(403)

        if not users.user_exists(user_id):
            abort(403)

        if not content or len(content) > 5000:
            abort(403)

        try:
            tea.add_review(variety, content, user_id)
        except sqlite3.IntegrityError:
            abort(403)

        return redirect(f"/tea/{variety}")

@app.route("/edit/<int:review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    require_login()

    review = tea.get_review(review_id)
    if not review:
        abort(404)
    
    if review["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("edit.html", review=review)

    if request.method == "POST":
        check_csrf()
        content = request.form["content"]
        if not content or len(content) > 5000:
            abort(403)

        tea.update_review(review_id, content)
        return redirect(f"/tea/{review["variety"]}")

@app.route("/remove/<int:review_id>", methods=["GET", "POST"])
def remove_review(review_id):
    require_login()

    review = tea.get_review(review_id)
    if not review:
        abort(404)

    if review["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("remove.html", review=review)

    if request.method == "POST":
        check_csrf()
        if "continue" in request.form:
            tea.delete_review(review_id)
        return redirect(f"/tea/{review["variety"]}")
    
@app.route("/add_comment", methods=["POST"])
def add_comment():
    check_csrf()
    require_login()

    review_id = request.form["review_id"]
    content = request.form["content"]
    user_id = session["user_id"]
    source = request.form["source"]

    if not content or len(content) > 5000:
        abort(403)

    tea.add_comment(review_id, user_id, content)
    review = tea.get_review(review_id)

    if source == "tea":
        return redirect(f"/tea/{review['variety']}")
    elif source == "user":
        return redirect(f"/user/{review['user_id']}")
    else:
        abort(400)
    
    
@app.route("/search")
def search():
    query = request.args.get("query")
    results = tea.search_reviews(query) if query else []
    return render_template("search.html", query=query, results=results)

@app.route("/user/<int:user_id>")
def show_user(user_id):
    profile_user = users.get_user(user_id)
    if not profile_user:
        abort(404)
    
    reviews = users.get_reviews(user_id)
    logged_in_user = session["user_id"]
    comments = {review['id']: tea.get_comments(review['id']) for review in reviews}
    return render_template("user.html", profile_user=profile_user, reviews=reviews, comments=comments, logged_in_user=logged_in_user)

@app.route("/register", methods=["GET", "POST"])
def register():
    success_message = None
    show_form = True

    if request.method == "GET":
        return render_template("register.html", success_message=success_message, show_form=show_form)

    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]

        if not username or len(username) > 30:
            abort(403)
        if not password1 or len(password1) > 30:
            abort(403)
        if not password2 or len(password2) > 30:
            abort(403)

        if password1 != password2:
            #return "VIRHE: turvakisut eivät ole samat"
            flash("VIRHE: turvakisut eivät ole samat")
            return redirect("/register")

        try:
            users.create_user(username, password1)
            success_message = "Tunnus luotu onnistuneesti! Tervetuloa mukaan mauuhtavaan seuraan :3"
            show_form = False
            
            user_id = users.check_login(username, password1)
            session["user_id"] = user_id
            session["username"] = username
            
        except sqlite3.IntegrityError:
            flash("VIRHE: tunnus on jo varattu")
            return redirect("/register")
            #return "VIRHE: tunnus on jo varattu"

        return render_template("register.html", success_message=success_message, show_form=show_form)

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
            flash("VIRHE: väärä tunnus tai turvakisu")
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
            flash("VIRHE: Lähettämäsi tiedosto ei ole jpg-tiedosto")
            return redirect("/add_image")

        image = file.read()
        if len(image) > 100 * 1024:
            flash("VIRHE: Lähettämäsi tiedosto on liian suuri")
            return redirect("/add_image")

        user_id = session["user_id"]
        users.update_image(user_id, image)
        flash("Kuvan lisääminen onnistui")
        return redirect("/user/" + str(user_id))
    
@app.route("/image/<int:user_id>")
def show_image(user_id):
    image = users.get_image(user_id)
    if not image:
        abort(404)

    response = make_response(bytes(image))
    response.headers.set("Content-Type", "image/jpeg")
    return response

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")