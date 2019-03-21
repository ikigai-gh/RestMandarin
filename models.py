from sqlalchemy import Column, Integer, String, ForeignKey, ARRAY
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    email = Column(String(50))
    phone = Column(String(20))

    def __repr__(self):
        return f'<User id: {self.id}, name: {self.name}>'


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String(50))
    tags = Column(ARRAY(String))
    content = Column(String)

    def __repr__(self):
        return f'<Post id: {self.id}, title: {self.title}>'
