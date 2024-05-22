from os import getenv as env
from os import path
from pathlib import Path

from librensetsu.const import IS_GITHUB_WORKFLOW  # type: ignore
from librensetsu.prettyprint import Platform, PrettyPrint, Status  # type: ignore

# script path
__file__: str = path.abspath(__name__)

__version__: str = "0.0.1"

IS_VERBOSE: bool = False
"""Check if the program runs in verbose mode"""

USER_AGENT: str = env("USER_AGENT") or ""
"""User agent for HTTP requests"""

GITHUB_ACTIONS: bool = IS_GITHUB_WORKFLOW
"""Check if the program runs on GitHub Actions"""


OVERRIDE_PATH: Path | str = ""
"""The path to the user's configured folder to store data"""

CONFIG_PATH: Path | str = ""
"""The path to the configuration file"""

pp = PrettyPrint(Platform.SYSTEM)
"""Pretty print object"""

__all__ = [
    "IS_VERBOSE",
    "USER_AGENT",
    "GITHUB_ACTIONS",
    "OVERRIDE_PATH",
    "CONFIG_PATH",
    "pp",
    "Status",
]
