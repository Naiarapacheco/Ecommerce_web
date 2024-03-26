from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sistema.db"
app.config["SECRET_KEY"] = 'b650c5c554b59cc076af052c'
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "page_login"   #login_view informa qual é a página de login
login_manager.login_message = "Por favor, realize o login para acessar essa página"
login_manager.login_message_category = "info"


from empresa import routes