from . import db

class User(db.Model):
	__tablename__='users'
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(255))
	password=db.Column(db.String(255))
	def save(self):
		db.session.add(self)
		db.session.commit()
class Post(db.Model):
	__tablename__='posts'
	id=db.Column(db.Integer,primary_key=True)
    userid=db.Column(db.Integer)
	text=db.Column(db.String(255))
	def save(self):
		db.session.add(self)
		db.session.commit()
