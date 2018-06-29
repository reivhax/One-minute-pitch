from flask import render_template,request,redirect,url_for,abort
from flask_login import login_user,login_required,current_user
from .forms import LoginForm
from . import auth

# Views
@auth.route('/login')
def login():
    title = 'Login'
    Form = LoginForm()
    return render_template('login.html', title = title ,Form=Form)
