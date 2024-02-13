from json import dumps, loads
from typing import Literal, TypedDict
import requests as req
from traceback import print_exc

from bokusu.core.commons import read_resource
from bokusu.core.secrets import ANILIST_USERNAME, ANILIST_ACCESSTOKEN, ANILIST_REFRESHTOKEN, ANILIST_CLIENTID, ANILIST_CLIENTSECRET, ANILIST_REDIRECTURI, ANILIST_EXPIRESIN
from bokusu.core.folder import add_directory

class GqlVariables(TypedDict):
    """GraphQL variables type"""
    user: str

def load_anilist_gql(media_type: Literal["anime", "manga"],
                     variables: GqlVariables) -> dict[str, str | GqlVariables]:
    """
    Load GraphQL variables and return the dict

    :param media_type: Media type target
    :type media_type: Literal["anime", "manga"]
    :param variables: GraphQL variables
    :type variables: GqlVariables

    :return: GraphQL variables
    :rtype: dict[str, str | GqlVariables]
    """

    # load gql file from module's directory (hikaru/anilist/{media_type}_query.gql)
    gql_file = f"{media_type}_query.gql"
    gql_content = read_resource(__name__, gql_file)

    # return the dict with query and variables keys
    return {"query": gql_content, "variables": variables}


def export_anilist(media_type: Literal["anime", "manga"]) -> bool:
    """
    Export list from AniList

    :param media_type: Media type target
    :type media_type: Literal["anime", "manga"]

    :return: True if successful, False if not
    :rtype: bool
    """
    # create directory for export
    path = add_directory("backup", name="AniList")

    # create GraphQL variables
    variables: GqlVariables = {
        "user": ANILIST_USERNAME,
    }

    # create GraphQL variables dict
    gql_variables = load_anilist_gql(media_type, variables)

    # create GraphQL headers
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {ANILIST_ACCESSTOKEN}",
    }

    # export list
    try:
        export = req.post("https://graphql.anilist.co",
                          headers=headers,
                          data=gql_variables)
        export_json = loads(export.text)
        with open(f"{path}/anilist_{media_type}.json", "w") as f:
            f.write(dumps(export_json, indent=4))
        return True
    except Exception as _:
        print_exc()
        return False
