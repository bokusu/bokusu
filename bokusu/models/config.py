"""Pydantic-enabled configuration models."""

from pathlib import Path
from typing import Literal, Any, Union

from pydantic import BaseModel, Field, HttpUrl, DirectoryPath
from pydantic_extra_types.language_code import LanguageAlpha2

# Base Class
#############


class BaseServiceConfig(BaseModel):
    """Base configuration for a service."""

    enabled: bool = Field(
        default=True,
        description="Whether backup assistant is enabled for this service.",
    )


class WaybackConfig(BaseModel):
    """Wayback Machine configuration."""

    snap_urls: bool = Field(
        default=True,
        description="Whether to snapshot URLs defined by the service plugins.",
    )
    snap_homepage: bool = Field(
        default=False, description="Whether to snapshot homepage of the service too."
    )


class MalXmlSettings(BaseModel):
    """MyAnimeList-flavored Exported XML settings."""

    overwrite_existing: bool = Field(
        default=True,
        description="Whether to overwrite existing entries when importing back.",
    )
    ignore_missing: bool = Field(
        default=False,
        description="""
        Whether to ignore missing entries.

        True: Missing entry will be ignored.
        False: Missing entry will be added as a comment.
        """,
    )
    compress_to_gzip: Union[Literal["both"], bool] = Field(
        default=False,
        description="Whether to compress XML to gzip. Use 'both' to keep uncompressed XML too.",
        examples=[
            False,
            "both",
        ],
    )


# Base Fields
##############

MalXMLField = Field(
    default=None,
    description="MyAnimeList-flavored Exported XML settings. Use this to override the global settings.",
    json_schema_extra={"nullable": True},
)

WaybackField = Field(
    default=None,
    description="Wayback Machine configuration.",
    json_schema_extra={"nullable": True},
)


# AniList
##########


class AniListClient(BaseModel):
    """AniList client configuration."""

    client_id: int = Field(..., description="The client ID.")
    client_secret: str = Field(
        ...,
        description="The client secret, must be 40 characters long.",
        min_length=40,
        max_length=40,
    )
    redirect_uri: HttpUrl = Field(
        default="https://anilist.co/api/v2/oauth/pin", description="The redirect URI."
    )


class AniListCredentials(BaseModel):
    """AniList credentials."""

    access_token: str = Field(..., description="The access token.")
    refresh_token: str = Field(..., description="The refresh token.")
    expires_at: int = Field(..., description="The expiration in UNIX/POSIX timestamp.")


AniListExports = Literal["automail-json", "json", "rymsf-yaml", "malxml", "all"]


class AniListConfig(BaseServiceConfig):
    """AniList configuration."""

    client: AniListClient = Field(..., description="AniList client configuration.")
    credentials: AniListCredentials = Field(..., description="AniList credentials.")
    exports: Union[list[AniListExports], AniListExports] = Field(
        default=["all"],
        description="The exports to perform.\n\n- automail-json: Automail JSON\n- json: JSON\n- rymsf-yaml: Ryuuganime Media Save File YAML\n- malxml: MyAnimeList-flavored Exported XML\n- all: All of the above.",
        examples=[
            ["json", "malxml"],
            "all",
        ],
    )
    malxml_settings: Union[MalXmlSettings, None] = MalXMLField

    def __init__(self, **data: dict[str, Any]):
        super().__init__(**data)  # type: ignore
        if isinstance(self.exports, str):
            self.exports = [self.exports]


# Anime-Planet Config
######################


class AnimePlanetConfig(BaseServiceConfig):
    """Anime-Planet configuration."""

    username: str = Field(..., description="Username.")
    override_useragent: Union[str, None] = Field(
        default=None,
        description="Override the user-agent string defined in #/profiles/*/global/useragent.",
    )
    malxml_settings: MalXmlSettings = Field(
        ...,
        description="MyAnimeList-flavored Exported XML settings. Use this to override the global settings.",
    )
    wayback_settings: Union[WaybackConfig, None] = WaybackField

    def __post_init__(self):
        if self.override_useragent is not None:
            self.override_useragent = self.override_useragent.strip()

    def __init__(self, **data: dict[str, Any]):
        super().__init__(**data)  # type: ignore
        if isinstance(self.exports, str):
            self.exports = [self.exports]


# Annict Config
################


class AnnictWaybackConfig(WaybackConfig):
    """Annict Wayback Machine configuration."""

    languages: list[Literal["ja", "en"]] = Field(
        default=["ja"],
        description="Languages to snapshot.",
        examples=[
            ["ja", "en"],
        ],
    )


AnnictExports = Literal["malxml", "rymsf-yaml", "logs-txt", "all"]


class AnnictConfig(BaseServiceConfig):
    """Annict configuration."""

    username: str = Field(..., description="Username.")
    exports: Union[list[AnnictExports], AnnictExports] = Field(
        default=["all"],
        description="The exports to perform.\n\n- malxml: MyAnimeList-flavored Exported XML\n- rymsf-yaml: Ryuuganime Media Save File YAML\n- logs-txt: Logs in plain text\n- all: All of the above.",
        examples=[
            ["malxml", "rymsf-yaml"],
            "all",
        ],
    )
    malxml_settings: Union[MalXmlSettings, None] = MalXMLField
    wayback_settings: Union[AnnictWaybackConfig, None] = Field(
        default=None,
        description="Wayback Machine configuration.",
        json_schema_extra={"nullable": True},
    )

    def __init__(self, **data: dict[str, Any]):
        super().__init__(**data)  # type: ignore
        if isinstance(self.exports, str):
            self.exports = [self.exports]


# Profile
##########


class UserSettings(BaseModel):
    """Additional/Overriding settings for a user."""

    enabled: bool = Field(
        default=True, description="Enable backup process from this profile."
    )
    useragent: str | None = Field(
        default=None,
        description="User-agent string to use for the user. Overrides the global user-agent string.",
    )
    """User-agent string to use for the user."""

    def __post_init__(self):
        if self.useragent is not None:
            self.useragent = self.useragent.strip()


class ProfileConfig(BaseModel):
    """Profile Configurations"""

    user_settings: UserSettings = Field(
        ...,
        description="User settings to override the global settings.",
    )
    """User settings to override the global settings."""

    anilist: Union[AniListConfig, None] = Field(
        default=None,
        description="AniList configuration.",
        json_schema_extra={"nullable": True},
    )
    """AniList configuration."""
    animeplanet: Union[AnimePlanetConfig, None] = Field(
        default=None,
        description="Anime-Planet configuration.",
        json_schema_extra={"nullable": True},
    )
    """Anime-Planet configuration."""
    annict: Union[AnnictConfig, None] = Field(
        default=None,
        description="Annict configuration.",
        json_schema_extra={"nullable": True},
    )
    """Annict configuration."""


# Bokusu Main Config
#####################


class Config(BaseModel):
    """Bokusu configuration."""

    default_dump_path: DirectoryPath = Field(
        default=Path.expanduser(Path("~/.bokusu")).resolve(),
        description="The default path to dump backups. By default, it uses %USERPROFILE%/.bokusu on Windows, or ~/.bokusu on POSIX",
    )
    """The default path to dump backups."""
    useragent: Union[str, None] = Field(
        default=None,
        description="The user-agent to use.",
    )
    """The user-agent to use."""
    profiles: dict[str, ProfileConfig] = Field(
        ...,
        description="Profiles.",
    )
    """Profiles."""

    def __post_init__(self):
        if self.useragent is not None:
            self.useragent = self.useragent.strip()
