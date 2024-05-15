from importlib import import_module


class ResourceNotFoundError(Exception):
    """Exception raised when a resource is not found."""


def read_resource(directory: str, file_path: str, return_as_path: bool = False) -> str:
    """
    Gets the content of a file within a python package/module.
    :param package_name: The name of the package.
    :param file_path: The path to the file within the package.
    :param return_as_path: If True, the file path is returned instead of the file content.
    :type package_name: str
    :type file_path: str
    :type return_as_path: bool
    :return: The content of the file.
    :rtype: str
    :raises ResourceNotFoundError: If the file is not found.
    :example:
    >>> read_resource('bokusu', 'core/commons.py')
    """
    try:
        package = import_module("bokusu")
        module_path = package.__path__[0]
        directory = directory.replace(".", "/")
        directory = directory.replace("\\", "/")
        full_file_path = f"{module_path}/{directory}/{file_path}"
        if return_as_path:
            return full_file_path
        with open(full_file_path, "r") as f:
            return f.read()
    except (ImportError, FileNotFoundError):
        raise ResourceNotFoundError(
            f"File '{file_path}' not found inside bokusu package."
        )
