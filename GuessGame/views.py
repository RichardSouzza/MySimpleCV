from flask import Blueprint, render_template


guessgame_bp = Blueprint("guessgame", __name__,
                         static_folder="static",
                         static_url_path="",
                         template_folder="templates",
                         url_prefix="/GuessGame")


@guessgame_bp.route("/")
def index():
    return render_template("guessgame/guessgame.html")
