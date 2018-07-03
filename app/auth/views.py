from flask import render_template,request,redirect,url_for,abort
from flask_login import login_user,login_required,current_user,logout_user
from ..models import User
from .forms import LoginForm,RegisterForm
from . import auth

# Views
@auth.route('/login', methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    title = 'Login'
    Form = LoginForm()
    Error=False
    if Form.validate_on_submit():
        username=str(Form.username.data)
        password=str(Form.password.data)
        if username and password:
            user=User.query.filter(User.username==username).first()
            if user and user.verifypass(password):
                print(password)
                login_user(user,Form.remember.data)
                return redirect(url_for('main.dashboard'))
            Error='Wrong Username or Password'
        else:
            Error='Please Type a Username or Password'
    return render_template('login.html', title = title ,Form=Form,Error=Error)

@auth.route('/register', methods=["GET","POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    title = 'Register'
    Form = RegisterForm()
    Error=False
    if Form.validate_on_submit():
        username=str(Form.username.data)
        password=str(Form.password.data)
        if username and password:
            user=User.query.filter(User.username==username).first()
            if not user:
                user=User(username=username,passwd=password)
                user.save()
                return redirect(url_for('auth.login'))
            Error='Username Already taken'
    return render_template('register.html', title = title ,Form=Form,Error=Error)

@auth.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect(url_for('main.dashboard'))
