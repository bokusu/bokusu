from datetime import datetime
from datetime import time as dt_tm
from datetime import timezone as dt_tz
from enum import Enum
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field

from bokusu.models.malxml import (
    Anime,
    AnimeStatus,
    AnimeStorageMedium,
    AnimeType,
    Manga,
    MangaStatus,
    MangaStorageMedium,
    PostToSNS,
    ReplayValue,
    MalXML,
    AnimeMyStatus,
    MangaMyStatus,
    ExportType,
)
from bokusu.models.malxml import Priority as MALPriority


class MediaType(str, Enum):
    """List of allowed media type"""

    animation = "animation"
    comic = "comic"
    game = "game"
    tv = "tv"
    movie = "movie"
    book = "book"
    podcast = "podcast"
    other = "other"


class Season(str, Enum):
    """Season of the year"""

    spring = "spring"
    summer = "summer"
    fall = "fall"
    winter = "winter"


class Priority(str, Enum):
    """Priority of the media"""

    very_low = "very_low"
    low = "low"
    medium = "medium"
    high = "high"
    very_high = "very_high"


class UserEntryStatus(str, Enum):
    """User entry status"""

    watching = reading = playing = listening = current = "current"
    watched = read = played = listened = completed = "completed"
    on_hold = onhold = paused = "onhold"
    stopped = dropped = "dropped"
    plan_to_watch = plan_to_read = plan_to_play = plan_to_listen = planned = "planned"
    rewatching = rereading = replaying = relistening = repeat = "repeat"
    not_interested = notinterested = "notinterested"


class Date(BaseModel):
    """Schema for date and time"""

    start: datetime | None = Field(None, description="Start date and time")
    finish: datetime | None = Field(None, description="Finish date and time")


class ExtendedDate(Date):
    """Extended date and time"""

    season: Season | None = Field(None, description="Season of the year")
    time: dt_tm | None = Field(None, description="Time of the day")
    timezone: dt_tz | None = Field(None, description="Timezone")


class VideoProgress(BaseModel):
    """Schema for video progress"""

    episode: int | None = Field(None, description="Episode number")
    season: int | None = Field(None, description="Season number")


class BookProgress(BaseModel):
    """Schema for book progress"""

    chapter: int | None = Field(None, description="Chapter number")
    volume: int | None = Field(None, description="Volume number")
    page: int | None = Field(None, description="Page number")


Mappings = dict[str, str | int | dict[str, str | int | None] | None]
"""Type alias for mappings"""


ExtendedScore = dict[str, int | float | None]
"""Type alias for extended score"""

MediaIdType = Literal["int", "slug", "uuid", "base64", "url", "hash", "custom"]
"""Type alias for media id type"""


class MediaIdentifier(BaseModel):
    """Schema for media identifier"""

    type: MediaIdType = Field(..., description="Type of media identifier")
    value: str = Field(..., description="Value of media identifier")
    additional: dict[MediaIdType, str] | None = Field(
        None, description="Additional media identifier"
    )


class Title(BaseModel):
    """Schema for title"""

    model_config = ConfigDict(  # type: ignore
        extra="allow",
        validate_assignment=True,
    )

    native: str | None = Field(None, description="Native title")
    localized: str | None = Field(None, description="Localized title")
    transliterated: str | None = Field(None, description="Transliterated title")
    english: str | None = Field(None, description="English title")


class Score(BaseModel):
    """Schema for score"""

    model_config = ConfigDict(  # type: ignore
        validate_assignment=True,
    )

    value: int | float | None = Field(None, description="Score value")
    maximum: int | float | None = Field(None, description="Maximum score value")
    extended: ExtendedScore | None = Field(None, description="Extended score")


class MediaEntry(BaseModel):
    """Schema for media entry"""

    model_config = ConfigDict(  # type: ignore
        extra="allow",
        validate_assignment=True,
    )

    id: MediaIdentifier = Field(..., description="Media identifier in service")
    title: Title = Field(..., description="Title of the media")
    type: MediaType = Field(..., description="Type of media")
    subtype: str | None = Field(None, description="Subtype of media")
    status: UserEntryStatus = Field(..., description="Status of user entry")
    progress: VideoProgress | BookProgress = Field(
        ..., description="Current progress of user"
    )
    upstream_progress: VideoProgress | BookProgress = Field(
        ..., description="Progress from upstream service"
    )
    date: Date = Field(..., description="Date and time user started and finished")
    notes: str | None = Field(None, description="Notes about the media")
    repeat_count: int | None = Field(None, description="Number of times repeated")
    score: Score = Field(None, description="Score of the media")
    entryid: MediaIdentifier | None = Field(
        None, description="Identifier of the entry in user's list"
    )
    tags: list[str] | str | None = Field(None, description="User defined tags")
    priority: Priority | None = Field(None, description="Priority of the media")
    storage_medium: str | None = Field(None, description="Storage medium")
    replaylikelihood: Priority | None = Field(None, description="Likelihood of replay")
    is_private: bool | None = Field(None, description="Is the entry private")
    mappings: Mappings | None = Field(None, description="Mappings to other services")
    updated: datetime | None = Field(None, description="Last updated date and time")
    created: datetime | None = Field(None, description="Creation date and time")
    upstream_metadata: dict[str, Any] | None = Field(
        None, description="Metadata from upstream service"
    )
    local_metadata: dict[str, Any] | None = Field(
        None, description="(Additional) local metadata"
    )

    @property
    def to_malxml(self) -> Anime | Manga:
        title = self.title.transliterated or self.title.native
        mal_id = self.mappings.get("myanimelist", None) if self.mappings else None
        mal_id = int(mal_id) if mal_id else 0  # type: ignore
        score = self.score.value if self.score.value else 0
        score = round(score)
        if isinstance(self.tags, str):
            self.tags = [self.tags]
        if self.type == MediaType.animation:
            status = {
                UserEntryStatus.current: AnimeStatus.WATCHING,
                UserEntryStatus.completed: AnimeStatus.COMPLETED,
                UserEntryStatus.dropped: AnimeStatus.DROPPED,
                UserEntryStatus.paused: AnimeStatus.ON_HOLD,
                UserEntryStatus.planned: AnimeStatus.PLAN_TO_WATCH,
                UserEntryStatus.repeat: AnimeStatus.COMPLETED,
            }
            final_status = status.get(self.status, AnimeStatus.PLAN_TO_WATCH)
            episodes = (
                self.progress.episode
                if isinstance(self.progress, VideoProgress)
                else None
            )
            episodes = episodes or 0
            ueps = (
                self.upstream_progress.episode
                if isinstance(self.upstream_progress, VideoProgress)
                else None
            )
            ueps = ueps or 0
            if self.priority == Priority.very_low or not self.priority:
                self.priority = Priority.low
            elif self.priority == Priority.very_high:
                self.priority = Priority.high

            return Anime(
                my_comments=self.notes or "",
                my_discuss=False,
                my_finish_date=self.date.finish,
                my_id=0,
                my_priority=MALPriority.from_str(self.priority),
                my_rated=None,
                my_rewatch_value=ReplayValue.from_str(self.replaylikelihood)
                if self.replaylikelihood
                else None,
                my_rewatching_ep=0,
                my_rewatching=self.status == UserEntryStatus.repeat,
                my_score=score,
                my_sns=PostToSNS.DISALLOW if self.is_private else PostToSNS.DEFAULT,
                my_start_date=self.date.start,
                my_status=final_status,
                my_storage_value=0.00,
                my_storage=AnimeStorageMedium.from_str(self.storage_medium)
                if self.storage_medium
                else None,
                my_tags=self.tags,
                my_times_watched=self.repeat_count or 0,
                my_watched_episodes=episodes,
                series_animedb_id=mal_id,
                series_episodes=ueps,
                series_title=title,
                series_type=AnimeType.from_str(self.subtype) if self.subtype else None,
                update_on_import=True,
            )
        elif self.type in [MediaType.comic, MediaType.book]:
            status = {
                UserEntryStatus.current: MangaStatus.READING,
                UserEntryStatus.completed: MangaStatus.COMPLETED,
                UserEntryStatus.dropped: MangaStatus.DROPPED,
                UserEntryStatus.paused: MangaStatus.ON_HOLD,
                UserEntryStatus.planned: MangaStatus.PLAN_TO_READ,
                UserEntryStatus.repeat: MangaStatus.COMPLETED,
            }
            final_status = status.get(self.status, MangaStatus.PLAN_TO_READ)
            chapters = (
                self.progress.chapter
                if isinstance(self.progress, BookProgress)
                else None
            )
            chapters = chapters or 0
            volumes = (
                self.progress.volume
                if isinstance(self.progress, BookProgress)
                else None
            )
            volumes = volumes or 0
            uchs = (
                self.upstream_progress.chapter
                if isinstance(self.upstream_progress, BookProgress)
                else None
            )
            uchs = uchs or 0
            uvols = (
                self.upstream_progress.volume
                if isinstance(self.upstream_progress, BookProgress)
                else None
            )
            uvols = uvols or 0
            if self.priority == Priority.very_low or not self.priority:
                self.priority = Priority.low
            elif self.priority == Priority.very_high:
                self.priority = Priority.high

            return Manga(
                manga_chapters=chapters,
                manga_mangadb_id=mal_id,
                manga_title=title,
                manga_volumes=uvols,
                my_comments=self.notes or "",
                my_discuss=False,
                my_finish_date=self.date.finish,
                my_id=0,
                my_priority=MALPriority.from_str(self.priority),
                my_read_chapters=uchs,
                my_read_volumes=volumes,
                my_reread_value=ReplayValue.from_str(self.replaylikelihood)
                if self.replaylikelihood
                else None,
                my_rereading=self.status == UserEntryStatus.repeat,
                my_retail_volumes=0,
                my_scanlation_group="",
                my_score=score,
                my_sns=PostToSNS.DISALLOW if self.is_private else PostToSNS.DEFAULT,
                my_start_date=self.date.start,
                my_status=final_status,
                my_storage=MangaStorageMedium.from_str(self.storage_medium)
                if self.storage_medium
                else None,
                my_tags=self.tags,
                my_times_read=self.repeat_count or 0,
                update_on_import=True,
            )
        else:
            raise ValueError("Media type is not defined")


class Header(BaseModel):
    """Information about the export"""

    version: int | float | str = Field(..., description="Version of the export")
    media_type: MediaType | list[MediaType] = Field(
        ..., description="Type of media in the export"
    )
    name: str = Field(None, description="Name of the export")
    description: str | None = Field(None, description="Description of the export")
    service_details: dict[str, Any] | None = Field(
        None, description="Details about the service"
    )
    exported_details: dict[str, Any] | None = Field(
        None, description="Details about the export"
    )
    user_details: dict[str, Any] | None = Field(
        None, description="Details about the user"
    )
    additional: dict[str, Any] | None = Field(
        None, description="Additional information"
    )


def convert_to_malxml(data: list[MediaEntry]) -> MalXML:
    """Convert data to MALXML"""
    childs: list[Anime | Manga] = []
    mtype: MediaType | None = None
    totals = {
        UserEntryStatus.current: 0,
        UserEntryStatus.completed: 0,
        UserEntryStatus.dropped: 0,
        UserEntryStatus.paused: 0,
        UserEntryStatus.planned: 0,
        UserEntryStatus.repeat: 0,
    }
    head: AnimeMyStatus | MangaMyStatus | None = None
    for entry in data:
        if len(childs) > 1:
            # check if media type is same with previous entry
            if isinstance(childs[-1], Anime) and entry.type == MediaType.animation:
                childs.append(entry.to_malxml)
                mtype = MediaType.animation
                totals[entry.status] += 1
            elif isinstance(childs[-1], Manga) and entry.type in [
                MediaType.comic,
                MediaType.book,
            ]:
                childs.append(entry.to_malxml)
                mtype = MediaType.comic
                totals[entry.status] += 1
            else:
                raise ValueError("Media type is different from previous entry")
    if mtype == MediaType.animation:
        head = AnimeMyStatus(
            user_export_type=ExportType.ANIME,
            user_total_anime=len(data),
            user_total_watching=totals[UserEntryStatus.current],
            user_total_completed=totals[UserEntryStatus.completed]
            + totals[UserEntryStatus.repeat],
            user_total_onhold=totals[UserEntryStatus.paused],
            user_total_dropped=totals[UserEntryStatus.dropped],
            user_total_plantowatch=totals[UserEntryStatus.planned],
        )
    elif mtype in [MediaType.comic, MediaType.book]:
        head = MangaMyStatus(
            user_export_type=ExportType.MANGA,
            user_total_manga=len(data),
            user_total_reading=totals[UserEntryStatus.current],
            user_total_completed=totals[UserEntryStatus.completed]
            + totals[UserEntryStatus.repeat],
            user_total_onhold=totals[UserEntryStatus.paused],
            user_total_dropped=totals[UserEntryStatus.dropped],
            user_total_plantoread=totals[UserEntryStatus.planned],
        )
    else:
        raise ValueError("Media type is not defined")
    return MalXML(
        user=head,
        entries=childs,
    )


class HeaderedRymsf(BaseModel):
    """Headered response for RYMSF"""

    model_config = ConfigDict(  # type: ignore
        extra="allow",
        validate_assignment=True,
    )

    header: dict[str, Any] = Field(..., description="Header of the file")
    data: list[MediaEntry] = Field(None, description="Exported data")

    @property
    def to_malxml(self) -> MalXML:
        return convert_to_malxml(self.data)
