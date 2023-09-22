from flask import Blueprint, render_template
from .examples import examples


practical_activity_css_bp = Blueprint("practical_activity_css", __name__,
                                      static_folder="static",
                                      static_url_path="",
                                      template_folder="templates",
                                      url_prefix="/PracticalActivity-CSS")


@practical_activity_css_bp.route("/")
def index():
    return render_template(
        "practical_activity_css/index.html", title="Atividade Prática - CSS", examples=examples
    )


@practical_activity_css_bp.route("/<example>")
def example(example):
    return render_template(f"practical_activity_css/{example}.html", title=f"{example}")

