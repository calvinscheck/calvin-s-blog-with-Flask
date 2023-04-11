from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

# Creating a mixin class that all models can inherit (to have access)
class CRUDMixin():

  def save(self):
    db.session.add(self)
    db.session.commit()
    return self
  def delete(self):
    db.session.delete(self)
    db.session.commit()
    return