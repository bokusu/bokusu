from pathlib import Path
from importlib import import_module

class ResourceNotFoundError(Exception):
    """Exception raised when a resource is not found."""


def read_resource(directory: str, file_path: str, return_as_path: bool = False) -> str:
    """
    Gets the content of a file within a python package/module.
    :param directory: The directory within the package.
    :param file_path: The path to the file within the directory.
    :param return_as_path: If True, the file path is returned instead of the file content.
    :type directory: str
    :type file_path: str
    :type return_as_path: bool
    :return: The content of the file or the file path.
    :rtype: str
    :raises ResourceNotFoundError: If the file is not found.
    :example:
    >>> read_resource('core', 'commons.py')
    <<< <content of bokusu/core/commons.py>
    """
    try:
        package = import_module("bokusu")
        module_path = package.__path__[0]
        full_file_path = Path(module_path) / directory / file_path
        # check if the file exists
        if not full_file_path.is_file():
            raise FileNotFoundError
        if return_as_path:
            return str(full_file_path)
        with open(full_file_path, "r") as f:
            return f.read()
    except (ImportError, FileNotFoundError) as err:
        raise ResourceNotFoundError(
            f"File '{file_path}' not found inside bokusu package."
        ) from err
