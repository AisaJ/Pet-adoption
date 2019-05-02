from . import main
from flask import render_template,request,redirect,url_for

@main.route('/')
def index():

  title='This works'
  return render_template('index.html',title=title)

@main.route('/petcare')
def petcare():


  title= "Pet Care"
  return render_template('petcare.html',title = title)