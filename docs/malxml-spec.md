<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- omit in toc -->
# MyAnimeList XML Unofficial Specification

## Introduction

The following document is an unofficial attempt to define what the "MAL standard"
consists of. Between the various anime list sites, the standard for exports that
has emerged is the one in use by MAL. However, they do not officially document
how their standard works, and neither is there a publicly available unofficial
documentation. So for the purposes of this project, this document is an
unofficial attempt at defining what the "MAL standard" consists of.

## Guideline to Read Element/Tag

The following guideline is used to read the elements and tags in this document:

* **Type** &mdash; The type of the element or tag
* **Required?** &mdash; Whether the element or tag is required or not
* **Default** &mdash; The default value of the element or tag. In enum, it is the
  default value if not specified
* **Description** &mdash; The description of the element or tag

> [!NOTE]
>
> Although some tags/elements are marked as required, it is a best practice to
> include all elements/tags to avoid any issues.

<!-- omit in toc -->
## Table of Contents

* [Introduction](#introduction)
* [Guideline to Read Element/Tag](#guideline-to-read-elementtag)
* [Export Format](#export-format)
* [XML Header](#xml-header)
* [XML Root Element](#xml-root-element)
* [Generic Types](#generic-types)
  * [String](#string)
  * [Text](#text)
  * [Integer](#integer)
  * [Float](#float)
  * [Array](#array)
  * [Null/None](#nullnone)
  * [Boolean](#boolean)
  * [Date](#date)
  * [Enumerations](#enumerations)
    * [Media Type](#media-type)
    * [Update on Import](#update-on-import)
    * [Replay Priority](#replay-priority)
    * [Title Priority](#title-priority)
    * [Social Network Services (SNS) Share](#social-network-services-sns-share)
    * [Anime List Status](#anime-list-status)
    * [Anime Release Type](#anime-release-type)
    * [Anime Storages](#anime-storages)
    * [Manga List Status](#manga-list-status)
    * [Manga Storages](#manga-storages)
* [Elements](#elements)
  * [`<myinfo>`](#myinfo)
  * [`<anime>`](#anime)
  * [`<manga>`](#manga)
* [Expected Output](#expected-output)

## Export Format

While MyAnimeList and other trackers allows or requires to import with bare XML,
MyAnimeList specifically exports in a gzipped XML format.

An example of the file name as follow:

```plaintext
{media_type}list_{epoch}_{user_id}.xml.gz
```

Where:

| Handlebar      | Example Value | Description          |
| -------------- | ------------- | -------------------- |
| `{media_type}` | `anime`       | Media type           |
| `{epoch}`      | `1612345678`  | Unix epoch timestamp |
| `{user_id}`    | `123456`      | User ID              |

## XML Header

MyAnimeList XML exports uses following configuration for the XML header:

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

## XML Root Element

The root element of the XML file is `myanimelist`.

```xml
<myanimelist>
  <!-- ... -->
</myanimelist>
```

**Required** elements:

| Order | Element                                    | Description      |
| ----- | ------------------------------------------ | ---------------- |
| 1     | [`<myinfo>`](#myinfo)                      | User information |
| 2..n  | [`<anime>`](#anime) \| [`<manga>`](#manga) | Media entry      |
> [!CAUTION]
>
> The XML file only contains either `anime` or `manga` elements, not both.

## Generic Types

### String

Strings are represented as plain text.

```xml
<field>Some text</field>
```

### Text

Text are represented as plain string within `CDATA` tag.

```xml
<field><![CDATA[Some text]]></field>
```

> [!WARNING]
>
> [String][str] and [Text][txt] are different. Text is used for fields
> that may contain special characters that may break the XML structure.

### Integer

Integer values are represented as a [string][str] of digits.

```xml
<field>123</field>
```

### Float

Float values are represented as a [string][str] of digits with a decimal point.

```xml
<field>123.45</field>
```

### Array

Unlike other variant of XML, MyAnimeList XML rather uses comma-separated values
in [Text][txt] format.

```xml
<field><![CDATA[Value 1, Value 2, Value 3]]></field>
```

> [!NOTE]
>
> It is advised to split the values by comma and trim the whitespace to avoid
> any issues.

### Null/None

In case a field is empty or unknown, unless [specified otherwise][date], an
empty string is used.

```xml
<field></field>
```

### Boolean

*well, this is a bit tricky...*

Depending on media type, boolean values are represented as either `1` or `0`...
or even `YES` and `NO`.

| Value   | Anime | Manga |
| ------- | ----- | ----- |
| `false` | `0`   | `NO`  |
| `true`  | `1`   | `YES` |

```xml
<anime>
  <my_rewatching>0</my_rewatching>
</anime>
```

```xml
<manga>
  <my_rereading>NO</my_rereading>
</manga>
```

We're still not sure why they're different, but it's how it is.

### Date

The dates used in the document are formatted to follow `YYYY-MM-DD`. In case a
date is unset or isn't known, `0000-00-00` is used.

```xml
<my_start_date>2021-01-01</my_start_date>
<my_finish_date>0000-00-00</my_finish_date>
```

### Enumerations

Enums are represented as a [string](#string).

#### Media Type

Enums of a set of strings that represent the type of media

| Value | Media Type |
| ----- | ---------- |
| `1`   | Anime      |
| `2`   | Manga      |

```xml
<user_export_type>1</user_export_type>
```

#### Update on Import

Enums of a set of strings that represent the type of update on import

| Value | Description                    |
| ----- | ------------------------------ |
| `0`   | Do not overwrite existing data |
| `1`   | Overwrite existing data        |

```xml
<update_on_import>1</update_on_import>
```

#### Replay Priority

Enums of a set of  that represent the priority of rewatching or re-reading

| Value       | Description        |
| ----------- | ------------------ |
| `Very Low`  | Very low priority  |
| `Low`       | Low priority       |
| `Medium`    | Medium priority    |
| `High`      | High priority      |
| `Very High` | Very high priority |

```xml
<my_rewatch_value>Medium</my_rewatch_value>
```

#### Title Priority

Enums of a set of strings that represent the priority of the title to be consumed

| Value    | Default? | Description     |
| -------- | -------- | --------------- |
| `Low`    | Yes      | Low priority    |
| `Medium` |          | Medium priority |
| `High`   |          | High priority   |

```xml
<my_priority>High</my_priority>
```

#### Social Network Services (SNS) Share

Enums of a set of strings that represent if MyAnimeList is allowed to share the
entry updates to the social network services

| Value            | Default? | Description                        |
| ---------------- | -------- | ---------------------------------- |
| `default`        | Yes      | Use the default setting            |
| `allow`          |          | Allow sharing without confirmation |
| `ask_every_time` |          | Ask for confirmation every time    |
| `deny`           |          | Deny sharing                       |

```xml
<my_sns>allow</my_sns>
```

#### Anime List Status

Enums of a set of strings that represent the status of the anime in the list

| Value           | Default? | Description        |
| --------------- | -------- | ------------------ |
| `Watching`      |          | Currently watching |
| `Plan to Watch` | Yes      | Plan to watch      |
| `Completed`     |          | Completed watching |
| `Dropped`       |          | Dropped watching   |
| `On-Hold`       |          | Paused watching    |

```xml
<my_status>Watching</my_status>
```

#### Anime Release Type

Enums of a set of strings that represent the type of release of the anime

| Value        | Default? | Description              |
| ------------ | -------- | ------------------------ |
| `CM`         |          | Commercial               |
| `Movie`      |          | heatrical movie          |
| `Music`      |          | Music video              |
| `ONA`        |          | Original net animation   |
| `OVA`        |          | Original video animation |
| `PV`         |          | Promotional video        |
| `Special`    |          | Special episode          |
| `TV Special` |          | Television special       |
| `TV`         |          | Television series        |
| `Unknown`    | Yes      | Unknown release type     |

```xml
<series_type>TV</series_type>
```

#### Anime Storages

Enums of a set of strings that represent the type of storage used to store the anime

| Value         | Description              |
| ------------- | ------------------------ |
| `Blu-ray`     | Blu-ray disc             |
| `DVD / CD`    | DVD or CD                |
| `Hard Drive`  | Hard drive               |
| `External HD` | External hard drive      |
| `NAS`         | Network-attached storage |
| `Retail DVD`  | Retail DVD               |
| `VHS`         | VHS tape                 |

```xml
<my_storage>Blu-ray</my_storage>
```

#### Manga List Status

Enums of a set of strings that represent the status of the manga in the list

| Value          | Default? | Description       |
| -------------- | -------- | ----------------- |
| `Reading`      |          | Currently reading |
| `Plan to Read` | Yes      | Plan to read      |
| `Completed`    |          | Completed reading |
| `Dropped`      |          | Dropped reading   |
| `On-Hold`      |          | Paused reading    |

```xml
<my_status>Reading</my_status>
```

#### Manga Storages

Enums of a set of strings that represent the type of storage used to store the manga

| Value          | Description              |
| -------------- | ------------------------ |
| `Blu-ray`      | Blu-ray disc             |
| `DVD / CD`     | DVD or CD                |
| `External HD`  | External hard drive      |
| `Hard Drive`   | Hard drive               |
| `Magazine`     | Magazine                 |
| `NAS`          | Network-attached storage |
| `Retail Manga` | Retail manga             |

```xml
<my_storage>Magazine</my_storage>
```

## Elements

### `<myinfo>`

User information. Depending on media type, the following tags were used:

| Tag                         | Type                      | Required? | Description                                                                          |
| --------------------------- | ------------------------- | --------- | ------------------------------------------------------------------------------------ |
| `<user_export_type>`        | [Media Type](#media-type) | Yes       | Export type                                                                          |
| `<user_id>`                 | [int]                     |           | User ID                                                                              |
| `<user_name>`               | [str]                     |           | User name                                                                            |
| `<user_total_{media_type}>` | [int]                     |           | Total number of media in the list, where `{media_type}` is either `anime` or `manga` |
| `<user_total_completed>`    | [int]                     |           | Total number of media in completed status                                            |
| `<user_total_onhold>`       | [int]                     |           | Total number of media in on-hold status                                              |
| `<user_total_dropped>`      | [int]                     |           | Total number of media in dropped status                                              |

Exclusive to anime exports:

| Tag                        | Type  | Required? | Description                                   |
| -------------------------- | ----- | --------- | --------------------------------------------- |
| `<user_total_watching>`    | [int] |           | Total number of media in watching status      |
| `<user_total_plantowatch>` | [int] |           | Total number of media in plan to watch status |

Exclusive to manga exports:

| Tag                       | Type  | Required? | Description                                  |
| ------------------------- | ----- | --------- | -------------------------------------------- |
| `<user_total_reading>`    | [int] |           | Total number of media in reading status      |
| `<user_total_plantoread>` | [int] |           | Total number of media in plan to read status |

```xml
<!-- Anime -->
<myinfo>
  <user_id>123456</user_id>
  <user_name>username</user_name>
  <user_export_type>1</user_export_type>
  <user_total_anime>123</user_total_anime>
  <user_total_watching>12</user_total_watching>
  <user_total_completed>34</user_total_completed>
  <user_total_onhold>56</user_total_onhold>
  <user_total_dropped>78</user_total_dropped>
  <user_total_plantowatch>90</user_total_plantowatch>
</myinfo>

<!-- Manga -->
<myinfo>
  <user_id>123456</user_id>
  <user_name>username</user_name>
  <user_export_type>2</user_export_type>
  <user_total_manga>123</user_total_manga>
  <user_total_reading>12</user_total_reading>
  <user_total_completed>34</user_total_completed>
  <user_total_onhold>56</user_total_onhold>
  <user_total_dropped>78</user_total_dropped>
  <user_total_plantoread>90</user_total_plantoread>
</myinfo>
```

### `<anime>`

Anime entry. The following tags were used:

> [!NOTE]
>
> * The tags marked with *Legacy* are artifacts from AniDB or are unused by MAL.
> * Required tag means that most importer from other sites will require these tags.
>   * We recommend to include all tags to avoid any issues.

| Tag                     | Type                                | Required? | Default         | Description                                                                    |
| ----------------------- | ----------------------------------- | --------- | --------------- | ------------------------------------------------------------------------------ |
| `<series_animedb_id>`   | [int]                               | Yes       |                 | MyAnimeList ID of the anime                                                    |
| `<series_title>`        | [txt]                               |           |                 | Title of the anime                                                             |
| `<series_type>`         | [Release Type][art]                 |           | `Unknown`       | Type of the anime                                                              |
| `<series_episodes>`     | [int]                               |           | `0`             | Total number of episodes                                                       |
| `<my_id>`               | [int], *Legacy*                     |           | `0`             | Sequential global number given to each entry when added to the user's list[^1] |
| `<my_watched_episodes>` | [int]                               | Yes       | `0`             | Number of episodes watched                                                     |
| `<my_start_date>`       | [date]                              |           | `0000-00-00`    | Date the anime was started                                                     |
| `<my_finish_date>`      | [date]                              |           | `0000-00-00`    | Date the anime was finished                                                    |
| `<my_rated>`            | [null], *Legacy*                    |           |                 | Purpose unknown, unused, left empty                                            |
| `<my_score>`            | [int]                               | Yes       |                 | Score given to the anime                                                       |
| `<my_storage>`          | [Anime Storages][ast] \| [null]     |           |                 | Type of storage used to store the anime                                        |
| `<my_storage_value>`    | [float], *Legacy*                   |           | `0.00`          | Drive space in GB or the number of disks; artifacts from AniDB                 |
| `<my_status>`           | [Anime List Status][als]            | Yes       | `Plan to Watch` | Status of the anime                                                            |
| `<my_comments>`         | [txt]                               |           |                 | Comments on the anime                                                          |
| `<my_times_watched>`    | [int]                               | Yes       | `0`             | Number of times re-watched                                                     |
| `<my_rewatch_value>`    | [Replay Priority][replay] \| [null] |           |                 | Priority of rewatching                                                         |
| `<my_priority>`         | [Title Priority][title]             |           | `Low`           | Priority of the anime                                                          |
| `<my_tags>`             | [arr]                               |           |                 | Tags separated by commas, can include spaces                                   |
| `<my_rewatching>`       | [bool]                              | Yes       | `0`             | `1` if anime is being rewatched, `0` otherwise                                 |
| `<my_rewatching_ep>`    | [int], *Legacy*                     |           | `0`             | Episode in the rewatch, MAL leaves it at 0[^2]                                 |
| `<my_discuss>`          | [bool]                              |           | `0`             | `1` if the anime is open for discussion, `0` otherwise                         |
| `<my_sns>`              | [SNS Share][sns]                    |           | `default`       | Share the entry updates to the social network services                         |
| `<update_on_import>`    | [Update on Import][uoi]             | Yes       | `0`             | Overwrite existing entry on import                                             |

```xml
<anime>
  <series_animedb_id>12345</series_animedb_id>
  <series_title><![CDATA[Title]]></series_title>
  <series_type>TV</series_type>
  <series_episodes>12</series_episodes>
  <my_id>0</my_id>
  <my_watched_episodes>12</my_watched_episodes>
  <my_start_date>2021-01-01</my_start_date>
  <my_finish_date>0000-00-00</my_finish_date>
  <my_rated></my_rated>
  <my_score>10</my_score>
  <my_storage></my_storage>
  <my_storage_value>0.00</my_storage_value>
  <my_status>Watching</my_status>
  <my_comments><![CDATA[Comments]]></my_comments>
  <my_times_watched>1</my_times_watched>
  <my_rewatch_value></my_rewatch_value>
  <my_priority>Low</my_priority>
  <my_tags><![CDATA[Tag 1, Tag 2, Tag 3]]></my_tags>
  <my_rewatching>0</my_rewatching>
  <my_rewatching_ep>0</my_rewatching_ep>
  <my_discuss>0</my_discuss>
  <my_sns>default</my_sns>
  <update_on_import>0</update_on_import>
</anime>
```

### `<manga>`

Manga entry. The following tags were used:

| Tag                  | Type                                | Required? | Default        | Description                                                                    |
| -------------------- | ----------------------------------- | --------- | -------------- | ------------------------------------------------------------------------------ |
| `<manga_mangadb_id>` | [int]                               | Yes       |                | MyAnimeList ID of the manga                                                    |
| `<manga_title>`      | [txt]                               |           |                | Title of the manga                                                             |
| `<manga_volumes>`    | [int]                               |           | `0`            | Total number of volumes                                                        |
| `<manga_chapters>`   | [int]                               |           | `0`            | Total number of chapters                                                       |
| `<my_id>`            | [int]                               |           | `0`            | Sequential global number given to each entry when added to the user's list[^1] |
| `<my_read_volumes>`  | [int]                               | Yes       | `0`            | Number of volumes read                                                         |
| `<my_read_chapters>` | [int]                               | Yes       | `0`            | Number of chapters read                                                        |
| `<my_start_date>`    | [date]                              |           | `0000-00-00`   | Date the manga was started                                                     |
| `<my_finish_date>`   | [date]                              |           | `0000-00-00`   | Date the manga was finished                                                    |
| `<my_score>`         | [int]                               | Yes       |                | Score given to the manga                                                       |
| `<my_status>`        | [Manga List Status][mls]            | Yes       | `Plan to Read` | Status of the manga                                                            |
| `<my_comments>`      | [txt]                               |           |                | Comments on the manga                                                          |
| `<my_times_read>`    | [int]                               | Yes       | `0`            | Number of times re-read                                                        |
| `<my_tags>`          | [arr]                               |           |                | Tags separated by commas, can include spaces                                   |
| `<my_priority>`      | [Title Priority][title]             |           | `Low`          | Priority of the manga                                                          |
| `<my_reread_value>`  | [Replay Priority][replay] \| [null] |           |                | Priority of re-reading                                                         |
| `<my_rereading>`     | [bool]                              | Yes       | `NO`           | `YES` if manga is being re-read, `NO` otherwise                                |
| `<my_discuss>`       | [bool]                              |           | `YES`          | `YES` if the manga is open for discussion, `NO` otherwise                      |
| `<my_sns>`           | [SNS Share][sns]                    |           | `default`      | Share the entry updates to the social network services                         |
| `<update_on_import>` | [Update on Import][uoi]             | Yes       | `0`            | Overwrite existing entry on import                                             |

```xml
<manga>
  <manga_mangadb_id>12345</manga_mangadb_id>
  <manga_title><![CDATA[Title]]></manga_title>
  <manga_volumes>12</manga_volumes>
  <manga_chapters>123</manga_chapters>
  <my_id>0</my_id>
  <my_read_volumes>12</my_read_volumes>
  <my_read_chapters>123</my_read_chapters>
  <my_start_date>2021-01-01</my_start_date>
  <my_finish_date>0000-00-00</my_finish_date>
  <my_score>10</my_score>
  <my_status>Reading</my_status>
  <my_comments><![CDATA[Comments]]></my_comments>
  <my_times_read>1</my_times_read>
  <my_tags><![CDATA[Tag 1, Tag 2, Tag 3]]></my_tags>
  <my_priority>Low</my_priority>
  <my_reread_value></my_reread_value>
  <my_rereading>NO</my_rereading>
  <my_discuss>YES</my_discuss>
  <my_sns>default</my_sns>
  <update_on_import>0</update_on_import>
</manga>
```

## Expected Output

The expected output of the XML file is as follows:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<myanimelist>
  <myinfo>
    <user_id>123456</user_id>
    <user_name>username</user_name>
    <user_export_type>1</user_export_type>
    <user_total_anime>123</user_total_anime>
    <user_total_watching>12</user_total_watching>
    <user_total_completed>34</user_total_completed>
    <user_total_onhold>56</user_total_onhold>
    <user_total_dropped>78</user_total_dropped>
    <user_total_plantowatch>90</user_total_plantowatch>
  </myinfo>
  <anime>
    <series_animedb_id>12345</series_animedb_id>
    <series_title><![CDATA[Title]]></series_title>
    <series_type>TV</series_type>
    <series_episodes>12</series_episodes>
    <my_id>0</my_id>
    <my_watched_episodes>12</my_watched_episodes>
    <my_start_date>2021-01-01</my_start_date>
    <my_finish_date>0000-00-00</my_finish_date>
    <my_rated></my_rated>
    <my_score>10</my_score>
    <my_storage></my_storage>
    <my_storage_value>0.00</my_storage_value>
    <my_status>Watching</my_status>
    <my_comments><![CDATA[Comments]]></my_comments>
    <my_times_watched>1</my_times_watched>
    <my_rewatch_value></my_rewatch_value>
    <my_priority>Low</my_priority>
    <my_tags><![CDATA[Tag 1, Tag 2, Tag 3]]></my_tags>
    <my_rewatching>0</my_rewatching>
    <my_rewatching_ep>0</my_rewatching_ep>
    <my_discuss>0</my_discuss>
    <my_sns>default</my_sns>
    <update_on_import>0</update_on_import>
  </anime>
</myanimelist>
```

<!--------------------------->

[str]: #string
[int]: #integer
[txt]: #text
[null]: #nullnone
[bool]: #boolean
[date]: #date
[float]: #float
[arr]: #array

[als]: #anime-list-status
[art]: #anime-release-type
[ast]: #anime-storages
[mls]: #manga-list-status
[replay]: #replay-priority
[sns]: #social-network-services-sns-share
[title]: #title-priority
[uoi]: #update-on-import

<!-- markdownlint-disable MD034 -->
[^1]: https://myanimelist.net/forum/?goto=post&topicid=267660&id=9784885
[^2]: https://myanimelist.net/forum/?goto=post&topicid=294806&id=10649513
