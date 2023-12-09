from datetime import datetime
from time import sleep

from rich import print as rprint
from waybackpy import WaybackMachineSaveAPI as SaveApi
from waybackpy.exceptions import MaximumSaveRetriesExceeded as MaxRetries

from hikaru.core.const import USER_AGENT


class WaybackClient:
    """WaybackClient is a wrapper around WaybackPy to make it easier to use."""

    def __init__(self):
        """Initialize client"""
        self.last_snapshot: datetime | None = None
        self.last_url: str | None = None

    def save(self, url: str) -> str:
        """
        Save a URL to the Wayback Machine

        :param url: URL to save
        :type url: str

        :return: URL of the saved page
        :rtype: str
        """
        if self.last_url is not None and self.last_url == url:
            # if the last URL is the same as the current URL, return the last URL
            return self.last_url
        if self.last_snapshot is not None:
            # wait until 6 seconds
            last_snapshot = (datetime.now() - self.last_snapshot).seconds
            if last_snapshot < 6:
                rprint(f"[red]Waiting {6 - last_snapshot} seconds before saving {url}[/red]")
                sleep(6 - last_snapshot)
        # save the URL
        save = SaveApi(url, USER_AGENT)
        try:
            snapshot = save.save()
        except MaxRetries:
            rprint(f"[red]Maximum retries exceeded for {url}, waits for 5 minutes[/red]")
            sleep(300)
            snapshot = save.save()
        # return the URL of the saved page
        return snapshot

WAYBACK_CLIENT = WaybackClient()
"""Constant for WaybackClient instance, used to save last snapshot and last URL"""
