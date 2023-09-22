from flask import Blueprint, render_template


home_bp = Blueprint("home", __name__,
                    static_folder="static",
                    static_url_path="",
                    template_folder="templates")


class Project:
    def __init__(self, name, image, route):
        self.name = name
        self.image = image
        self.route = route


@home_bp.route("/")
def index():
    projects = [
        Project("HTML Form", "HTML-Form.png", "/HTML-Form"), 
        Project("MySimpleCV", "MySimpleCV.png", "/MySimpleCV"),
        Project("Practical Activity - CSS", "MySimpleCV.png", "/PracticalActivity-CSS"),
        Project("SportShop", "SportShop.png", "/SportShop"),
    ]
    return render_template("home/index.html", title="Unit Challenges", projects=projects)
