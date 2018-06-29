from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager

@login_manager.user_loader
def usergetter(isd):
	return User.query.get(isd)
class User(db.Model,UserMixin):
	__tablename__='users'
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(255))
	password=db.Column(db.String(255))
	def verifypass(self,trial):
		return check_password_hash(self.password,trial)
	@property
	def passwd(self):
		raise AttributeError('You cannot read this!')
	@passwd.setter
	def passwd(self,passwd):
		self.password = generate_password_hash(passwd)
	def save(self):
		db.session.add(self)
		db.session.commit()

class Post(db.Model):
	__tablename__='posts'
	id=db.Column(db.Integer,primary_key=True)
	userid=db.Column(db.Integer)
	text=db.Column(db.String(65535))
	def save(self):
		db.session.add(self)
		db.session.commit()
	def countlikes(self):
		likes=Upvote.query.filter(Upvote.postid==self.id).count()
		return likes
	def countdislikes(self):
		dislikes=Downvote.query.filter(Upvote.postid==self.id).count()
		return dislikes
class Comment(db.Model):
	__tablename__='comments'
	id=db.Column(db.Integer,primary_key=True)
	userid=db.Column(db.Integer)
	postid=db.Column(db.Integer)
	text=db.Column(db.String(65535))
	def save(self):
		db.session.add(self)
		db.session.commit()
class Upvote(db.Model):
	__tablename__='upvotes'
	id=db.Column(db.Integer,primary_key=True)
	userid=db.Column(db.Integer)
	postid=db.Column(db.Integer)
	def save(self):
		db.session.add(self)
		db.session.commit()
class Downvote(db.Model):
	__tablename__='downvotes'
	id=db.Column(db.Integer,primary_key=True)
	userid=db.Column(db.Integer)
	postid=db.Column(db.Integer)
	def save(self):
		db.session.add(self)
		db.session.commit()
