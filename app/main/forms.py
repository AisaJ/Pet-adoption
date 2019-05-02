from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class MessageForm(FlaskForm):

    title = StringField('title',validators=[Required()])
    message = TextAreaField('message')
    submit = SubmitField('Submit')