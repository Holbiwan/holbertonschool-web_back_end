#!/usr/bin/env python3
"""Hash password"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """_hash_password function that that takes in
    a password string arguments and returns bytes"""
    pw_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw_bytes, salt)
