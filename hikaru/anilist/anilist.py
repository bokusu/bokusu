from json import dumps
from typing import Literal

from hikaru.core.commons import read_resource


def load_anilist_gql(media_type: Literal["anime", "manga"],
                     variables: dict[str, str | int]) -> dict[str, str | dict[str, str]]:
    """
    Load GraphQL variables and return the dict

    :param media_type: Media type target
    :type media_type: Literal["anime", "manga"]
    :param variables: GraphQL variables
    :type variables: dict[str, str | int]

    :return: GraphQL variables
    :rtype: dict[str, str | dict[str, str]]
    """

    # load gql file from module's directory (hikaru/anilist/{media_type}_query.gql)
    gql_file = f"{media_type}_query.gql"
    gql_content = read_resource(__name__, gql_file)

    # parse variables into JSON string
    variables_json = dumps(variables)

    # return the dict with query and variables keys
    return {"query": gql_content, "variables": variables_json}
