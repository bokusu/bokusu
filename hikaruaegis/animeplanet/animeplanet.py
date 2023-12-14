from typing import Literal
from traceback import print_exc

from hikaruaegis.malscraper.client import MALScraper
from hikaruaegis.core.folder import add_directory
from hikaruaegis.core.secrets import ANIMEPLANET_USERNAME


def export_animeplanet(media_type: Literal["anime", "manga"]) -> bool:
    """
    Export list from Anime-Planet

    :param media_type: Media type target
    :type media_type: Literal["anime", "manga"]

    :return: True if successful, False if not
    :rtype: bool
    """
    # create MAL-Scraper client
    client = MALScraper()

    # create directory for export
    path = add_directory("backup", "Anime-Planet")

    # export list
    try:
        export = client.export_list(
            ANIMEPLANET_USERNAME,
            "animeplanet",
            media_type,
            export_to=f"{path}/animeplanet_{media_type}.xml"
        )
        return True
    except Exception as e:
        print_exc()
        return False

