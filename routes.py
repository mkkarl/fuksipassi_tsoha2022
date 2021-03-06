from app import app
from flask import render_template, request, redirect
import users

@app.route("/")
def index():
    user_id = users.user_id()
    if user_id == 0:
        return redirect("/login")
    return render_template("index.html", is_admin=users.is_admin(user_id), is_tutor=users.is_tutor(user_id), is_fresher=users.is_fresher(user_id))

@app.route("/login", methods=["GET", "POST"])
def login():
    if users.user_id() != 0:
        return redirect("/")
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if users.user_id() != 0:
        return redirect("/")
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")

@app.route("/users")
def allusers():
    user_id = users.user_id()
    if user_id == 0:
        return redirect("/login")
    return render_template("users.html", is_admin=users.is_admin(user_id), is_tutor=users.is_tutor(user_id), is_fresher=users.is_fresher(user_id), userlist=users.userlist())

@app.route("/user/<int:id>")
def user(id):
    user_id = users.user_id()
    if user_id == id or users.is_admin(user_id) or users.is_tutor(user_id):
        userinfo = users.userinfo(id)
        return render_template("user.html", is_admin=users.is_admin(user_id), is_tutor=users.is_tutor(user_id), is_fresher=users.is_fresher(user_id), userinfo=userinfo)
    return redirect("/")

@app.route("/user")
def ownprofile():
    user_id = users.user_id()
    if user_id == 0:
        return redirect("/login")
    return redirect("/user/" + str(user_id))