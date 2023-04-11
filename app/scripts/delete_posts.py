from app.posts.models import Post
from app.extensions.database import db

def delete_posts_with_ids(ids):
    for post_id in ids:
        post = Post.query.get(post_id)
        if post:
            db.session.delete(post)
            db.session.commit()
            print(f"Deleted post with id {post_id}")
        else:
            print(f"Post with id {post_id} not found")

if __name__ == '__main__':
    ids_to_delete = [5, 6, 7, 8]
    delete_posts_with_ids(ids_to_delete)
