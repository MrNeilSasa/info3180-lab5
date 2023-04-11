from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed, FileRequired

class MovieForm(FlaskForm):
    title = StringField('Title: ', validators=[InputRequired()])
    description = TextAreaField('Description: ', validators=[InputRequired()])
    poster = FileField('Upload Image of Poster: ', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Only JPEG and PNG images are allowed!')] )