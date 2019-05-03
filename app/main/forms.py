from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class MessageForm(FlaskForm):

    message = TextAreaField('Message the Seller',validators=[Required()])
    submit = SubmitField('Submit')

class PetForm(FlaskForm):
    name = StringField('Pets Name')  
    gender = SelectField('Pets Gender', choices=[('Male', 'Male'),('Female', 'Female')])
    age = StringField('Pets Age (In months)')
    description = TextAreaField('Pet Description')
    contact = StringField('enter phone number')
    submit = SubmitField('Submit')
    
    
