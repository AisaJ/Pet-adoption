from . import main
from flask import render_template,flash,abort,redirect,url_for,request
from flask_login import login_required, current_user
from ..models import User,Pet,Message
from .forms import UpdateProfile,PetForm,MessageForm
from .. import db,photos
import markdown2

@main.route('/')
def index():
  title='Adopt a Pet'
  pets= Pet.query.all()

  return render_template('index.html',title=title,pet=pets)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)    


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/pet/new',methods=['GET','POST'])
@login_required
def new_pet():
    pet=Pet.query.filter_by(user_id=current_user.id)
    pets =Pet.query.all()
    pet_form = PetForm()
    if pet_form.validate_on_submit():
        name = pet_form.name.data
        gender = pet_form.gender.data
        age = pet_form.age.data
        description = pet_form.description.data
        contact = pet_form.contact.data

        new_pet = Pet(pet_name=name,gender=gender,age=age,description=description,contact=contact)

        db.session.add(new_pet)
        db.session.commit()

        return redirect(url_for('main.index'))
    return render_template('new_pet.html',pet_form=pet_form,title='Please add pet for adoption',pet=pet,pets=pets)

@main.route('/upload/<uname>/pet/pic',methods= ['POST'])
@login_required
def pet_pic(uname):
    pet=Pet.query.filter_by(user_id=current_user.id)
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        pet.pet_pic_path = path

        db.session.commit()
    return redirect(url_for('main.new_pet',uname=uname))

@main.route('/petcare')
def petcare():

  title= "Pet Care"
  return render_template('petcare.html',title = title)

@main.route('/message/pets',methods=['GET','POST'])
def message():
  message = MessageForm()
  
  all_pets=Pet.query.all()

  if message.validate_on_submit():
    content = message.message.data
    
    new_message = Message(message=content)

    db.session.add(new_message)
    db.session.commit()  
    
  post = 'Engage the owner'
  
#   messages = Message.query.filter_by(pet_id=pet.id).all()  
#   if pet is None:
#     abort(404)
  
  return render_template('adopt_pet.html',all_pets=all_pets, message_form=message,post=post)