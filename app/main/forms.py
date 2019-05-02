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

class PetForm(FlaskForm):
    name = StringField('Pets Name')  
    Gender = SelectField('Pets Gender', choices=[('Male', 'Male'),('Female', 'Female')])
    Age = StringField('Pets Age (In months)')
    description = TextAreaField('Pet Description')
    Contact = StringField('enter phone number')
    submit = SubmitField('Submit')
    
    
