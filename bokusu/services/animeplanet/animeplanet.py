from typing import Literal
from traceback import print_exc

from bokusu.malscraper.client import MALScraper
from bokusu.core.folder import add_directory
from bokusu.core.secrets import ANIMEPLANET_USERNAME


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
    path = add_directory("backup", name="Anime-Planet")

    # export list
    try:
        export = client.export_list(
            ANIMEPLANET_USERNAME,
            "animeplanet",
            media_type,
        )
        # write export to file
        with open(f"{path}/{media_type}.xml", "w", encoding="utf-8") as file:
            file.write(export)
        return True

    except Exception as _:
        print_exc()
        return False

