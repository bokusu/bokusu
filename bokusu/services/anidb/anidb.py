import logging
from asyncio import sleep
from datetime import datetime, timezone
from typing import Literal

import asyncudp  # type: ignore

from bokusu.services.anidb.models import (AniDBAuth, AniDBResponse,
                                          AniDBResponseCode)


class AniDB:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.socket = None
        self.session = ""

    async def __aenter__(self):
        self.socket = await asyncudp.create_socket(remote_addr=(self.host, self.port)) # type: ignore
        return self

    def __enter__(self):
        raise RuntimeError("Use async with")

    async def __aexit__(self, exc_type, exc_value, traceback):  # type: ignore
        self.socket.close() if self.socket else None

    async def __send_cmd(self, command: str) -> tuple[str, str]:
        if not self.socket:
            raise RuntimeError(
                "Socket is not initialized, have you init class with async context?")
        logging.debug(f"Sending command {command}")
        await self.socket.sendto(command.encode("utf-8"))  # type: ignore
        get_resp, addr = await self.socket.recvfrom()  # type: ignore
        await self._delay()
        logging.debug(f"Received response {get_resp} from {addr}")
        return (get_resp, addr)  # type: ignore

    async def _login(self, auth: AniDBAuth) -> AniDBResponse:
        """
        Login to AniDB

        :param auth: AniDB authentication dataclass
        :type auth: AniDBAuth
        :return: AniDB response dataclass
        :rtype: AniDBResponse
        """
        get_resp, _ = await self.__send_cmd(f"AUTH {auth.params}")
        resp = AniDBResponse.from_string(get_resp)
        if resp.return_code == AniDBResponseCode.LOGIN_ACCEPTED:
            self.session = resp.additional_return_string
            logging.debug(f"Logged in with session {self.session}")
        return resp

    async def _logout(self) -> AniDBResponse:
        """
        Logout from AniDB

        :return: AniDB response dataclass
        :rtype: AniDBResponse
        """
        get_resp, _ = await self.__send_cmd(f"LOGOUT s={self.session}")
        return AniDBResponse.from_string(get_resp)

    async def _ping(self) -> AniDBResponse:
        """
        Ping AniDB

        :return: AniDB response dataclass
        :rtype: AniDBResponse
        """
        get_resp, _ = await self.__send_cmd("PING")
        return AniDBResponse.from_string(get_resp)

    async def _notify(self, buddy: bool = False) -> AniDBResponse:
        """
        Check for notifications from AniDB

        :param buddy: Check for buddy notifications
        :type buddy: bool, optional
        :return: AniDB response dataclass
        :rtype: AniDBResponse
        """
        cmd = "NOTIFY s={self.session}"
        if buddy:
            cmd += "&buddy=1"
        get_resp, _ = await self.__send_cmd(f"NOTIFY s={self.session}")
        return AniDBResponse.from_string(get_resp)

    async def _notifylist(self) -> AniDBResponse:
        """
        List notifications from AniDB

        :return: AniDB response dataclass
        :rtype: AniDBResponse
        """
        get_resp, _ = await self.__send_cmd(f"NOTIFYLIST s={self.session}")
        return AniDBResponse.from_string(get_resp)

    async def _notifyget(self, msgtype: Literal["M", "N"], msgid: int) -> AniDBResponse:
        """
        Get a notification from AniDB

        :param msgtype: Message type
        :type msgtype: Literal["M", "N"]
        :param msgid: Message ID
        :type msgid: int
        :return: AniDB response dataclass
        :rtype: AniDBResponse
        """
        get_resp, _ = await self.__send_cmd(f"NOTIFYGET s={self.session}&type={msgtype}&id={msgid}")
        return AniDBResponse.from_string(get_resp)

    async def _mylistexport(self, template: str = "xml") -> AniDBResponse:
        """
        Export MyList to AniDB

        :return: AniDB response dataclass
        :rtype: AniDBResponse
        """
        get_resp, _ = await self.__send_cmd(f"MYLISTEXPORT template={template}&s={self.session}")
        return AniDBResponse.from_string(get_resp)

    # give each process a delay to prevent API violation

    async def _delay(self, seconds: float = 0.5) -> None:
        """
        Delay the process

        :param seconds: Seconds to delay
        :type seconds: float
        """
        await sleep(seconds)

    async def run(self, auth: AniDBAuth) -> None:
        """
        Run the AniDB service

        :param auth: AniDB authentication dataclass
        :type auth: AniDBAuth
        """
        try:
            await self._login(auth)
        except Exception:
            logging.exception("Failed to login")
            raise Exception("Failed to login")
        await self._ping()
        ntf = await self._notify()
        # run additional notification checks
        if ntf.data and ntf.data[1]:
            logging.debug(f"Message notifications: {ntf.data[1]}")
            msglist = await self._notifylist()
            if msglist.data:
                for msg in msglist.data:
                    if msg[0] != "M":
                        continue
                    logging.debug(f"Message notification: {msg}")
                    msgget = await self._notifyget("M", int(msg[1]))
                    if msgget.data:
                        logging.debug(f"Message notification data: {msgget.data}")
                        dta = msgget.data[0]
                        # check if it's from the system with title starts with "[MY LIST EXPORT]"
                        if dta[4] != "2":
                            continue
                        if not dta[5].startswith("[MY LIST EXPORT]"):
                            continue
                        print(f"""MyList export notification:
Date: {datetime.fromtimestamp(int(dta[3]), tz=timezone.utc)}
From: {dta[2]}
Subject: {dta[5]}

{dta[6]}

----------
Notice from cartridge:
To prevent API violation, you must manually read the message from following link:
https://anidb.net/user/mail/{dta[0]}
Then, bokusu will attempt to send the export request once message is read and
your list is ready to be exported.

AniDB cartridge for bokusu will exit.
""")
                        await self._logout()
                        return
            else:
                logging.debug("No message notifications")
        else:
            logging.debug("No notifications")
        await self._mylistexport()
        await self._logout()
