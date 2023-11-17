#!/usr/bin/env python3
"""User declaration"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """User model"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)


if __name__ == "__main__":
    print(User.__tablename__)
    for column in User.__table__.columns:
        print("{}: {}".format(column, column.type))
