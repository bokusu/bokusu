"""This module contains functions for setting up folders."""

import os
from typing import Optional

def add_directory(path: str, name: Optional[str] = None) -> None:
    """
    Creates a directory if it doesn't exist.
    
    :param path: The path to the directory.
    :type path: str
    :param name: The name of the directory. If None, the path will be used.
    :type name: str | None
    :return: Should return None.
    :rtype: None
    """
    print(f"Creating directory for {name}")
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print(f"Directory for {name} already exists.")
