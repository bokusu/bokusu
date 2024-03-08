from dataclasses import dataclass
from enum import Enum
from typing import Literal


def convert_to_params(data: dict[str, str | int | bool | None],
                      retain_bool: bool = False) -> str:
    """
    Convert a dataclass to a string params for AniDB to understand

    :param data: Dataclass to convert
    :type data: dict[str, str | int | bool | None]
    :param retain_bool: Retain boolean values in the string so that they are not removed, defaults to False
    :type retain_bool: bool, optional
    :return: String params
    :rtype: str
    """
    strings = ""
    for key, value in data.items():
        if value is not None:
            match str(type(value)):
                case "<class 'bool'>":
                    value = int(value)
                    if value == 0 and not retain_bool:
                        continue
                case "<class 'str'>":
                    value = value
                case "<class 'int'>":
                    value = str(value)
                case _:
                    raise ValueError(f"Invalid type {type(value)}")
            strings += f"{key}={value}&"
    return strings[:-1]


class AniDBInvalidType(Exception):
    """AniDB invalid type exception"""


class AniDBResponseCode(Enum):
    """Enum of known AniDB response codes"""
    LOGIN_ACCEPTED = 200
    LOGIN_ACCEPTED_NEW_VERSION = 201
    LOGGED_OUT = 203
    RESOURCE = 205
    STATS = 206
    TOP = 207
    UPTIME = 208
    ENCRYPTION_ENABLED = 209
    MYLIST_ENTRY_ADDED = 210
    MYLIST_ENTRY_DELETED = 211
    ADDED_FILE = 214
    ADDED_STREAM = 215
    EXPORT_QUEUED = 217
    EXPORT_CANCELLED = 218
    ENCODING_CHANGED = 219
    FILE = 220
    MYLIST = 221
    MYLIST_STATS = 222
    WISHLIST = 223
    NOTIFICATION = 224
    GROUP_STATUS = 225
    WISHLIST_ENTRY_ADDED = 226
    WISHLIST_ENTRY_DELETED = 227
    WISHLIST_ENTRY_UPDATED = 228
    MULTIPLE_WISHLIST = 229
    ANIME = 230
    ANIME_BEST_MATCH = 231
    RANDOM_ANIME = 232
    ANIME_DESCRIPTION = 233
    REVIEW = 234
    CHARACTER = 235
    SONG = 236
    ANIMETAG = 237
    CHARACTERTAG = 238
    EPISODE = 240
    UPDATED = 243
    TITLE = 244
    CREATOR = 245
    NOTIFICATION_ENTRY_ADDED = 246
    NOTIFICATION_ENTRY_DELETED = 247
    NOTIFICATION_ENTRY_UPDATE = 248
    MULTIPLE_NOTIFICATION = 249
    GROUP = 250
    CATEGORY = 251
    BUDDY_LIST = 253
    BUDDY_STATE = 254
    BUDDY_ADDED = 255
    BUDDY_DELETED = 256
    BUDDY_ACCEPTED = 257
    BUDDY_DENIED = 258
    VOTED = 260
    VOTE_FOUND = 261
    VOTE_UPDATED = 262
    VOTE_REVOKED = 263
    HOT_ANIME = 265
    RANDOM_RECOMMENDATION = 266
    RANDOM_SIMILAR = 267
    NOTIFICATION_ENABLED = 270
    NOTIFYACK_SUCCESSFUL_MESSAGE = 281
    NOTIFYACK_SUCCESSFUL_NOTIFICATION = 282
    NOTIFICATION_STATE = 290
    NOTIFYLIST = 291
    NOTIFYGET_MESSAGE = 292
    NOTIFYGET_NOTIFY = 293
    SENDMESSAGE_SUCCESSFUL = 294
    USER_ID = 295
    CALENDAR = 297
    PONG = 300
    AUTHPONG = 301
    NO_SUCH_RESOURCE = 305
    API_PASSWORD_NOT_DEFINED = 309
    FILE_ALREADY_IN_MYLIST = 310
    MYLIST_ENTRY_EDITED = 311
    MULTIPLE_MYLIST_ENTRIES = 312
    WATCHED = 313
    SIZE_HASH_EXISTS = 314
    INVALID_DATA = 315
    STREAMNOID_USED = 316
    EXPORT_NO_SUCH_TEMPLATE = 317
    EXPORT_ALREADY_IN_QUEUE = 318
    EXPORT_NO_EXPORT_QUEUED_OR_IS_PROCESSING = 319
    NO_SUCH_FILE = 320
    NO_SUCH_ENTRY = 321
    MULTIPLE_FILES_FOUND = 322
    NO_SUCH_WISHLIST = 323
    NO_SUCH_NOTIFICATION = 324
    NO_GROUPS_FOUND = 325
    NO_SUCH_ANIME = 330
    NO_SUCH_DESCRIPTION = 333
    NO_SUCH_REVIEW = 334
    NO_SUCH_CHARACTER = 335
    NO_SUCH_SONG = 336
    NO_SUCH_ANIMETAG = 337
    NO_SUCH_CHARACTERTAG = 338
    NO_SUCH_EPISODE = 340
    NO_SUCH_UPDATES = 343
    NO_SUCH_TITLES = 344
    NO_SUCH_CREATOR = 345
    NO_SUCH_GROUP = 350
    NO_SUCH_CATEGORY = 351
    BUDDY_ALREADY_ADDED = 355
    NO_SUCH_BUDDY = 356
    BUDDY_ALREADY_ACCEPTED = 357
    BUDDY_ALREADY_DENIED = 358
    NO_SUCH_VOTE = 360
    INVALID_VOTE_TYPE = 361
    INVALID_VOTE_VALUE = 362
    PERMVOTE_NOT_ALLOWED = 363
    ALREADY_PERMVOTED = 364
    HOT_ANIME_EMPTY = 365
    RANDOM_RECOMMENDATION_EMPTY = 366
    RANDOM_SIMILAR_EMPTY = 367
    NOTIFICATION_DISABLED = 370
    NO_SUCH_ENTRY_MESSAGE = 381
    NO_SUCH_ENTRY_NOTIFICATION = 382
    NO_SUCH_MESSAGE = 392
    NO_SUCH_NOTIFY = 393
    NO_SUCH_USER = 394
    CALENDAR_EMPTY = 397
    NO_CHANGES = 399
    NOT_LOGGED_IN = 403
    NO_SUCH_MYLIST_FILE = 410
    NO_SUCH_MYLIST_ENTRY = 411
    MYLIST_UNAVAILABLE = 412
    LOGIN_FAILED = 500
    LOGIN_FIRST = 501
    ACCESS_DENIED = 502
    CLIENT_VERSION_OUTDATED = 503
    CLIENT_BANNED = 504
    ILLEGAL_INPUT_OR_ACCESS_DENIED = 505
    INVALID_SESSION = 506
    NO_SUCH_ENCRYPTION_TYPE = 509
    ENCODING_NOT_SUPPORTED = 519
    BANNED = 555
    UNKNOWN_COMMAND = 598
    INTERNAL_SERVER_ERROR = 600
    ANIDB_OUT_OF_SERVICE = 601
    SERVER_BUSY = 602
    NO_DATA = 603
    TIMEOUT = 604
    API_VIOLATION = 666
    PUSHACK_CONFIRMED = 701
    NO_SUCH_PACKET_PENDING = 702
    VERSION = 998

    def __str__(self) -> str:
        return str(self.name).replace("_", " ").title()


@dataclass
class AniDBResponse:
    """AniDB response dataclass"""
    return_code: AniDBResponseCode
    """AniDB response code"""
    return_string: str
    """AniDB response string"""
    tag: str | None = None
    """AniDB response tag"""
    additional_return_string: str | None = None
    """AniDB additional response string, usually session key"""
    data: list[str | list[str]] = []
    """AniDB response data"""

    @staticmethod
    def from_string(data: str) -> "AniDBResponse":
        """
        Convert a string to a dataclass

        :param data: String to convert
        :type data: str
        :return: AniDB response dataclass
        :rtype: AniDBResponse
        """
        procdat = data.split("\n")
        header = procdat[0].split(" ")
        retcode = 0
        retstring = ""
        tag = None
        additional_return_string = None

        if header[0].isdigit():
            retcode = int(header[0])
            retstring = " ".join(header[1:])
        elif header[1].isdigit():
            retcode = int(header[1])
            tag = header[0]
            if len(header) > 2 and header[2].isalnum() and (len(header[2]) >= 4 and len(header[2]) <= 8):
                additional_return_string = header[2]
                retstring = " ".join(header[3:])
            else:
                retstring = " ".join(header[2:])
        else:
            raise ValueError(f"Invalid response header {header}")

        retdatsplit: list[str | list[str]] = []

        if len(procdat) > 1:
            retdat = "`n".join(procdat[1:])
            if "`n" in retdat:
                retdat = retdat.split("`n")
            retdatsplit = []
            for i in range(len(retdat)):
                if "|" in retdat[i]:
                    retdatsplit.append(retdat[i].split("|"))
        else:
            retdatsplit = []

        return AniDBResponse(
            AniDBResponseCode(retcode),
            retstring,
            tag,
            additional_return_string,
            retdatsplit
        )


@dataclass
class AniDBAuth:
    """AniDB authentication dataclass"""
    user: str
    """AniDB username"""
    passwd: str
    """AniDB password"""
    protover: int
    """AniDB protocol version"""
    client: str
    """AniDB client"""
    clientver: int
    """AniDB client version"""
    enc: Literal["ISO8859_1", "ISO8859_2", "ISO8859_4", "ISO8859_5",
                 "ISO8859_7", "ISO8859_8", "ISO8859_9", "ISO8859_15", "KOI8_R",
                 "ASCII", "UTF8", "UTF-16", "UnicodeBigUnmarked",
                 "UnicodeLittleUnmarked", "Cp1250", "Cp1251", "Cp1252", "Cp1253",
                 "Cp1254", "Cp1257", "UnicodeBig", "UnicodeLittle"] | None = "UTF8"
    """AniDB encoding"""
    nat: bool = False
    """AniDB network address translation"""
    comp: bool = False
    """AniDB compression"""
    mtu: int | None = None
    """AniDB maximum transmission unit"""
    imgserver: bool = False
    """AniDB image server"""

    # validate the dataclass
    def __post_init__(self):
        if self.mtu and (self.mtu < 400 or self.mtu > 1400):
            raise AniDBInvalidType("MTU must be between 400 and 1400")

    @property
    def params(self) -> str:
        """
        Convert the dataclass to a string

        :return: String params
        :rtype: str
        """
        final_dict = self.__dict__
        # replace passwd to pass
        final_dict["pass"] = final_dict.pop("passwd")
        return convert_to_params(final_dict)
