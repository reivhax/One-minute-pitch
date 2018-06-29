from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from . import main
from ..models import Post,Comment,User,Upvote,Downvote

# Views
@main.route('/')
def dashboard():
    title = 'Dashboard' if current_user.is_authenticated else 'Home'
    posts = Post.query.all()
    return render_template('index.html', title = title,posts=posts)

@main.route('/newpitch')
def pitch():
    newpost = Post(userid=current_user.id,text=request.args['pitch'])
    newpost.save()
    posts = Post.query.all()
    return render_template('ajaxresponses.html',posts=posts)
