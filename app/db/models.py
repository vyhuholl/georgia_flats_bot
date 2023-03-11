"""User model for the database."""

from sqlalchemy import CheckConstraint, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """
    User model.

    Attributes:
        id: идентификатор пользователя
        city: город, в котором пользователь ищет съёмное жильё
        min_price: минимальная цена, по которой он готов снимать жильё
        max_price: максимальная цена, по которой он готов снимать жильё
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    city = Column(String, nullable=False)

    min_price = Column(
        Integer, CheckConstraint("min_price >=0 "), default=0, nullable=False,
    )

    max_price = Column(Integer, CheckConstraint("min_price >=0 "), default=None)
