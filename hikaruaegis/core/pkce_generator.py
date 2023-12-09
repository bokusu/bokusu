"""Module to generate PKCE codes"""

from base64 import urlsafe_b64encode
from hashlib import sha256
from secrets import token_urlsafe
from typing import TypedDict


class PkceDict(TypedDict):
    """A dictionary containing verifier and code challenge"""
    verifier: str
    code_challenge: str

def generate_pkce_code_verifier(length: int = 128) -> str:
    """
    Generate PKCE code verifier

    :param length: Determine length of character to be generated
    :type length: int = 128
    :return: Code verifier
    :rtype: str
    """
    # Generate a random string for code verifier
    if length < 43 or length > 128:
        raise ValueError("Code verifier length must be between 43 and 128 characters")
    verifier = token_urlsafe(length)
    return verifier[:length]

def generate_pkce_code_challenge(verifier: str) -> str:
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
    code_challenge = urlsafe_b64encode(sha256_hash).rstrip(b'=').decode('utf-8')
    return code_challenge

def build_pcke_challenge(length: int = 128) -> PkceDict:
    """
    Generate a PCKE challenger, complete with verifier and code challenge 👍

    :param length: Determine length of character to be generated
    :type length: int = 128
    :return: Dictionary containing a verifier and code challenger
    :rtype: PckeDict
    """

    verify = generate_pkce_code_verifier(length=length)
    final_dict: PkceDict = {
        "verify": verify,
        "code_challenge": generate_pkce_code_challenge(verify),
    }

    return final_dict
