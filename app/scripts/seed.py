from app.app import create_app
from app.posts.models import Post
from app.extensions.database import db

if __name__ == '__main__':
  app = create_app()
  app.app_context().push()

# Blog articles inc. name, date
blog_posts_dictionary = {
        'article1': {'name': 'The foundation of happiness', 'date': '20.02.2022'},
        'article2': {'name': 'Life means balance', 'date': '23.2.2022'},
        'article3': {'name': 'The power of words', 'date': '30.3.2022'},
        'article4': {'name': 'Hold your Head up!', 'date': '20.05.2022'},
    }

for slug, Post in blog_posts_dictionary.items():
  new_post = Post(slug=slug, name=Post['name'], date=Post['date'])
  db.session.add(new_post)

db.session.commit()