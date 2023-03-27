from app.extensions.database import db
from datetime import datetime

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  slug = db.Column(db.String(80), unique=True)
  name = db.Column(db.String(80))
  date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))