from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    title = StringField('Input neighbourhood:', validators = [Required()])
    post = TextAreaField('Post Your Search:', validators = None)
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself',validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    name = StringField("Your Name")
    comment_itself = StringField("Comment",validators=[Required()])
    submit = SubmitField('Submit')

class SubscribeForm(FlaskForm):
    email = StringField("Enter Your Email Address :")
    submit= SubmitField('Subscribe')
