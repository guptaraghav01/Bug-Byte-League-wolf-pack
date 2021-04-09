from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flaskblog.models import User
from flask_login import login_user, current_user, logout_user, login_required
from hashlib import sha256


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


assert isinstance(app.route, object)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/topics')
def topics():
    return render_template('topics.html')

@app.route("/question")
def question():
    return render_template('question.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        h = sha256()
        password = form.password.data.encode('utf-8')
        h.update(password)
        hash = h.hexdigest()
        user = User(FirstName=form.FirstName.data, MiddleName=form.MiddleName.data, LastName=form.LastName.data,
                    DOB=form.DOB.data, UserEmail=form.UserEmail.data, type=form.type.data,  PhoneNo=form.PhoneNo.data,
                    Education=form.Education.data, password=hash)
        db.session.add(user)
        db.session.commit()
        flash('Account has been created. You can login now!!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(UserEmail=form.UserEmail.data).first()
        h = sha256()
        password = form.password.data.encode('utf-8')
        h.update(password)
        hash = h.hexdigest()
        if user and (user.password == hash):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.FirstName = form.FirstName.data
        current_user.MiddleName = form.MiddleName.data
        current_user.LastName = form.LastName.data
        current_user.DOB = form.DOB.data
        current_user.UserEmail = form.UserEmail.data
        current_user.PhoneNo = form.PhoneNo.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.FirstName.data = current_user.FirstName
        form.MiddleName.data = current_user.MiddleName
        form.LastName.data = current_user.LastName
        form.DOB.data = current_user.DOB
        form.UserEmail.data = current_user.UserEmail
        form.PhoneNo.data = current_user.PhoneNo
    return render_template('account.html', title='Account', form=form)
