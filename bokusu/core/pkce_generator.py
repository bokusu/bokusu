"""Module to generate PKCE codes"""

from base64 import urlsafe_b64encode
from hashlib import sha256
from secrets import token_urlsafe
from dataclasses import dataclass


class LengthError(ValueError):
    """Raised when length is not between 43 and 128 characters"""

@dataclass
class PkceCodes:
    """A class containing verifier and code challenge"""
    verifier: str
    code_challenge: str


class PkceGenerator:
    """A class to generate PKCE codes"""

    def __init__(self, length: int = 128):
        """
        Initialize the class

        :param length: Determine length of character to be generated
        :type length: int = 128
        """
        self.code_verifier = self._code_verifier(length=length)
        self.code_challenge = self._code_challenge(self.code_verifier)

    @staticmethod
    def _code_verifier(length: int = 128) -> str:
        """
        Generate PKCE code verifier

        :param length: Determine length of character to be generated
        :type length: int = 128
        :return: Code verifier
        :rtype: str
        """
        # Generate a random string for code verifier
        if length < 43 or length > 128:
            raise LengthError(
                "Code verifier length must be between 43 and 128 characters")
        verifier = token_urlsafe(length)
        return verifier[:length]

    @staticmethod
    def _code_challenge(verifier: str) -> str:
        """
        Generate code challenge if required

        :param verifier: Code verifier generated from generate_pkce_code_verifier()
        :type verifier: str
        :return: Code challenge
        :rtype: str
        """
        # Generate code challenge from code verifier using SHA-256
        verifier_bytes = verifier.encode('ascii')
        sha256_hash = sha256(verifier_bytes).digest()
        code_challenge = urlsafe_b64encode(
            sha256_hash).rstrip(b'=').decode('utf-8')
        return code_challenge

    def get_codes(self) -> PkceCodes:
        """
        Return PKCE codes

        :return: PKCE codes
        :rtype: PkceCodes
        """
        return PkceCodes(self.code_verifier, self.code_challenge)
