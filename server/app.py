from flask import Flask

import sys
sys.path.append("..")

from HTML_Form.views import html_form_bp
from Home.views import home_bp
from MySimpleCV.views import mysimplecv_bp
from PracticalActivity_CSS.views import practical_activity_css_bp
from SportShop.views import sportshop_bp


app = Flask(__name__)
app.register_blueprint(html_form_bp)
app.register_blueprint(home_bp)
app.register_blueprint(mysimplecv_bp)
app.register_blueprint(practical_activity_css_bp)
app.register_blueprint(sportshop_bp)
