import os
import sys
currentUrl = os.path.dirname(__file__)
parentUrl = os.path.abspath(os.path.join(currentUrl, os.pardir))
sys.path.append(parentUrl)
sys.path.append(currentUrl)
from flask import Flask
from flask_mail import Mail
from config import config
from flask_cors import CORS

mail = Mail()


def create_app(config_name):
    app = Flask(__name__, static_folder="../../dist/static", template_folder="../../dist")
    CORS(app, supports_credentials=True)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .search import search as search_blueprint
    app.register_blueprint(search_blueprint, url_prefix='/search')

    from .login import login as login_blueprint
    app.register_blueprint(login_blueprint, url_prefix='/login')

    from .weather import weather as weather_blueprint
    app.register_blueprint(weather_blueprint, url_prefix='/weather')

    return app