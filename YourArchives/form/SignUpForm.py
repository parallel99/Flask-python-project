from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from YourArchives.model.UserModel import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email = User.query.filter_by(email=email_address_to_check.data).first()
        if email:
            raise ValidationError('Email Address already exists! Please try a different email address')


    username = StringField(label='Username', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Password Confirm', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')