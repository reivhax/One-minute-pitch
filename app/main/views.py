from flask import render_template,request,redirect,url_for,abort
from flask_login import login_user,login_required,current_user
from . import main

# Views
@main.route('/')
@login_required
def index():
    title = 'Home'
    return render_template('index.html', title = title )
