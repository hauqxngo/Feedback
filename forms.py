from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Optional, Email, Length

class UserForm(FlaskForm):
    """Form for creating users."""

    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    email = StringField('Email Address', validators=[InputRequired(), Email()])
    first_name = StringField('First Name', validators=[Optional()])
    last_name = StringField('Last Name', validators=[Optional()])

class LoginForm(FlaskForm):
    """Form to login a user."""
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class FeedbackForm(FlaskForm):
    """Form to add new feedback."""

    title = StringField('Title', validators=[InputRequired(), Length(max=100)])
    content = StringField('Content', validators=[InputRequired()])


class DeleteForm(FlaskForm):
    """This form is intentionally blank."""