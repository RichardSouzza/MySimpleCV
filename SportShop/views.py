from flask import Blueprint, render_template


sportshop_bp = Blueprint("sportshop", __name__,
                          static_folder="static",
                          static_url_path="",
                          template_folder="templates",
                          url_prefix="/SportShop")


class Product:
    def __init__(self, name, image, bg_color):
        self.name = name
        self.image = image
        self.bg_color = bg_color


@sportshop_bp.route("/")
def index():
    products = [
        Product("Camisa do Brasil", "camisa-brasil.webp", "bg-yellow-100"),
        Product("Camisa do Flamengo", "camisa-flamengo.webp", "bg-red-100"),
        Product("Camisa do Confiança", "camisa-confiança.webp", "bg-sky-100"),
    ] * 2
    return render_template("sportshop/sportshop.html", title="SportShop", products=products)
