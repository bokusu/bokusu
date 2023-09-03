from dataclasses import dataclass


@dataclass
class AniListToken:
    """AniList token"""
    token_type: str
    expires_in: int
    access_token: str
    refresh_token: str

__all__ = ["AniListToken"]
