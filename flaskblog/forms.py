from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_login import current_user


class RegistrationForm(FlaskForm):
    FirstName = StringField('First Name',
                            validators=[DataRequired(), Length(min=2, max=20)])
    MiddleName = StringField('Middle Name')
    LastName = StringField('Last Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    DOB = StringField('Date of Birth',
                      validators=[DataRequired()])
    UserEmail = StringField('E-Mail',
                            validators=[DataRequired(), Email()])
    PhoneNo = StringField('Phone Number',
                          validators=[DataRequired(), Length(min=2, max=20)])
    Education = StringField('Name of School/College/Company',
                            validators=[DataRequired(), Length(min=2, max=60)])
    type = StringField('You are here as: (Learner/Professional)',
                       validators=[DataRequired(), Length(min=2, max=60)])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=6, max=20)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    recaptcha = RecaptchaField()

    def validate_email(self, email):
        user = User.query.filter_by(UserEmail=UserEmail.data).first()
        if user:
            raise ValidationError(
                'That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    UserEmail = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    FirstName = StringField('First Name',
                            validators=[Length(min=2, max=20)])
    MiddleName = StringField('Middle Name')
    LastName = StringField('Last Name',
                           validators=[Length(min=2, max=20)])
    DOB = StringField('Date of Birth')
    UserEmail = StringField('E-Mail')
    PhoneNo = StringField('Phone Number',
                          validators=[Length(min=2, max=20)])
    Education = StringField('Name of School/College/Company',
                            validators=[Length(min=2, max=60)])
    submit = SubmitField('Save Changes')

    def validate_email(self, email):
        if UserEmail.data != current_user.UserEmail:
            user = User.query.filter_by(UserEmail=UserEmail.data).first()
            if user:
                raise ValidationError(
                    'That email is taken. Please choose a different one.')
