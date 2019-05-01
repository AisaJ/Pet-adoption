from . import main
from flask import render_template,flash,abort,redirect,url_for
from ..models import User,Pet,Message
from .. import db

@main.route('/')
def index():

  title='This works'
  return render_template('index.html',title=title)