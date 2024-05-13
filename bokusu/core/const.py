from os import getenv as env
from os import path

# script path
__file__: str = path.abspath(__name__)

__version__: str = "0.0.1"

IS_VERBOSE: bool = False
"""Check if the program runs in verbose mode"""

USER_AGENT: str = env("USER_AGENT") or ""

OVERRIDE_PATH: str = env("OVERRIDE_PATH") or ""
"""The path to the user's configured folder to store data"""
