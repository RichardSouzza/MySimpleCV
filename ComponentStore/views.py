from flask import Blueprint, render_template


component_store_bp = Blueprint("component_store", __name__,
                          static_folder="static",
                          static_url_path="",
                          template_folder="templates",
                          url_prefix="/ComponentStore")


@component_store_bp.route("/")
def index():
    return render_template("component_store/component_store.html")
