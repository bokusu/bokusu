from typing import Literal
from traceback import print_exc

from bokusu.malscraper.client import MALScraper
from bokusu.core.folder import add_directory
from bokusu.core.secrets import ANIMEPLANET_USERNAME


async def export_animeplanet(media_type: Literal["anime", "manga"]) -> tuple[str | None, bool]:
    """
    Export list from Anime-Planet

    :param media_type: Media type target
    :type media_type: Literal["anime", "manga"]

    :return: Exported list, True if successful, False if not
    :rtype: tuple[str, bool]
    """
    # create MAL-Scraper client

    # create directory for export
    path = add_directory("backup", name="Anime-Planet")

    # export list
    try:
        async with MALScraper() as client:
            export = await client.export_list(
                ANIMEPLANET_USERNAME,
                "animeplanet",
                media_type,
            )
        with open(f"{path}/{media_type}.xml", "w", encoding="utf-8") as file:
            file.write(export)
        return export, True

    except Exception as _:
        print_exc()
        return None, True

