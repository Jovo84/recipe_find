from flask import Blueprint, render_template


web = Blueprint('web', __name__, template_folder='templates')


@web.route("/")
def home_page():
    return render_template("index.html")

@web.route("/privacy")
def privacy_page():
    return render_template("privacy.html")

@web.route("/terms")
def terms_page():
    return render_template("terms.html")

@web.route("/signin")
def signin_page():
    return render_template("signin.html")

@web.route("/signup")
def signup_page():
    return render_template("signup.html")

@web.route("/browse")
def browse_page():
    return render_template("browse.html")



