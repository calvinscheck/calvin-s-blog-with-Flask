from app.app import create_app
from app.extensions.database import db
from app.posts.models import Post

app = create_app()
app.app_context().push()

post1 = Post.query.filter_by(slug='article1').first()
post2 = Post.query.filter_by(slug='article2').first()
post3 = Post.query.filter_by(slug='article3').first()
post4 = Post.query.filter_by(slug='article4').first()

# Update the content field of each post
post1.content = 'This is the content for article1.'
post2.content = 'This is the content for article2.'
post3.content = 'This is the content for article3.'
post4.content = 'This is the content for article4.'

# Save the updated posts
post1.save()
post2.save()
post3.save()
post4.save()