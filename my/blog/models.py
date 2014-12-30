from sqlalchemy import (
    Column,
    Date,
    DateTime,
    Integer,
    ForeignKey,
    Unicode,
    UnicodeText,
)
from sqlalchemy.orm import (
    relationship,
)
from pyramid_sqlalchemy import (
    BaseObject as Base,
    Session as DBSession,
)


class Blog(Base):
    __tablename__ = 'blogs'
    query = DBSession.query_property()
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), unique=True)
    title = Column(UnicodeText)
    description = Column(UnicodeText)


class Entry(Base):
    __tablename__ = 'entries'
    query = DBSession.query_property()
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    title = Column(UnicodeText)
    content = Column(UnicodeText)
    blog_id = Column(Integer, ForeignKey('blogs.id'))
    blog = relationship('Blog', backref='entries')
