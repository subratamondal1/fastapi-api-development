"""Encrypt (Hash) Password"""

from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    """Encryption (Hashing) Class"""

    def bcrypt(password: str):
        """Encryption (Hashing) Method"""
        return password_context.hash(password)
