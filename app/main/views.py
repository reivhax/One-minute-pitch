from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from . import main
from .models import Post,Comment,User,Upvote,Downvote

# Views
@main.route('/')
def dashboard():
    title = 'Home'
    posts = Post.query.all()
    return render_template('index.html', title = title )
