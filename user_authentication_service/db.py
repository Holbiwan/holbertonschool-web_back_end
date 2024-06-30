#!/usr/bin/env python3
"""Database module"""

from sqlalchemy import create_engine, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class to interact with the database."""

    def __init__(self) -> None:
        """Initialize a new DB instance."""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Create and return a session object if it doesn't exist."""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database and return the user object."""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Find and return a user based on the provided filters."""
        if not kwargs:
            raise InvalidRequestError("No arguments provided.")
        user = self._session.query(User).filter_by(**kwargs).first()
        if user:
            return user
        raise NoResultFound("No user found with the given parameters.")

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update user attributes and commit changes to the database."""
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            setattr(user, key, value)
        self._session.commit()
