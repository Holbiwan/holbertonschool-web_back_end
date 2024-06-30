#!/usr/bin/env python3
"""Authentication service module"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """Function that takes a password string and returns its hash value."""
    pw_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw_bytes, salt)


def _generate_uuid() -> str:
    """Method that returns a string representation of a new UUID."""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        """Initialize a new instance of Auth."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with the provided email and password."""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {email} already exists.")
        except NoResultFound:
            hashed_pwd = _hash_password(password)
            user = self._db.add_user(email, hashed_pwd)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """Validate login credentials."""
        try:
            user = self._db.find_user_by(email=email)
            pw_bytes = password.encode("utf-8")
            match = bcrypt.checkpw(pw_bytes, user.hashed_password)
            return match
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Create a session for a user and return the session ID as a string."""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str):
        """Get a user from the session ID. Returns the user."""
        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id) -> None:
        """Destroy a session for a user by removing the session ID."""
        if user_id:
            self._db.update_user(user_id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> str:
        """Generate a reset password token for the user with the given email."""
        try:
            user = self._db.find_user_by(email=email)
            token = str(uuid.uuid4())
            self._db.update_user(user.id, reset_token=token)
            return token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """Update the user's password using the reset token."""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_pwd = _hash_password(password)
            self._db.update_user(user.id, hashed_password=hashed_pwd)
            self._db.update_user(user.id, reset_token=None)
        except NoResultFound:
            raise ValueError
