from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from . import main
from .. import db
from ..models import Post,Comment,User,Upvote,Downvote,Favourite

# Views
@main.route('/')
def dashboard():
    title = 'Dashboard' if current_user.is_authenticated else 'Home'
    posts = Post.query.all()
    categories = db.session.query(Post.category).distinct().all()
    defaultcategories = [('pickup lines',),('interview pitch',),('product pitch',),('promotion pitch',)]
    categories = set(categories+defaultcategories)
    print(categories)
    return render_template('index.html', title = title,posts=posts,categories=categories)

@main.route('/manage/')
@login_required
def myaccount():
    title = 'Management'
    posts = current_user.posts.all()
    comments = current_user.comments.all()
    return render_template('manage.html', title = title,posts=posts,comments=comments)

@main.route('/my-favorites/')
@login_required
def favorites():
    title = 'My Favourites'
    posts = current_user.favorites.all()
    posts = map(lambda fav: fav.post,posts)
    return render_template('fav.html', title = title,posts=posts)

@main.route('/fav/<int:id>')
def addfav(id):
    if current_user.is_authenticated:
        posts = current_user.favorites.all()
        userfavs = map(lambda fav: fav.postid,posts)
        if id in userfavs:
            oldfav = current_user.favorites.filter(Post.id==id).first()
            oldfav.selfdestruct()
            return 'Removed'
        newfav = Favourite(userid=current_user.id,postid=id)
        newfav.save()
        return 'Added'
    return 'Error'

@main.route('/newpitch')
def pitch():
    if current_user.is_authenticated:
        newpost = Post(userid=current_user.id,text=request.args['pitch'],category=request.args['category'])
        newpost.save()
        newposts=[newpost]
        return render_template('ajaxresposes.html',type='post',posts=newposts)
    return

@main.route('/newcomment/<int:id>',methods=['POST'])
def comment(id):
    if current_user.is_authenticated:
        newcomment = Comment(
            userid=current_user.id,
            postid=str(request.form['post']),
            text=str(request.form['reaction'])
        )
        newcomment.save()
        newcomments=[newcomment]
        return render_template('ajaxresposes.html',type='comment',comments=newcomments)
    return ''

@main.route('/like/<int:id>')
def like(id):
    if current_user.is_authenticated:
        if current_user.likes.filter(Upvote.postid==id).first():
            return 'Error'
        Upvote(userid=current_user.id,postid=id).save()
        return 'Success'
    return 'Error'

@main.route('/dislike/<int:id>')
def dislike(id):
    if current_user.is_authenticated:
        if current_user.dislikes.filter(Downvote.postid==id).first():
            return 'Error'
        Downvote(userid=current_user.id,postid=id).save()
        return 'Success'
    return 'Error'
@main.route('/delete/comment/<int:id>',methods=["POST"])
def deletecomment(id):
    if current_user.is_authenticated:
        comment=current_user.comments.filter(Comment.id==id).first()
        if not comment:
            return 'Error'
        comment.selfdestruct()
        return 'Success'
    return 'Error'
@main.route('/delete/post/<int:id>',methods=["POST"])
def deletepost(id):
    if current_user.is_authenticated:
        post=current_user.posts.filter(Post.id==id).first()
        if not post:
            return 'Error'
        post.selfdestruct()
        return 'Success'
    return 'Error'
