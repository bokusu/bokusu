"""Module to generate PKCE codes"""

import secrets
import hashlib
import base64

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
    verifier = secrets.token_urlsafe(length)
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
    sha256_hash = hashlib.sha256(verifier_bytes).digest()
    code_challenge = base64.urlsafe_b64encode(sha256_hash).rstrip(b'=').decode('utf-8')
    return code_challenge
