from app.extensions.database import db, CRUDMixin
from datetime import datetime

class Post(db.Model, CRUDMixin):
  id = db.Column(db.Integer, primary_key=True)
  slug = db.Column(db.String(80), unique=True)
  name = db.Column(db.String(80))
  date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Author(db.Model, CRUDMixin):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128))
  # foreign key relationship. That way I can assign different authors to posts
  author_id = db.Column(db.Integer, db.ForeignKey('post.id'))
