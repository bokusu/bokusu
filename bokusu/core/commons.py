from pkg_resources import resource_string

def read_resource(path: str, file_name: str) -> str:
    """
    Read a file from a resource

    :param path: Path to the resource
    :type path: str
    :param file_name: File name
    :type file_name: str

    :return: File content
    :rtype: str
    """

    # load file from module's directory (hikaru/{path}/{file_name})
    file_content = resource_string(path, file_name).decode("utf-8")

    # return the file content
    return file_content
