from ast import Pass
import email
from wtforms import Form, StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, URL
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(Form):
    title = StringField("Blog Post Title", validators=[InputRequired()])
    subtitle = StringField("Subtitle", validators=[InputRequired()])
    img_url = StringField("Blog Image URL", validators=[InputRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[InputRequired()])
    submit = SubmitField("Submit Post",)

class RegisterForm(Form):
    email = StringField("Email", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    name = StringField("Name", validators=[InputRequired()])
    submit = SubmitField("Sign Me Up")

class LoginForm(Form):
    email = StringField("Email", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Log In")

class CommentForm(Form):
    comment_text = CKEditorField("Comment", validators=[InputRequired()])
    submit = SubmitField("Post Comment")
