from app.extensions.database import db
from app.posts.models import Post
from datetime import datetime

def test_posts_update(client):
  # create a new post
  post = Post(slug='life-is-beautiful', name='Life is Beautiful', date=datetime(2022, 5, 6, 6, 0, 0))
  db.session.add(post)
  db.session.commit()

  post.name = 'The Here and Now'
  post.save()

  updated_post = Post.query.filter_by(slug='life-is-beautiful').first()
  assert updated_post.name == 'The Here and Now'

def test_cookie_delete(client):
  # deletes cookie
  posts = Post(slug='test', name='test', date=datetime(2022, 5, 6, 6, 0, 0))
  db.session.add(posts)
  db.session.commit()

  posts.delete()

  deleted_cookie = Post.query.filter_by(slug='test').first()
  assert deleted_cookie is None