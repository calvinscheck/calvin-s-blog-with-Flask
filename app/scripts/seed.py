from app.app import create_app
from app.posts.models import Post, Author
from app.extensions.database import db
from datetime import datetime

if __name__ == '__main__':
  app = create_app()
  app.app_context().push()

# Create authors
author1 = Author(name="Author 1")
author2 = Author(name="Author 2")
db.session.add(author1)
db.session.add(author2)
db.session.commit()

# Create Posts and assigning them to the previous created authors
blog_posts_dictionary = {
    'article1': {'name': 'The foundation of happiness', 'date':  datetime(2023, 4, 1, 12, 0, 0), 'author_id': author1.id, 'content': 'Content for article1'},
    'article2': {'name': 'Life means balance', 'date':  datetime(2023, 5, 3, 12, 0, 0), 'author_id': author2.id, 'content': 'Content for article2'},
    'article3': {'name': 'The power of words', 'date':  datetime(2023, 6, 1, 12, 0, 0), 'author_id': author1.id, 'content': 'Content for article3'},
    'article4': {'name': 'Hold your Head up!', 'date':  datetime(2023, 7, 1, 12, 0, 0), 'author_id': author2.id, 'content': 'Content for article4'},
}

for slug, values in blog_posts_dictionary.items():
    new_post = Post(slug=slug, name=values['name'], date=values['date'], author_id=values['author_id'], content=values['content'])
    db.session.add(new_post)

db.session.commit()