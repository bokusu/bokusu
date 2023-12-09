from dataclasses import dataclass
from datetime import datetime
from typing import Any, Literal

media_type = Literal[
    'animation',
    'comic',
    'game',
    'tv',
    'movie',
    'book',
    'podcast',
    'other'
]
"""List of allowed media type"""

@dataclass
class Date:
    """Schema for date and time"""
    start: datetime | None = None
    finish: datetime | None = None
    season: Literal[
        'spring',
        'summer',
        'fall',
        'winter'
    ] | None = None
    time: datetime | None = None

@dataclass
class Progress:
    """Progress"""
    episode: int | None = None
    """Episode in shows"""
    season: int | None = None
    """Season in shows"""
    chapter: int | None = None
    """Chapter in books"""
    volume: int | None = None
    """Volume in books"""

@dataclass
class ExtendedProgress(Progress):
    """Extended progress"""
    isRepeating: bool | None = None
    """Is user currently repeating the title?"""

@dataclass
class ExtendedScore:
    """Extended score"""
    story: float | int | None = None
    """Story score"""
    visual: float | int | None = None
    """Visual score"""
    sound: float | int | None = None
    """Sound score"""

@dataclass
class Mappings:
    """Entry mapping to external sites"""
    aniDb: str | None = None
    anilist: str | None = None
    animePlanet: str | None = None
    aniSearch: str | None = None
    annict: str | None = None
    bangumi: str | None = None
    goodreads: str | None = None
    imdb: str | None = None
    kaize: str | None = None
    kinopoisk: str | None = None
    kitsu: str | None = None
    livechart: str | None = None
    mangaUpdates: str | None = None
    myanimelist: str | None = None
    myshows: str | None = None
    nautiljon: str | None = None
    notifyMoe: str | None = None
    novelUpdates: str | None = None
    otakOtaku: str | None = None
    shikimori: str | None = None
    simkl: str | None = None
    tmdb: str | None = None
    trakt: str | None = None
    tvmaze: str | None = None

@dataclass
class MediaEntry:
    """Metadata of the title"""
    id: str | int
    """Media ID in the database"""
    title: str
    """Media title"""
    status: Literal[
        'current',
        'paused',
        'dropped',
        'planned',
        'nointerest',
        'completed',
        'repeat'
    ]
    """Status of the media"""
    current: ExtendedProgress
    """User progress of the media"""
    date: Date
    """User start and end date consuming media"""
    notes: str | None
    """User notes"""
    repeatcount: int | None
    """Count of how much the media has been repeated, 0 for none"""
    score: float | int | None
    """User vote/score/rate"""
    slug: str | None = None
    """Media slug as ID"""
    tags: str | list[str] | None = None
    """User tag"""
    priority: Literal[
        'high',
        'medium',
        'low'
    ] | None = None
    """User priority for the media to consume"""
    storageMedium: Literal[
        'audiotape',
        'bluray',
        'cloud',
        'drive',
        'dvd',
        'externaldrive',
        'nas',
        'other',
        'retail',
        'theater',
        'tvbroadcast',
        'vhs',
    ] | None = None
    """User storage medium"""
    replaylikelyhood: Literal[
        'verylow',
        'low',
        'medium',
        'high',
        'veryhigh',
    ] | None = None
    """Likelyhood user would replay the title"""
    upstream: Progress | None = None
    """Media progress of release"""
    isPrivate: bool | None = None
    """Is the title set to private on user's list?"""
    extendedScore: ExtendedScore | None = None
    """Extended vote/score/rating"""
    reactions: Literal[
        'laughing',
        'unconditioned',
        'sleepy',
        'amazed',
        'happy',
        'loved',
        'confused',
        'enjoyed',
        'motivated',
        'disgusted',
        'scared',
        'sad',
        'shocked',
        'mad'
    ] | None = None
    """User's reaction to the title"""
    mappings: Mappings | None = None
    """External sites mapping to the entry"""
    updated: datetime | None = None
    """Updated time of the entry list"""
    created: datetime | None = None
    """Created date of the entry list"""
    metadata: dict[str, Any] | None = None
    """Extended details of the title"""

@dataclass
class FileMetadata:
    version: int | float | str
    """Version of the Media Save File"""
    mediaType: media_type
    """Media type of exported data"""
    name: str | None = None
    """Name of the file"""
    description: str | None = None
    """Description of the file"""
    service: dict[str, Any] | None = None
    """Extended details of the service"""
    exported: dict[str, Any] | None = None
    """Extended details of the exported file"""
    user: dict[str, Any] | None = None
    """Extended details of the user"""

@dataclass
class Headered:
    metadata: FileMetadata
    """Metadata of the file"""
    entries: list[MediaEntry]
    """List of exported data"""
