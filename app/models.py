from sqlalchemy import Column, Integer, String, Boolean
from app.db import Base

class Todo(Base):
    __tablename__ = 'todos'
    id = Column('id', Integer, primary_key = True)
    title = Column('title', String(200))
    done = Column('done', Boolean, default=False)
