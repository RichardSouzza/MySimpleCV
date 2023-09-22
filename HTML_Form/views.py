from flask import Blueprint, request, redirect, url_for, render_template


html_form_bp = Blueprint("html_form", __name__,
                         static_folder="static",
                         static_url_path="",
                         template_folder="templates",
                         url_prefix="/HTML-Form")


@html_form_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        username = "Anonymous" if username == "" else username
        return redirect(url_for("html_form.userpage", username=username))

    return render_template("html_form/form.html", title="Register User")


@html_form_bp.route("/<username>")
def userpage(username):
    return render_template("html_form/userpage.html", title=username, username=username)
