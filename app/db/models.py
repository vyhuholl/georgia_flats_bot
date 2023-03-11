from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """
    Модель пользователя.

    Attributes:
        id: идентификатор пользователя
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
