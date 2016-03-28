from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length
from ..models import Post

class PostForm(Form):
    body = StringField('What\'s on your mind?', validators=[Required(), Length(1,140)])
    submit = SubmitField('Submit')
