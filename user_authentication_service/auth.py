#!/usr/bin/env python3
"""Authentification service module"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """_hash_password function that that takes in
    a password string arguments and returns bytes"""
    pw_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw_bytes, salt)


def _generate_uuid() -> str:
    """_generate_uuid method that return a
    string representation of a new UUID."""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register_user method that register a new user"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {email} already exists.")
        except NoResultFound:
            hashed_pwd = _hash_password(password)
            user = self._db.add_user(email, hashed_pwd)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """valid_login method"""
        try:
            user = self._db.find_user_by(email=email)
            pw_bytes = password.encode("utf-8")
            match = bcrypt.checkpw(
                pw_bytes, user.hashed_password)
            return match
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """create_session method that
        returns the session ID as a string."""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str):
        """get_user_from_session_id method that
        returns the corresponding User or None"""
        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id) -> None:
        """destroy_session method that destroy_session"""
        if user_id:
            self._db.update_user(user_id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> str:
        """get_reset_password_token method that
        Generate reset password token"""
        try:
            user = self._db.find_user_by(email=email)
            token = str(uuid.uuid4())
            self._db.update_user(user.id, reset_token=token)
            return token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """update_password method that update the user pwd"""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_pwd = _hash_password(password)
            self._db.update_user(user.id, hashed_password=hashed_pwd)
            self._db.update_user(user.id, reset_token=None)
        except NoResultFound:
            raise ValueError
