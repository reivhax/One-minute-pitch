from . import db
from random import randrange
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
	posts = db.relationship('Post', backref='user', lazy='dynamic')
	comments = db.relationship('Comment', backref='user', lazy='dynamic')
	likes = db.relationship('Upvote', backref='user', lazy='dynamic')
	dislikes = db.relationship('Downvote', backref='user', lazy='dynamic')
	favorites=db.relationship('Favourite', backref='user', lazy='dynamic')

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
	def favs(self):
		for fav in self.favorites.all():
			yield fav.post
	def __repr__(self):
		return '<User %r>' % self.username

class Favourite(db.Model):
	__tablename__='favourites'
	id=db.Column(db.Integer,primary_key=True)
	userid=db.Column(db.Integer, db.ForeignKey('users.id'))
	postid=db.Column(db.Integer, db.ForeignKey('posts.id'))
	def save(self):
		db.session.add(self)
		db.session.commit()
	def selfdestruct(self):
		db.session.delete(self)
		db.session.commit()

class Post(db.Model):
	__tablename__='posts'
	id=db.Column(db.Integer,primary_key=True)
	text=db.Column(db.String(65535))
	userid=db.Column(db.Integer, db.ForeignKey('users.id'))
	category=db.Column(db.String(255))
	likes=db.relationship('Upvote', backref='post', lazy='dynamic')
	dislikes=db.relationship('Downvote', backref='post', lazy='dynamic')
	comments=db.relationship('Comment', backref='post', lazy='dynamic')
	userfavs=db.relationship('Favourite', backref='post', lazy='dynamic')

	def save(self):
		db.session.add(self)
		db.session.commit()
	def selfdestruct(self):
		for child in self.likes.all()+self.dislikes.all()+self.comments.all():
			child.selfdestruct()
		db.session.delete(self)
		db.session.commit()

class Comment(db.Model):
	__tablename__='comments'
	id=db.Column(db.Integer,primary_key=True)
	userid=db.Column(db.Integer, db.ForeignKey('users.id'))
	postid=db.Column(db.Integer, db.ForeignKey('posts.id'))
	text=db.Column(db.String(65535))
	def save(self):
		db.session.add(self)
		db.session.commit()
	def selfdestruct(self):
		db.session.delete(self)
		db.session.commit()

class Upvote(db.Model):
	__tablename__='upvotes'
	id=db.Column(db.Integer,primary_key=True)
	userid=db.Column(db.Integer, db.ForeignKey('users.id'))
	postid=db.Column(db.Integer, db.ForeignKey('posts.id'))
	def save(self):
		db.session.add(self)
		db.session.commit()
	def selfdestruct(self):
		db.session.delete(self)
		db.session.commit()

class Downvote(db.Model):
	__tablename__='downvotes'
	id=db.Column(db.Integer,primary_key=True)
	userid=db.Column(db.Integer, db.ForeignKey('users.id'))
	postid=db.Column(db.Integer, db.ForeignKey('posts.id'))
	def save(self):
		db.session.add(self)
		db.session.commit()
	def selfdestruct(self):
		db.session.delete(self)
		db.session.commit()

class Bloopers(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	text=db.Column(db.String(65535))
	@classmethod
	def getrandom(self):
		length=self.query.count()
		for i in range(5):
			yield self.query.get(randrange(length)).text
