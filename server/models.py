from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class Project(db.Model, SerializerMixin):
    pass

    def __repr__(self):
        pass
