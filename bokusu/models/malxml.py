"""Generate MAL XML file from defined schema and data"""

from dataclasses import dataclass as dcls
from datetime import datetime as dtm
from enum import Enum

from bokusu.models.xml import XML, Tag

################################################################################
# SHARED ENUMS
################################################################################


class ReplayValue(Enum):
    """Replay value enum."""

    VLOW = "Very Low"
    """Very low."""
    LOW = "Low"
    """Low."""
    MEDIUM = "Medium"
    """Medium."""
    HIGH = "High"
    """High."""
    VHIGH = "Very High"
    """Very high."""

    @classmethod
    def from_int(cls, value: int) -> "ReplayValue":
        """
        Converts an integer to a replay value.

        :param value: The integer value.
        :type value: int
        :return: The replay value.
        :rtype: ReplayValue
        """
        if value == 1:
            return cls.VLOW
        if value == 2:
            return cls.LOW
        if value == 3:
            return cls.MEDIUM
        if value == 4:
            return cls.HIGH
        if value == 5:
            return cls.VHIGH
        raise ValueError(f"Invalid replay value: {value}")

    @classmethod
    def from_str(cls, value: str) -> "ReplayValue":
        """
        Converts a string to a replay value.

        :param value: The string value.
        :type value: str
        :return: The replay value.
        :rtype: ReplayValue
        """
        if value == "Very Low":
            return cls.VLOW
        if value == "Low":
            return cls.LOW
        if value == "Medium":
            return cls.MEDIUM
        if value == "High":
            return cls.HIGH
        if value == "Very High":
            return cls.VHIGH
        raise ValueError(f"Invalid replay value: {value}")


class Priority(Enum):
    """Priority enum."""

    LOW = "Low"
    """Low priority."""
    MEDIUM = "Medium"
    """Medium priority."""
    HIGH = "High"
    """High priority."""

    @classmethod
    def from_int(cls, value: int) -> "Priority":
        """
        Converts an integer to a priority.

        :param value: The integer value.
        :type value: int
        :return: The priority.
        :rtype: Priority
        """
        if value == 1:
            return cls.LOW
        if value == 2:
            return cls.MEDIUM
        if value == 3:
            return cls.HIGH
        raise ValueError(f"Invalid priority value: {value}")

    @classmethod
    def from_str(cls, value: str) -> "Priority":
        """
        Converts a string to a priority.

        :param value: The string value.
        :type value: str
        :return: The priority.
        :rtype: Priority
        """
        if value == "Low":
            return cls.LOW
        if value == "Medium":
            return cls.MEDIUM
        if value == "High":
            return cls.HIGH
        raise ValueError(f"Invalid priority value: {value}")


class PostToSNS(Enum):
    """Post to SNS enum."""

    DEFAULT = "default"
    """Follow default setting."""
    ALLOW = "allow"
    """Post every time (without confirmation)."""
    ASK_EVERY_TIME = "ask_every_time"
    """Post with confirmation"""
    DISALLOW = "disallow"
    """Do not post"""


################################################################################
# USER DETAILS
################################################################################


class ExportType(Enum):
    """Export type enum."""

    ANIME = 1
    MANGA = 2


@dcls
class BaseMyStatus:
    """Stores general statistics and information about the user"""

    user_export_type: ExportType
    """The export type."""
    user_id: int | None = None
    """The user's ID."""
    user_name: str | None = None
    """The user's name."""
    user_total_completed: int | None = None
    """The total number of entries completed."""
    user_total_onhold: int | None = None
    """The total number of entries on hold."""
    user_total_dropped: int | None = None
    """The total number of entries dropped."""


@dcls
class AnimeMyStatus(BaseMyStatus):
    """Stores general statistics and information about the user's anime list"""

    user_total_anime: int | None = None
    """The total number of entries."""
    user_total_watching: int | None = None
    """The total number of entries being watched."""
    user_total_plantowatch: int | None = None
    """The total number of entries in the plan to watch list."""

    @property
    def as_tag(self) -> Tag:
        """
        Converts the user's status to a MAL XML tag.

        :param user: The user's status.
        :type user: AnimeMyStatus
        :return: The MAL XML tag.
        :rtype: Tag
        """
        user_tag = Tag("myinfo")

        fields = [
            ("user_id", str(self.user_id)),
            ("user_name", self.user_name or ""),
            (
                "user_export_type",
                str(self.user_export_type.value) if self.user_export_type else "",
            ),
            ("user_total_anime", str(self.user_total_anime or "")),
            ("user_total_watching", str(self.user_total_watching or "")),
            ("user_total_completed", str(self.user_total_completed or "")),
            ("user_total_on_hold", str(self.user_total_onhold or "")),
            ("user_total_dropped", str(self.user_total_dropped or "")),
            ("user_total_plantowatch", str(self.user_total_plantowatch or "")),
        ]

        for field, value in fields:
            user_tag.add_child(Tag(field, value))

        return user_tag


@dcls
class MangaMyStatus(BaseMyStatus):
    """Stores general statistics and information about the user's manga list"""

    user_total_manga: int | None = None
    """The total number of entries."""
    user_total_reading: int | None = None
    """The total number of entries being read."""
    user_total_plantoread: int | None = None
    """The total number of entries in the plan to read list."""

    @property
    def as_tag(self) -> Tag:
        """
        Converts the user's status to a MAL XML tag.

        :param user: The user's status.
        :type user: MangaMyStatus
        :return: The MAL XML tag.
        :rtype: Tag
        """
        user_tag = Tag("myinfo")

        fields = [
            ("user_id", str(self.user_id)),
            ("user_name", self.user_name or ""),
            (
                "user_export_type",
                str(self.user_export_type.value) if self.user_export_type else "",
            ),
            ("user_total_manga", str(self.user_total_manga or "")),
            ("user_total_reading", str(self.user_total_reading or "")),
            ("user_total_completed", str(self.user_total_completed or "")),
            ("user_total_on_hold", str(self.user_total_onhold or "")),
            ("user_total_dropped", str(self.user_total_dropped or "")),
            ("user_total_plantoread", str(self.user_total_plantoread or "")),
        ]

        for field, value in fields:
            user_tag.add_child(Tag(field, value))

        return user_tag


################################################################################
# ANIME
################################################################################


class AnimeStatus(Enum):
    """Anime status enum."""

    WATCHING = "Watching"
    """Entry is currently being watched."""
    PLAN_TO_WATCH = "Plan to Watch"
    """Entry is in the plan to watch list."""
    COMPLETED = "Completed"
    """Entry is completely watched."""
    ON_HOLD = "On-Hold"
    """Entry is on hold/paused."""
    DROPPED = "Dropped"
    """Entry is dropped, not watching anymore."""


class AnimeType(Enum):
    """Anime type enum."""

    TV = "TV"
    """TV series."""
    OVA = "OVA"
    """OVA series."""
    MOVIE = "Movie"
    """Movie."""
    SPECIAL = "Special"
    """Special episode."""
    ONA = "ONA"
    """ONA series."""
    MUSIC = "Music"
    """Music video."""
    CM = "CM"
    """Commercial."""
    PV = "PV"
    """Promotional video."""
    TV_SPECIAL = "TV Special"
    """TV special episode."""
    UNKNOWN = "Unknown"
    """Unknown type."""

    @classmethod
    def from_str(cls, value: str) -> "AnimeType":
        """
        Converts a string to an anime type.

        :param value: The string value.
        :type value: str
        :return: The anime type.
        :rtype: AnimeType
        """
        if value == "TV":
            return cls.TV
        if value == "OVA":
            return cls.OVA
        if value == "Movie":
            return cls.MOVIE
        if value == "Special":
            return cls.SPECIAL
        if value == "ONA":
            return cls.ONA
        if value == "Music":
            return cls.MUSIC
        if value == "CM":
            return cls.CM
        if value == "PV":
            return cls.PV
        if value == "TV Special":
            return cls.TV_SPECIAL
        return cls.UNKNOWN


class AnimeStorageMedium(Enum):
    """Storage medium enum."""

    HARD_DRIVE = "Hard Drive"
    """Hard drive."""
    EXTERNAL_HD = "External HD"
    """External hard drive."""
    NAS = "NAS"
    """Network-attached storage."""
    BLU_RAY = "Blu-ray"
    """Blu-ray disc."""
    DVD_CD = "DVD / CD"
    """DVD or CD."""
    RETAIL_DVD = "Retail DVD"
    """Retail DVD."""
    VHS = "VHS"
    """VHS tape."""

    @classmethod
    def from_str(cls, value: str) -> "AnimeStorageMedium":
        """
        Converts a string to a storage medium.

        :param value: The string value.
        :type value: str
        :return: The storage medium.
        :rtype: AnimeStorageMedium
        """
        if value == "Hard Drive":
            return cls.HARD_DRIVE
        if value == "External HD":
            return cls.EXTERNAL_HD
        if value == "NAS":
            return cls.NAS
        if value == "Blu-ray":
            return cls.BLU_RAY
        if value == "DVD / CD":
            return cls.DVD_CD
        if value == "Retail DVD":
            return cls.RETAIL_DVD
        if value == "VHS":
            return cls.VHS
        raise ValueError(f"Invalid storage medium: {value}")


@dcls
class Anime:
    """Entry on the anime list with general and personal information."""

    # REQUIRED, FILLED BY MANY EXPORTERS
    series_animedb_id: int
    """The series' ID from MAL Database."""
    my_score: int = 0
    """The score the user gave to the series. Should be between 0 and 10."""
    my_status: AnimeStatus = AnimeStatus.PLAN_TO_WATCH
    """The status of the series on the user's list."""
    my_watched_episodes: int = 0
    """The total number of episodes watched."""
    update_on_import: bool = True
    """Allow the importer to CRUD the entry."""

    # OPTIONAL
    series_title: str | None = None
    """The series' title."""
    series_type: AnimeType | None = None
    """The series' type."""
    series_episodes: int | None = None
    """The total number of episodes from upstream."""
    my_id: int = 0
    """The entry's ID on the user's list. Unused by MAL, might be legacy."""
    my_start_date: dtm | None = None
    """The date the user started watching the series."""
    my_finish_date: dtm | None = None
    """The date the user finished watching the series."""
    my_rated: None = None
    """Unknown field, might be legacy."""
    my_storage: AnimeStorageMedium | None = None
    """The storage medium the series is stored."""
    my_storage_value: float | None = None
    """The amount of storage the series occupies. Artifacts from AniDB, unused by MAL."""
    my_comments: str = ""
    """Comments about the series."""
    my_times_watched: int = 0
    """The number of times the user watched the series."""
    my_rewatch_value: ReplayValue | None = None
    """The rewatch value."""
    my_priority: Priority | None = None
    """The priority of the series."""
    my_tags: list[str] | None = None
    """The tags associated with the series."""
    my_rewatching: bool = False
    """If the user is rewatching the series."""
    my_rewatching_ep: int = 0
    """Supposedly the episode the user is currently rewatching, unused by MAL."""
    my_discuss: bool = False
    """If the user wants to discuss the series."""
    my_sns: PostToSNS = PostToSNS.DEFAULT
    """The user's SNS settings."""

    @property
    def as_tag(self) -> Tag:
        """
        Converts an anime entry to a MAL XML tag.

        :param anime: The anime entry.
        :type anime: Anime
        :return: The MAL XML tag.
        :rtype: Tag
        """
        anime_tag = Tag("anime")

        fields = [
            ("series_animedb_id", str(self.series_animedb_id)),
            ("series_title", self.series_title or ""),
            ("series_type", self.series_type.value if self.series_type else ""),
            ("series_episodes", str(self.series_episodes or "")),
            ("my_id", str(self.my_id)),
            ("my_watched_episodes", str(self.my_watched_episodes)),
            (
                "my_start_date",
                self.my_start_date.strftime("%Y-%m-%d")
                if self.my_start_date
                else "0000-00-00",
            ),
            (
                "my_finish_date",
                self.my_finish_date.strftime("%Y-%m-%d")
                if self.my_finish_date
                else "0000-00-00",
            ),
            ("my_score", str(self.my_score)),
            ("my_status", self.my_status.value),
            ("my_rated", self.my_rated or ""),
            ("my_storage", self.my_storage.value if self.my_storage else ""),
            ("my_storage_value", str(self.my_storage_value or 0.00)),
            ("my_comments", self.my_comments),
            ("my_times_watched", str(self.my_times_watched)),
            (
                "my_rewatch_value",
                self.my_rewatch_value.value if self.my_rewatch_value else "",
            ),
            ("my_rewatching", "1" if self.my_rewatching else "0"),
            ("my_rewatching_ep", str(self.my_rewatching_ep)),
            ("my_priority", self.my_priority.value if self.my_priority else ""),
            ("my_tags", ",".join(self.my_tags) if self.my_tags else ""),
            ("my_discuss", "1" if self.my_discuss else "0"),
            ("my_sns", self.my_sns.value),
            ("update_on_import", "1" if self.update_on_import else "0"),
        ]

        req_cdata = ["series_title", "my_comments", "my_tags"]
        """Fields that require to be wrapped in CDATA."""
        for field, value in fields:
            anime_tag.add_child(Tag(field, value, cdata=field in req_cdata))

        return anime_tag


################################################################################
# MANGA
################################################################################


class MangaStatus(Enum):
    """Manga status enum."""

    READING = "Reading"
    """Entry is currently being read."""
    PLAN_TO_READ = "Plan to Read"
    """Entry is in the plan to read list."""
    COMPLETED = "Completed"
    """Entry is completely read."""
    ON_HOLD = "On-Hold"
    """Entry is on hold/paused."""
    DROPPED = "Dropped"
    """Entry is dropped, not reading anymore."""


class MangaStorageMedium(Enum):
    """Storage medium enum."""

    HARD_DRIVE = "Hard Drive"
    """Hard drive."""
    EXTERNAL_HD = "External HD"
    """External hard drive."""
    NAS = "NAS"
    """Network-attached storage."""
    BLU_RAY = "Blu-ray"
    """Blu-ray disc."""
    DVD_CD = "DVD / CD"
    """DVD or CD."""
    RETAIL_MANGA = "Retail Manga"
    """Retail manga."""
    MAGAZINE = "Magazine"
    """Magazine."""

    @classmethod
    def from_str(cls, value: str) -> "MangaStorageMedium":
        """
        Converts a string to a storage medium.

        :param value: The string value.
        :type value: str
        :return: The storage medium.
        :rtype: MangaStorageMedium
        """
        if value == "Hard Drive":
            return cls.HARD_DRIVE
        if value == "External HD":
            return cls.EXTERNAL_HD
        if value == "NAS":
            return cls.NAS
        if value == "Blu-ray":
            return cls.BLU_RAY
        if value == "DVD / CD":
            return cls.DVD_CD
        if value == "Retail Manga":
            return cls.RETAIL_MANGA
        if value == "Magazine":
            return cls.MAGAZINE
        raise ValueError(f"Invalid storage medium: {value}")


@dcls
class Manga:
    """Entry on the manga list with general and personal information."""

    # REQUIRED, FILLED BY MANY EXPORTERS
    manga_mangadb_id: int
    """The manga's ID from MAL Database."""
    my_score: int = 0
    """The score the user gave to the series. Should be between 0 and 10."""
    my_status: MangaStatus = MangaStatus.PLAN_TO_READ
    """The status of the series on the user's list."""
    my_read_volumes: int = 0
    """The total number of volumes read."""
    my_read_chapters: int = 0
    """The total number of chapters read."""
    update_on_import: bool = True
    """Allow the importer to CRUD the entry."""

    # OPTIONAL
    manga_title: str | None = None
    """The manga's title."""
    manga_volumes: int | None = None
    """The total number of volumes from upstream."""
    manga_chapters: int | None = None
    """The total number of chapters from upstream."""
    my_id: int = 0
    """The entry's ID on the user's list."""
    my_start_date: dtm | None = None
    """The date the user started reading the series."""
    my_finish_date: dtm | None = None
    """The date the user finished reading the series."""
    my_scanlation_group: str = ""
    """The scanlation group. Unused by MAL, legacy field."""
    my_storage: MangaStorageMedium | None = None
    """The storage medium the series is stored."""
    my_retail_volumes: int = 0
    """The total number of retail volumes, only for `my_storage == RETAIL_MANGA`."""
    my_comments: str = ""
    """Comments about the series."""
    my_times_read: int = 0
    """The number of times the user read the series."""
    my_reread_value: ReplayValue | None = None
    """The reread value."""
    my_priority: Priority | None = None
    """The priority of the series."""
    my_tags: list[str] | None = None
    """The tags associated with the series."""
    my_rereading: bool = False
    """If the user is rereading the series."""
    my_discuss: bool = False
    """If the user wants to discuss the series."""
    my_sns: PostToSNS = PostToSNS.DEFAULT
    """The user's SNS settings."""

    @property
    def as_tag(self) -> Tag:
        """
        Converts a manga entry to a MAL XML tag.

        :param manga: The manga entry.
        :type manga: Manga
        :return: The MAL XML tag.
        :rtype: Tag
        """
        manga_tag = Tag("manga")

        fields = [
            ("manga_mangadb_id", str(self.manga_mangadb_id)),
            ("manga_title", self.manga_title or ""),
            ("manga_volumes", str(self.manga_volumes or "")),
            ("manga_chapters", str(self.manga_chapters or "")),
            ("my_id", str(self.my_id)),
            ("my_read_volumes", str(self.my_read_volumes)),
            ("my_read_chapters", str(self.my_read_chapters)),
            (
                "my_start_date",
                self.my_start_date.strftime("%Y-%m-%d")
                if self.my_start_date
                else "0000-00-00",
            ),
            (
                "my_finish_date",
                self.my_finish_date.strftime("%Y-%m-%d")
                if self.my_finish_date
                else "0000-00-00",
            ),
            ("my_score", str(self.my_score)),
            ("my_status", self.my_status.value),
            ("my_scanlation_group", self.my_scanlation_group),
            ("my_storage", self.my_storage.value if self.my_storage else ""),
            ("my_retail_volumes", str(self.my_retail_volumes)),
            ("my_comments", self.my_comments),
            ("my_times_read", str(self.my_times_read)),
            (
                "my_reread_value",
                self.my_reread_value.value if self.my_reread_value else "",
            ),
            ("my_rereading", "YES" if self.my_rereading else "NO"),
            ("my_priority", self.my_priority.value if self.my_priority else ""),
            ("my_tags", ",".join(self.my_tags) if self.my_tags else ""),
            ("my_discuss", "YES" if self.my_discuss else "NO"),
            ("my_sns", self.my_sns.value),
            ("update_on_import", "1" if self.update_on_import else "0"),
        ]

        req_cdata = ["manga_title", "my_comments", "my_scanlation_group", "my_tags"]
        """Fields that require to be wrapped in CDATA."""
        for field, value in fields:
            manga_tag.add_child(Tag(field, value, cdata=field in req_cdata))

        return manga_tag


################################################################################
# EXPORT
################################################################################


@dcls
class MalXML:
    """MyAnimeList XML export."""

    user: AnimeMyStatus | MangaMyStatus
    """The user's status."""
    entries: list[Anime | Manga]
    """The user's entries."""

    @property
    def as_xml(self) -> XML:
        """
        Converts the export to MAL XML.

        :param export: The export.
        :type export: Export
        :return: The MAL XML.
        :rtype: XML
        """
        xml = XML()
        mal = Tag("myanimelist")

        mal.add_child(self.user.as_tag)
        for entry in self.entries:
            mal.add_child(entry.as_tag)

        xml.add_child(mal)

        return xml
