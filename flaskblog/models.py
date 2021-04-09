from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    CreatedOn = db.Column(db.DateTime, nullable=True, default = datetime.utcnow)
    ModifiedOn = db.Column(db.DateTime, default = datetime.utcnow)
    FirstName = db.Column(db.String(40), nullable=False)
    MiddleName = db.Column(db.String(40), nullable=True)
    LastName = db.Column(db.String(40), nullable=False)
    DOB = db.Column(db.String(20), nullable=False)
    UserEmail = db.Column(db.String(120), unique=True, nullable=False)
    type = db.Column(db.String(120), nullable=False)
    Education = db.Column(db.String(120), nullable=False)
    PhoneNo = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.id}', '{self.CreatedOn}', '{self.ModifiedOn}', '{self.FirstName}', '{self.MiddleName}', '{self.LastName}', '{self.Education}', '{self.DOB}', '{self.UserEmail}', '{self.PhoneNo}', '{self.password}')"
