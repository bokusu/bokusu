from typing import Literal

import requests as req
import aiohttp

from bokusu.core.const import USER_AGENT


class MALScraper:
    """MAL-Scraper general client"""

    def __init__(self):
        """Initialize client"""
        self.base_url = "https://malscraper.azurewebsites.net"
        self.user_agent = USER_AGENT
        self.origin = self.base_url
        self.referer = self.base_url + "/"

    async def __aenter__(self):
        """Async enter"""
        return self

    def __enter__(self):
        """Throw error if not async"""
        raise RuntimeError("Use async with")

    async def __aexit__(self, exc_type, exc_value, traceback):
        """Async exit"""

    async def export_list(self,
                    username: str,
                    source: Literal[
                        "anilist",
                        "animeplanet",
                        "kitsu",
                        "myanimelist"],
                    media_type: Literal["anime", "manga"],
                    update_on_import: bool = True,
                    use_alt: bool = False,
                    ) -> tuple[str, bool]:
        """
        Export list using malscraper from determined source

        :param username: Username on the platform
        :type username: str
        :param source: Source to scrape
        :type source: Literal["anilist", "animeplanet", "kitsu", "myanimelist"]
        :param media_type: Media type target
        :type media_type: Literal["anime", "manga"]
        :param update_on_import: Allow the entry on the platform to be updated during import? Default: True
        :type update_on_import: bool = True
        :param use_alt: Use alternative mode? For MAL, uses HTML scraping, AniList rounded the score. Default: False
        :type use_alt: bool = False

        :return: XML string of exported list
        :rtype: str
        """
        if use_alt is True and source in ["animeplanet", "kitsu"]:
            raise ValueError(f"Source {source} does not support alt mode")
        alt = "alt" if use_alt else ""
        target =(f"{source}{media_type}{alt}"
                 if source != "myanimelist"
                 else f"{media_type}{alt}")
        body = {
            "username": username,
            "listtype": target,
        }
        if update_on_import:
            body["update_on_import"] = "on"
        # post with body sent as x-www-form-urlencoded

        headers = {
            "Origin": self.origin,
            "Referer": self.referer,
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": self.user_agent,
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.base_url}/scrape",
                                    data=body,
                                    headers=headers) as post:
                text = await post.text()
                return text

