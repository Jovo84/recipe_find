from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from setup_app.app_config import APPConfig


app = Flask(__name__)
app.config.from_object(APPConfig)
app.static_folder = "../static/"
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


db = SQLAlchemy(app)
