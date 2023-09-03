"""Server for the firstrun app."""

import asyncio

import aiohttp
from fastapi import FastAPI
from dacite import from_dict

from models.anilist import AniListToken

app = FastAPI()


async def get_anilist_token(auth_code: str) -> AniListToken:
    """
    Get AniList token from the auth code

    :param auth_code: The auth code
    :type auth_code: str
    :return: The AniList token
    :rtype: AniListToken
    """
    async with aiohttp.ClientSession() as session:
        async with session.post("https://anilist.co/api/v2/oauth/token", data={
            "grant_type": "authorization_code",
            "client_id": "",
            "client_secret": "",
            "redirect_uri": "http://127.0.0.1:8000/anilist/",
            "code": auth_code
        }) as response:
            data = await response.json()
            return from_dict(AniListToken, data)

@app.get("/anilist/")
async def anilist(code: str):
    """
    Return the AniList code

    :param code: The code to return
    :type code: str
    :return: The code
    :rtype: str
    """
    task = await asyncio.create_task(get_anilist_token(code))
    print(task)
    return code
