# from flask_login import UserMixin
# from . import login_manager
# from datetime import datetime

# class User(UserMixin,db.Model):
#     __tablename__ = 'users'

#     id = db.Column(db.Integer,primary_key = True)
#     username = db.Column(db.String(255),index = True)
#     email = db.Column(db.String(255),unique = True,index = True)
#     role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
#     password_hash = db.Column(db.String(255))
#     profile_pic_path = db.Column(db.String())
#     bio = db.Column(db.String(255))
#     pets = db.relationship('Pet', backref='author', lazy=True)




# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id)

# class Pet(db.Model):
#     __tablename__='pets'

#     id = db.Column(db.Integer,primary_key = True)
#     pet_pic_path = db.Column(db.String())
#     description = db.Column(db.String())
#     name = db.Column(db.String())
#     gender = db.Column(db.String())
#     age = db.Column(db.String())
#     contact = db.Column(db.String())
#     user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

#     def save_pets(self):
#         db.session.add(self)
#         db.session.commit()

#     @classmethod
#     def get_pets(cls,id):
#         reviews = Pets.query.filter_by(movie_id=id).all()
#         return pets



# class Role(db.Model):
#     __tablename__='roles'
#     name = db.Column(db.String())
#     id = db.Column(db.Integer,primary_key = True)
#     users = db.relationship('User', backref='author', lazy=True)

# class Message(db.Model):
#     __tablename__='messages'
#     id = db.Column(db.Integer,primary_key = True)
#     message = db.Column(db.String())
#     user_id = db.Column(db.Integer,db.ForeignKey("users.id"))          
#     pet_id = db.Column(db.Integer,db.ForeignKey("users.id"))