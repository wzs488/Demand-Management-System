
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp
from wtforms.widgets import Input
from .models import Users
from flask_login import current_user


class CancelInput(Input):
    """
    Renders a cancel button.

    The field's label is used as the text of the cancel button instead of the
    data on the field.
    """
    input_type = 'button'

    def __call__(self, field, **kwargs):
        kwargs.setdefault('value', field.label.text)
        return super(CancelInput, self).__call__(field, **kwargs)


class CancelField(BooleanField):
    """
    Represents an ``<input type="button">``.  This allows checking if a given
    cancel button has been pressed.
    """
    widget = CancelInput()


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(message='username required'), Length(1, 64)])
    password = PasswordField('password', validators=[DataRequired(message='password required')])
    remember_me = BooleanField('remember me')
    submit = SubmitField('login')

    def validate_username(self, field):
        if not Users.query.filter_by(username=field.data).first():
            raise ValidationError('username incorrect')


class AddUserForm(FlaskForm):
    username = StringField('username', validators=[
        DataRequired(message='username reqired'), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'only use a-z,A-z,0-9')])
    password = PasswordField('password', validators=[DataRequired(message='password required'), EqualTo('password2', message='password are not same')])
    password2 = PasswordField('confirm password', validators=[DataRequired()])
    is_administrator = BooleanField('is admin')
    submit = SubmitField('add')
    cancel = CancelField('cancel')

    def validate_username(self, field):
        if Users.query.filter_by(username=field.data).first():
            raise ValidationError('username has been used')


class ToDoForm(FlaskForm):
    todo_content = TextAreaField('requirements context')
    cancel = SubmitField('cancel')
    submit = SubmitField('confirm')


class ResetInfoForm(FlaskForm):
    username = StringField('username', validators=[
        DataRequired(message='username required'), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'only use a-z,A-z,0-9')])
    old_password = PasswordField('old password', validators=[DataRequired(message='password required')])
    password = PasswordField('new password', validators=[DataRequired(message='password required'), EqualTo('password2', message='password are not same')])
    password2 = PasswordField('confirm password', validators=[DataRequired()])
    submit = SubmitField('update info')
    cancel = CancelField('cancel')

    def validate_old_password(self, field):
        if not current_user.verify_password(field.data):
            raise ValidationError('password incorrect')

    def validate_username(self, field):
        if Users.query.filter_by(username=field.data).first():
            raise ValidationError('username has been used')
