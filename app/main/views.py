from . import main
from flask import render_template
from ..models import User


@main.route('/')
def index():

  title='This works'
  return render_template('index.html',title=title)