from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any

from poli_enum.country import Country  # type: ignore


@dataclass
class FuzzyDate:
    """Date object that allows for incomplete date values (fuzzy)"""
    year: int | None = None
    """Year"""
    month: int | None = None
    """Month"""
    day: int | None = None
    """Day"""


@dataclass
class MediaTitle:
    """The official titles of the media in various languages"""
    romaji: str | None = None
    """The romanization of the native language title"""
    english: str | None = None
    """The official english title"""
    native: str | None = None
    """Official title in it's native language"""
    userPreferred: str | None = None
    """The currently authenticated users preferred title language. Default romaji for non-authenticated"""


class MediaType(Enum):
    """Media type enum, anime or manga"""
    ANIME = 'ANIME'
    MANGA = 'MANGA'


class MediaFormat(Enum):
    """The format the media was released in"""
    TV = 'TV'
    """Anime broadcast on television"""
    TV_SHORT = 'TV_SHORT'
    """Anime which are under 15 minutes in length and broadcast on television"""
    MOVIE = 'MOVIE'
    """Anime movies with a theatrical release"""
    SPECIAL = 'SPECIAL'
    """Special episodes that have been included in DVD/Blu-ray releases, picture dramas, pilots, etc"""
    OVA = 'OVA'
    """Anime that have been released directly on DVD/Blu-ray without originally going through a theatrical release or television broadcast"""
    ONA = 'ONA'
    """Anime that have been originally released online or are only available through streaming services."""
    MUSIC = 'MUSIC'
    """Short anime released as a music video"""
    MANGA = 'MANGA'
    """Professionally published manga with more than one chapter"""
    NOVEL = 'NOVEL'
    """Written books released as a series of light novels"""
    ONE_SHOT = 'ONE_SHOT'
    """Manga with just one chapter"""


class MediaStatus(Enum):
    """The current releasing status of the media"""
    FINISHED = 'FINISHED'
    """Has completed and is no longer being released"""
    RELEASING = 'RELEASING'
    """Is currently releasing"""
    NOT_YET_RELEASED = 'NOT_YET_RELEASED'
    """To be released at a later date"""
    CANCELLED = 'CANCELLED'
    """Is not and will not be releasing"""
    HIATUS = 'HIATUS'
    """Is currently paused from releasing and will resume at a later date"""


class MediaSeason(Enum):
    """The season the media was initially released in"""
    WINTER = 'WINTER'
    """Months December to February"""
    SPRING = 'SPRING'
    """Months March to May"""
    SUMMER = 'SUMMER'
    """Months June to August"""
    FALL = 'FALL'
    """Months September to November"""


CountryCode = Country
"""ISO 3166-1 alpha-2 country codes"""


class MediaSource(Enum):
    """Source type the media was adapted from"""
    ORIGINAL = 'ORIGINAL'
    """An original production not based of another work"""
    MANGA = 'MANGA'
    """Asian comic book"""
    LIGHT_NOVEL = 'LIGHT_NOVEL'
    """Written work published in volumes"""
    VISUAL_NOVEL = 'VISUAL_NOVEL'
    """Video game driven primary by text and narrative"""
    VIDEO_GAME = 'VIDEO_GAME'
    """Video game"""
    OTHER = 'OTHER'
    """Other"""
    NOVEL = 'NOVEL'
    """Written works not published in volumes"""
    DOUJINSHI = 'DOUJINSHI'
    """Self-published works"""
    ANIME = 'ANIME'
    """Japanese animation"""
    WEB_NOVEL = 'WEB_NOVEL'
    """Written work published online"""
    LIVE_ACTION = 'LIVE_ACTION'
    """Live action media such as movies or TV show"""
    GAME = 'GAME'
    """Games excluding video games"""
    COMIC = 'COMIC'
    """Comics excluding manga"""
    MULTIMEDIA_PROJECT = 'MULTIMEDIA_PROJECT'
    """Multimedia project"""
    PICTURE_BOOK = 'PICTURE_BOOK'
    """Picture book"""


class MediaTrailerSite(Enum):
    """The site the trailer is hosted by"""
    YOUTUBE = 'YOUTUBE'
    """Trailer hosted on Youtube"""
    DAILYMOTION = 'DAILYMOTION'
    """Trailer hosted on Dailymotion"""


@dataclass
class MediaTrailer:
    """Media trailer or advertisement"""
    id: str | None = None
    """The trailer video id"""
    site: MediaTrailerSite | None = None
    """The site the trailer is hosted by"""
    thumbnail: str | None = None
    """The url for the thumbnail image of the video"""


@dataclass
class MediaCoverImage:
    extraLarge: str | None = None
    """The cover image url of the media at its largest size. If this size isn't available, large will be provided instead"""
    large: str | None = None
    """The cover image url of the media at a large size"""
    medium: str | None = None
    """The cover image url of the media at medium size"""
    color: str | None = None
    """Average #hex color of color image"""


@dataclass
class MediaTag:
    """A tag that describes a theme or element of the media"""
    id: int
    """The id of the tag"""
    name: str
    """The name of the tag"""
    description: str | None = None
    """A general description of the tag"""
    category: str | None = None
    """The categories of tags this tag belongs to"""
    rank: int | None = None
    """The relevance ranking of the tag out of the 100 for this media"""
    isGeneralSpoiler: bool | None = None
    """If the tag could be considered to be a spoiler for any media"""
    isMediaSpoiler: bool | None = None
    """If the tag is a spoiler for this media"""
    isAdult: bool | None = None
    """If the tag is only for adult 18+ media"""
    userId: int | None = None
    """The user who submitted the tag"""


@dataclass
class AiringSchedule:
    """Media Airing Schedule. NOTE: We only aim to guarantee that future airing data is present and accurate"""
    id: int
    """The id of the airing schedule item"""
    airingAt: datetime
    """The time the episode airs at"""
    timeUntilAiring: int
    """Seconds until episode starts airing"""
    episode: int
    """The airing episode number"""
    mediaId: int
    """The associate media id of the airing episode"""
    media: dict[str, Any] | None = None
    """The associate  media of the airing episode"""


class ExternalLinkType(Enum):
    INFO = 'INFO'
    STREAMING = 'STREAMING'
    SOCIAL = 'SOCIAL'


@dataclass
class MediaExternalLink:
    """An external link to another site related to the media or staff member"""
    id: int
    """The id of the external link"""
    url: str | None = None
    """The url of the external link"""
    site: str = ""
    """The site location of the external link"""
    siteId: int | None = None
    """The id of the external link on its site"""
    type: ExternalLinkType | None = None
    language: str | None = None
    """Language the site content is in"""
    color: str | None = None
    icon: str | None = None
    """The icon image url of the site. Not available for all links. Transparent PNG 64x64"""
    notes: str | None = None
    isDisabled: bool | None = None


@dataclass
class MediaStreamingEpisode:
    """Data and links to legal streaming episodes on external sites"""
    title: str | None = None
    """Title of the episode"""
    thumbnail: str | None = None
    """Url of episode image thumbnail"""
    url: str | None = None
    """The url of the episode"""
    site: str | None = None
    """The site location of the streaming episodes"""


class MediaRankType(Enum):
    """The type of ranking"""
    RATED = 'RATED'
    """Ranking based on the media's ratings/score"""
    POPULAR = 'POPULAR'
    """Ranking based on the media's popularity"""


@dataclass
class MediaRank:
    """The rankinf of a media in particular time span and format compared to other media"""
    id: int
    """The id of the rank"""
    rank: int
    """The numerical rank of the media"""
    type: MediaRankType
    """The type of ranking"""
    format: MediaFormat
    """The format the media is ranked within"""
    year: int | None = None
    """The year the media is ranked within"""
    season: MediaSeason | None = None
    """The season the media is ranked within"""
    allTime: bool | None = None
    """If the ranking is based on all time instead of a season/year"""
    context: str = ""
    """String that gives context to the ranking type and time span"""


class MediaListStatus(Enum):
    """Media list watching/reading status enum."""
    CURRENT = 'CURRENT'
    """Currently watching/reading"""
    PLANNING = 'PLANNING'
    """Planning to watch/read"""
    COMPLETED = 'COMPLETED'
    """Finished watching/reading"""
    DROPPED = 'DROPPED'
    """Stopped watching/reading before completing"""
    PAUSED = 'PAUSED'
    """Paused watching/reading"""
    REPEATING = 'REPEATING'
    """Re-watching/reading"""""


@dataclass
class ScoreDistribution:
    """A user's list score distribution."""
    score: int | None = None
    amount: int | None = None
    """The amount of list entries with this score"""


@dataclass
class StatusDistribution:
    """A user's list status distribution."""
    status: MediaListStatus | None = None
    amount: int | None = None
    """The amount of list entries with this status"""


@dataclass
class MediaStats:
    """A media's statistics."""
    scoreDistribution: list[ScoreDistribution] | None = None
    statusDistribution: list[StatusDistribution] | None = None


@dataclass
class Media:
    """Anime or Manga"""
    id: int
    """The id of the media"""
    idMal: int | None = None
    """The mal id of the media"""
    title: MediaTitle | None = None
    """The official titles of the media in various languages"""
    type: MediaType | None = None
    """The type of the media; anime or manga"""
    format: MediaFormat | None = None
    """The format the media was released in"""
    status: MediaStatus | None = None
    """The current releasing status of the media"""
    description: str | None = None
    """Short description of the media's story and characters"""
    startDate: FuzzyDate | None = None
    """The first official release date of the media"""
    endDate: FuzzyDate | None = None
    """The last official release date of the media"""
    season: MediaSeason | None = None
    """The season the media was initially released in"""
    seasonYear: int | None = None
    """The season year the media was initially released in"""
    seasonInt: int | None = None
    """The year & season the media was initially released in"""
    episodes: int | None = None
    """The amount of episodes the anime has when complete"""
    duration: int | None = None
    """The general length of each anime episode in minutes"""
    chapters: int | None = None
    """The amount of chapters the manga has when complete"""
    volumes: int | None = None
    """The amount of volumes the manga has when complete"""
    countryOfOrigin: CountryCode | None = None
    """Where the media was created. (ISO 3166-1 alpha-2)"""
    isLicensed: bool | None = None
    """If the media is officially licensed or a self-published doujin release"""
    source: MediaSource | None = None
    """Source type the media was adapted from"""
    hashtag: str | None = None
    """Official Twitter hashtags for the media"""
    trailer: MediaTrailer | None = None
    """Media trailer or advertisement"""
    updatedAt: datetime | None = None
    """When the media's data was last updated"""
    coverImage: MediaCoverImage | None = None
    """The cover images of the media"""
    bannerImage: str | None = None
    """The banner image of the media"""
    genres: list[str] | None = None
    """The genres of the media"""
    synonyms: list[str] | None = None
    """Alternative titles of the media"""
    averageScore: int | None = None
    """A weighted average score of all the user's scores of the media"""
    meanScore: int | None = None
    """The mean score of all the user's scores of the media"""
    popularity: int | None = None
    """The number of users with the media on their list"""
    isLocked: bool | None = None
    """Locked media may not be added to lists our favorited. This may be due to the entry pending for deletion or other reasons."""
    trending: int | None = None
    """The amount of related activity in the past hour"""
    favourites: int | None = None
    """The amount of user's who have favourited the media"""
    tags: list[MediaTag] | None = None
    """List of tags that describes elements and themes of the media"""
    relations: dict[str, Any] | None = None
    """Other media in the same or connecting franchise"""
    characters: dict[str, Any] | None = None
    """The characters in the media"""
    staff: dict[str, Any] | None = None
    """the staff who produced the media"""
    studios: dict[str, Any] | None = None
    """The companies who produced the media"""
    isFavourite: bool = False
    """If the media is marked as favourite by the current authenticated user"""
    isFavouriteBlocked: bool = False
    """If the media is blocked from being added to favourites"""
    isAdult: bool | None = None
    """If the media is intended only for 18+ adult audiences"""
    nextAiringEpisode: AiringSchedule | None = None
    """THe media's next episode airing schedule"""
    airingSchedule: dict[str, Any] | None = None
    """The media's entire airing schedule"""
    trends: dict[str, Any] | None = None
    """The media's daily trend stats"""
    externalLinks: list[MediaExternalLink] | None = None
    """External links to another site related to the media"""
    streamingEpisodes: list[MediaStreamingEpisode] | None = None
    """Data and links to legal streaming episodes on external sites"""
    rankings: list[MediaRank] | None = None
    """The ranking of the media in a particular time span and format compared to other media"""
    mediaListEntry: dict[str, Any] | None = None
    """The authenticated user's media list entry for the media"""
    reviews: dict[str, Any] | None = None
    """User reviews of the media"""
    recommendations: dict[str, Any] | None = None
    """User recommended for similar media"""
    stats: MediaStats | None = None
    siteUrl: str | None = None
    """The url for the media page on the AniList website"""
    autoCreateForumThread: bool | None = None
    """If the media should have forum thread automatically created for it on airing episode release"""
    isRecommendationBlocked: bool | None = None
    """If the media is blocked from receiving recommended to/from"""
    isReviewBlocked: bool | None = None
    """If the media is blocked from being reviewed"""
    modNotes: str | None = None
    """Notes for site moderators"""


@dataclass
class UserAvatar:
    """A user's avatars"""
    large: str | None = None
    """The avatar of user at its largest size"""
    medium: str | None = None
    """The avatar of user at medium size"""


@dataclass
class NotificationOption:
    """Notification option for a user"""
    type: str
    """The type of notification"""
    enabled: bool | None = None
    """Whether this type of notification is enabled"""


@dataclass
class UserOptions:
    """User options for the user"""
    titleLanguage: str | None = None
    """The language the user wants to see media titles in"""
    displayAdultContent: bool | None = None
    """Whether the user has enabled viewing of 18+ content"""
    airingNotifications: bool | None = None
    """Whether the user receives notifications when a show they are watching aires"""
    profileColor: str | None = None
    """The color theme of the users profile"""
    notificationOptions: list[NotificationOption] | None = None
    """Notification options"""


@dataclass
class MediaListOptions:
    """The user's media list options"""
    scoreFormat: str | None = None
    """The score format the user is using for media lists"""
    rowOrder: str | None = None
    """The order the user's anime list is displayed in"""
    animeList: dict[str, Any] | None = None
    """List of anime lists custom lists the user has created"""
    mangaList: dict[str, Any] | None = None
    """List of manga lists custom lists the user has created"""


@dataclass
class User:
    """A user"""
    id: int
    """The id of the user"""
    name: str
    """The name of the user"""
    about: str | None = None
    """The bio written by user (Markdown)"""
    avatar: UserAvatar | None = None
    """The user's avatar images"""
    bannerImage: str | None = None
    """The user's banner images"""
    isFollowing: bool | None = None
    """If the authenticated user if following this user"""
    isFollower: bool | None = None
    """If this user if following the authenticated user"""
    isBlocked: bool | None = None
    """If the user is blocked by the authenticated user"""
    bans: dict[str, Any] | None = None
    options: UserOptions | None = None
    """The user's general options"""
    mediaListOptions: MediaListOptions | None = None
    """The user's media list options"""
    favourites: Favourites | None = None
    """The user's favourites"""
    statistics: UserStatisticTypes | None = None
    """The user's anime & manga statistics"""
    unreadNotificationCount: int | None = None
    """The number of unread notifications the user has"""
    siteUrl: str | None = None
    """The url for the user page on the AniList website"""
    donatorTier: int | None = None
    """The donator tier of the user"""
    donatorBadge: str | None = None
    """The donator badge of the user"""
    moderatorRoles: list[ModRole] | None = None
    """The user's moderator roles if they are a site moderator"""
    createdAt: datetime | None = None
    """When the user's account was created. (Does not exist for accounts created before 2020)"""
    updatedAt: datetime | None = None
    """When the user's data was last updated"""
    previousNames: list[UserPreviousName] | None = None
    """The previous names of the user"""


@dataclass
class MediaList:
    """Media list information"""
    id: int
    """The id of the list entry"""
    mediaId: int
    """The id of the media"""
    status: MediaListStatus | None = None
    """The watching/reading status"""
    score: float | None = None
    """The score of the entry"""
    progress: int | None = None
    """The amount of episodes/chapters consumed by the user"""
    progressVolumes: int | None = None
    """The amount of volumes read by the user"""
    repeat: int | None = None
    """The amount of times the user has rewatched/read the media"""
    priority: int | None = None
    """Priority of planning"""
    private: bool | None = None
    """If the entry should only be visible to authenticated user"""
    notes: str | None = None
    """Text notes"""
    hiddenFromStatusLists: bool | None = None
    """If the entry shown be hidden from non-custom lists"""
    customLists: dict[str, bool] | list[str] | None = None
    """Map of booleans for which custom lists the entry are in"""
    advancedScores: dict[str, float] | None = None
    """Map of advanced scores with name keys"""
    startedAt: FuzzyDate | None = None
    """When the entry was started by the user"""
    completedAt: FuzzyDate | None = None
    """When the entry was completed by the user"""
    updatedAt: datetime | None = None
    """When the entry data was last updated"""
    createdAt: datetime | None = None
    """When the entry data was created"""
    media: Media | None = None
