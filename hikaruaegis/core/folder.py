"""This module contains functions for setting up folders."""

import os
from platform import system
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

def hide_unhide_directory(path, hide=True):
    """
    Hide or unhide a directory based on the platform.

    :param path: Path to the directory
    :param hide: True to hide, False to unhide
    """
    curr_os = system()
    if curr_os == "Windows":
        try:
            # Get the current attributes
            attributes = os.stat(path).st_file_attributes

            # Set or clear the hidden attribute
            if hide:
                attributes |= 2  # Add the hidden attribute
            else:
                attributes &= ~2  # Remove the hidden attribute

            # Set the new attributes
            os.chflags(path, attributes)
        except Exception as e:
            print(f"Error: {e}")
    elif curr_os == "Darwin":  # macOS
        try:
            # Set or clear the hidden flag using chflags
            flag = "hidden" if hide else "nohidden"
            os.system(f"chflags {flag} '{path}'")
        except Exception as e:
            print(f"Error: {e}")
    else:
        pass