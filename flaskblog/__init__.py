from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a8rXgMkS8-eBcg-dEF-2vw'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'infoSE'
app.config['RECAPTCHA_USE_SSL']= False
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Leke50aAAAAAM95Kx1vh0sOkI_v-S2NtkJbXcwS'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6Leke50aAAAAANUyOP63iD8iVGCSBLC3Z8R0c1V_'
app.config['RECAPTCHA_OPTIONS']= {'theme':'black'}

from flaskblog import routes