import sqlite3
from flask import Flask
from flask import redirect, render_template, request, session, abort, make_response
import config, forum, users, tea

app = Flask(__name__)
app.secret_key = config.secret_key

with app.app_context():
    tea.populate_tea_varieties()

def require_login():
    if "user_id" not in session:
        abort(403)

@app.route("/")
def index():
    threads = forum.get_threads()
    return render_template("index.html", threads=threads)

@app.route("/teatimes")
def show_teatimes():
    varieties = tea.get_tea_varieties()
    return render_template("teatimes.html", varieties=varieties)

@app.route("/tea/<tea_variety>")
def tea_reviews(tea_variety):
    reviews = tea.get_reviews(tea_variety)
    return render_template("tea_reviews.html", reviews=reviews, tea_variety=tea_variety)

@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "GET":
        varieties = tea.get_tea_varieties()  # Get the tea varieties from the database
        return render_template("add_review.html", varieties=varieties)
    
    if request.method == "POST":
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
        except sqlite3.IntegrityError as e:
            abort(403)

        return redirect(f"/tea/{variety}")

@app.route("/thread/<int:thread_id>")
def show_thread(thread_id):
    thread = forum.get_thread(thread_id)
    if not thread:
        abort(404)
    messages = forum.get_messages(thread_id)
    return render_template("thread.html", thread=thread, messages=messages)

@app.route("/new_thread", methods=["POST"])
def new_thread():
    require_login()

    user_id = session["user_id"]
    title = request.form["title"]
    content = request.form["content"]
    if not title or len(title) > 100 or not content or len(content) > 5000:
        abort(403)

    thread_id = forum.add_thread(title, content, user_id)
    return redirect("/thread/" + str(thread_id))

@app.route("/new_message", methods=["POST"])
def new_message():
    require_login()

    user_id = session["user_id"]
    content = request.form["content"]
    thread_id = request.form["thread_id"]

    if not content or len(content) > 5000:
        abort(403)

    try:
        forum.add_message(content, user_id, thread_id)
    except sqlite3.IntegrityError:
        abort(403)

    return redirect("/thread/" + str(thread_id))

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
        content = request.form["content"]
        if not content or len(content) > 5000:
            abort(403)

        tea.update_review(review_id, content)
        return redirect(f"/tea/{review['variety']}")

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
        if "continue" in request.form:
            tea.delete_review(review_id)
        return redirect(f"/tea/{review['variety']}")
    
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
    return render_template("user.html", profile_user=profile_user, reviews=reviews, logged_in_user=logged_in_user)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

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
            return "VIRHE: turvakisut eivät ole samat"

        try:
            users.create_user(username, password1)
            return "Tunnus luotu"
        except sqlite3.IntegrityError:
            return "VIRHE: tunnus on jo varattu"

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
            return redirect("/")
        else:
            return "VIRHE: väärä tunnus tai turvakisu"
        
@app.route("/add_image", methods=["GET", "POST"])
def add_image():
    require_login()

    if request.method == "GET":
        return render_template("add_image.html")

    if request.method == "POST":
        file = request.files["image"]
        if not file.filename.endswith(".jpg"):
            return "VIRHE: väärä tiedostomuoto"

        image = file.read()
        if len(image) > 100 * 1024:
            return "VIRHE: liian suuri kuva"

        user_id = session["user_id"]
        users.update_image(user_id, image)
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
    del session["user_id"]
    return redirect("/")