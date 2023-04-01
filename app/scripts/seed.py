from app.app import create_app
from app.posts.models import Post
from app.extensions.database import db
from datetime import datetime

if __name__ == '__main__':
  app = create_app()
  app.app_context().push()

# Blog articles inc. name, date
blog_posts_dictionary = {
        'article1': {'name': 'The foundation of happiness', 'date':  datetime(2023, 4, 1, 12, 0, 0)},
        'article2': {'name': 'Life means balance', 'date':  datetime(2023, 5, 3, 12, 0, 0)},
        'article3': {'name': 'The power of words', 'date':  datetime(2023, 6, 1, 12, 0, 0)},
        'article4': {'name': 'Hold your Head up!', 'date':  datetime(2023, 7, 1, 12, 0, 0)},
    }

for slug, values in blog_posts_dictionary.items():
  new_post = Post(slug=slug, name=values['name'], date=values['date'])
  db.session.add(new_post)

db.session.commit()