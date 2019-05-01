from . import db 
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(UserMixin,db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer,primary_key=True)
  username = db.Column(db.String(255),index=True)
  email = db.Column(db.String(255),unique=True,index=True)
  bio = db.Column(db.String(255))
  profile_pic_path = db.Column(db.String())
  password_secure = db.Column(db.String(255))
  role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

  def __repr__(self):
    return f'User{self.username}'

class Role(db.Model):
  __tablename__ = 'roles'
  id = db.Column(db.Integer,primary_key=True)
  name = db.Column(db.String())
  pet_users = db.relationship('User',backref = 'role',lazy="dynamic")

  def __repr__(self):
    return f'User{self.name}'

class Message(db.Model):
  __tablename__ = 'message'
  id = db.Column(db.Integer,primary_key=True)
  message = db.Column(db.String(255))
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
  pet_id = db.Column(db.Integer,db.ForeignKey('pets.id'))

  def message_save(self):
    db.session.add(self)
    db.session.commit()

  def __repr__(self):
    return f'Message{self.message}'

class Pet(db.Model):
  __tablename__ ='pets'
  id =db.Column(db.Integer,primary_key=True)
  pet_name =db.Column(db.String(255))
  gender =db.Column(db.String(255))
  age =db.Column(db.Integer)
  description = db.Column(db.String(255))
  contact = db.Column(db.Integer)
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

  def __repr__(self):
    return f'Pet{self.pet_name}'
