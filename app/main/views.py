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
    if current_user.is_authenticated:
        newpost = Post(userid=current_user.id,text=request.args['pitch'])
        newpost.save()
        posts = Post.query.all()
        return render_template('ajaxresposes.html',posts=posts)
    return

@main.route('/like/<id>')
def like(id):
    if Upvote.query.filter(Upvote.userid==current_user.id,Upvote.postid==id).first():
        return 'Error'
    Upvote(userid=current_user.id,postid=id).save()
    return 'Success'

@main.route('/dislike/<id>')
def dislike(id):
    if Downvote.query.filter(Downvote.userid==current_user.id,Downvote.postid==id):
        return 'Error'
    Downvote(userid=current_user.id,postid=id).save()
    return 'Success'
