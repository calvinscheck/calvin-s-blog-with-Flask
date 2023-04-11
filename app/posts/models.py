from app.extensions.database import db, CRUDMixin
from datetime import datetime

class Author(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    # relationship to connect authors with posts
    posts = db.relationship('Post', backref='author', lazy=True)

class Post(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(80))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # foreign key relationship. That way, you can assign different authors to posts
    author_id = db.Column(db.Integer, db.ForeignKey('author.id', name='post_author_id'))
    content = db.Column(db.Text)
