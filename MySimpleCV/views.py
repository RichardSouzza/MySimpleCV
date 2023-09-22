from flask import Blueprint, render_template


mysimplecv_bp = Blueprint("mysimplecv", __name__,
                          static_folder="static",
                          static_url_path="",
                          template_folder="templates",
                          url_prefix="/MySimpleCV")


@mysimplecv_bp.route("/")
def index():
    return render_template("mysimplecv/my-cv.html")
