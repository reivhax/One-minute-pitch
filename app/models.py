from . import db

class User(db.Model):
	__tablename__='users'
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(255))
	password=db.Column(db.String(255))
	def verifypass(self,trial):
		return self.password == trial
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
class Downvote(db.Model):
	__tablename__='downvotes'
	id=db.Column(db.Integer,primary_key=True)
	userid=db.Column(db.Integer)
	postid=db.Column(db.Integer)
