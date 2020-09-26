from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    title = StringField('Blog Title', validators=[Required()])
    blog = TextAreaField('Write Blog...')
    submit = SubmitField('submit')
    
class CommentForm(FlaskForm):
    title = StringField('Comment Title', validators=[Required()])
    comment = TextAreaField('Comments...')
    submit = SubmitField('submit')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Short bio about you...',validators = [Required()])
    submit = SubmitField('Submit')