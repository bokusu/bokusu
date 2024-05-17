"""This module contains functions for setting up folders."""

import os
from pathlib import Path

from bokusu.core.const import GITHUB_ACTIONS, OVERRIDE_PATH, Status, pp


def create_folder(*path: str) -> Path:
    """
    Creates a folder if it doesn't exist.

    :param path: The path(s) to the folder.
    :type path: tuple[str]
    :return: The path to the folder.
    :rtype: Path
    """
    target = os.path.join(*path)
    os.makedirs(target, exist_ok=True)
    return Path(target).resolve()


def get_box_root() -> Path:
    """
    Get the root directory of Bokusu.

    On Windows, it should be %USERPROFILE%\\.bokusu, but on POSIX, it should be ~/.bokusu.
    However, on CI/CD (GitHub Actions), it should be the current repo directory.

    :return: The path to the root directory.
    :rtype: Path
    """
    if GITHUB_ACTIONS:
        return Path(".").resolve()
    path = Path("~/.bokusu").expanduser()
    if path.exists():
        return path
    pp.print(Status.ERROR, "Bokusu root directory not found. Creating one...")
    return create_folder(str(path))


def add_directory(*path: str, name: str | None = None) -> Path:
    """
    Creates a directory if it doesn't exist.

    :param path: The path(s) to the directory.
    :type path: tuple[str]
    :param name: The name of the directory. Defaults to None.
    :type name: str | None
    :return: The path to the directory.
    :rtype: Path
    """
    root = Path(OVERRIDE_PATH) or get_box_root()
    target = os.path.join(str(root), *path)
    if name:
        pp.print(Status.INFO, f"Creating directory for {name} on {target}...")
    else:
        pp.print(Status.INFO, f"Creating directory on {target}...")

    target = create_folder(target)

    return target
