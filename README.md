<!-- markdownlint-disable MD028 MD027 -->

# Bokusu

Easily backups your media lists from 15 sites and counting with async
compability in mind.

> [!WARNING]
>
> This project is not available to install yet, as it is still in development.
> You can help by contributing to the project so that it can be released
> sooner.

## Supported Sites

> [!IMPORTANT]
>
> The following sites has been thoroughly tested and supported from previous
> project, [`animeManga-autoBackup`][amab]. The following sites are guaranteed
> to be implemented and supported in the future.

<!-- markdownlint-disable MD033 -->

<table>
  <tr>
    <td align="center"><a href="https://anilist.co"><img src="images/anilist.png" alt="AniList" width="100"></a></td>
    <td align="center"><a href="https://anime-planet.com"><img src="images/animeplanet.png" alt="Anime-Planet" width="100"></a></td>
    <td align="center"><a href="https://annict.com"><img src="https://github.com/annict/annict-logo/blob/master/annict-logo-ver3.png?raw=true" alt="Annict" width="100"></a></td>
    <td align="center"><a href="https://bgm.tv"><img src="images/bangumi.png" alt="Bangumi" width="100"></a></td>
    <td align="center"><a href="https://kaize.io"><img src="images/kaize.png" alt="Kaize" width="100"></a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://anilist.co">AniList</a><br>🍥📔 / 🔐⌛</td>
    <td align="center"><a href="https://anime-planet.com">Anime-Planet</a><br>🍥📔 / 👥📸</td>
    <td align="center"><a href="https://annict.com">Annict</a><br>🍥 / 🔐📸⌛🌐</td>
    <td align="center"><a href="https://bgm.tv">Bangumi</a><br>🍥📔🎮📺 / 🔐📸🌐</td>
    <td align="center"><a href="https://kaize.io">Kaize</a><br>🍥📔 / 👥📸🧼</td>
  </tr>
  <tr>
    <td align="center"><a href="https://kitsu.app"><img src="images/kitsu.png" alt="Kitsu" width="100"></a></td>
    <td align="center"><a href="https://mangadex.org"><img src="images/mangadex.png" alt="MangaDex" width="100"></a></td>
    <td align="center"><a href="https://mangaupdates.com"><img src="https://www.mangaupdates.com/images/mascot.gif" alt="MangaUpdates" width="100"></a></td>
    <td align="center"><a href="https://myanimelist.net"><img src="images/myanimelist.png" alt="MyAnimeList" width="100"></a></td>
    <td align="center"><a href="https://notify.moe"><img src="images/notifymoe.png" alt="notify.moe" width="100"></a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://kitsu.app">Kitsu</a><br>🍥📔 / 🔐📸</td>
    <td align="center"><a href="https://mangadex.org">MangaDex</a><br>📔 / 🔐</td>
    <td align="center"><a href="https://mangaupdates.com">MangaUpdates</a><br>📔 / 🔐📸</td>
    <td align="center"><a href="https://myanimelist.net">MyAnimeList</a><br>🍥📔 / 👥🔐📸</td>
    <td align="center"><a href="https://notify.moe">Notify</a><br>🍥 / 👥📸</td>
  </tr>
  <tr>
    <td align="center"><a href="https://otakotaku.com"><img src="images/otakotaku.png" alt="Otak Otaku" width="100"></a></td>
    <td align="center"><a href="https://shikimori.one"><img src="images/shikimori.jpg" alt="Shikimori" width="100"></a></td>
    <td align="center"><a href="https://simkl.com"><img src="images/simkl.png" alt="Simkl" width="100"></a></td>
    <td align="center"><a href="https://trakt.tv"><img src="images/trakt.png" alt="Trakt" width="100"></a></td>
    <td align="center"><a href="https://vndb.org"><img src="images/vndb.jpg" alt="VNDB" width="100"></a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://otakotaku.com">Otak Otaku</a><br>🍥 / 👥📸🌐</td>
    <td align="center"><a href="https://shikimori.one">Shikimori</a><br>🍥📔 / 🔐📸🌐</td>
    <td align="center"><a href="https://simkl.com">SIMKL</a><br>🍥📺🎬 / 🔐📸</td>
    <td align="center"><a href="https://trakt.tv">Trakt</a><br>📺🎬 / 🔐📸⌛</td>
    <td align="center"><a href="https://vndb.org">VNDB</a><br>🎮 / 🔐📸</td>
  </tr>
</table>

### Supported with Caveats

> [!NOTE]
>
> The following sites are supported, but with some caveats. Please read the
> notes for each site to understand the limitations.

For now, there are no sites that are supported with caveats, yay!

### Legends

<table>
  <tr>
    <th colspan="6" align="center">Supported Media Types</th>
  </tr>
  <tr>
    <th>🍥</th><td>Anime</td>
    <th>📔</th><td>Manga</td>
    <th>🎮</th><td>Games</td>
  </tr>
  <tr>
    <th>📺</th><td>TV Show</td>
    <th>🎬</th><td>Movie</td>
    <th>📖</th><td>Book</td>
  </tr>
  <tr>
    <th>🎵</th><td>Music</td>
    <th></th><td></td>
    <th></th><td></td>
  </tr>
  <tr>
    <th colspan="6" align="center">Site Information</th>
  </tr>
  <tr>
    <th>🔐</th><td>Requires login</td>
    <th>👥</th><td>List/entry must public</td>
    <th>🌐</th><td>Regionalized sites</td>
  </tr>
  <tr>
    <th>📸</th><td>Wayback Machine support</td>
    <th>⌛</th><td>Exports history log</td>
    <th>🧼</th><td>No Explicit Content</td>
  </tr>
  <tr>
    <th>📨</th><td>Have caveats</td>
    <th>🏃</th><td>Requires bypassing security screening/captcha</td>
    <th></th><td></td>
</table>
<!-- markdownlint-enable MD013 MD033 -->

### Planned for The Integrations

> [!NOTE]
>
> The following sites are planned to be integrated in the future, but not
> guaranteed to be implemented due some known issues or limitations.

* [ ] [aniDB](https://anidb.net) &mdash; 🍥 / 🔐📨\
  Due to limited UDP API commands, `bokusu` will only be able to send an
  export request and read your mail to check if the export is ready. You need
  to manually download the export file from the mail every 2 weeks.
* [ ] [aniSearch](https://anisearch.com) &mdash; 🍥📔📺🎬 / 👥🌐🏃
* [ ] [Doujinshi.info](https://doujinshi.info) &mdash; 📔 / 🔐📸
* [ ] [Goodreads](https://goodreads.com) &mdash; 📖 / 👥⌛📸
* [ ] [IMDb](https://imdb.com) &mdash; 📺🎬 / 👥📸🏃
* [ ] [Kinopoisk](https://kinopoisk.ru) &mdash; 📺🎬 / 👥🌐📸
* [ ] [Kinorium](https://en.kinorium.com) &mdash; 📺🎬 / 👥🌐📸
* [ ] [Kurozora](https://kurozora.app) (former Aozora) &mdash; 🍥📔🎮 / 🔐📸
* [ ] [Last.fm](https://last.fm) &mdash; 🎵 / 🔐⌛📸
* [ ] [ListenBrainz](https://listenbrainz.org) &mdash; 🎵 / 🔐⌛📸
* [ ] [LiveChart.me](https://livechart.me) &mdash; 🍥 / 🔐🏃
* [ ] [MyDramaList](https://mydramalist.com) &mdash; 📺🎬 / 👥📸
* [ ] [MyShows](https://en.myshows.me) &mdash; 📺🎬 / 👥🌐📸
* [ ] [Nautiljon](https://nautiljon.com) &mdash; 🍥📔📺🎬 / 👥🌐📸🏃
* [ ] [RAWG](https://rawg.io) &mdash; 🎮 / 👥
* [ ] [The Movie Database](https://themoviedb.org) &mdash; 📺🎬 / 📸

If you want to see a site that is not listed here, please open an issue and we'll
see what we can do.

### Export File Interoperability

Bokusu offers multiple export file formats to choose from, so you can
choose the one that is most suitable for your use case. In most cases, you
only need MAL-flavored XML format so you can import it to other sites that
support importing from MAL.

<!-- markdownlint-disable MD013 MD033 -->

|         Site |  XML  | MALXML | JSON  | RYMSF YAML[^1] |  CSV  | Plain Text |   Reimportable[^2]    |
| -----------: | :---: | :----: | :---: | :------------: | :---: | :--------: | :-------------------: |
|      AniList |       |   ✅    |   ✅   |       ✅        |       |   ✅[^3]    |   MALXML, JSON[^4]    |
| Anime-Planet |       |   ✅    |   ✅   |       ✅        |       |            |        MALXML         |
|       Annict |       | ⭕[^5]  |   ✅   |     ⭕[^5]      |       |   ✅[^3]    |                       |
|      Bangumi |       |        |   ✅   |       ✅        |       |            |                       |
|        Kaize |       | ✅[^6]  |   ✅   |       ✅        |       |            |        MALXML         |
|        Kitsu |       |   ✅    |   ✅   |       ✅        |       |            |        MALXML         |
|     MangaDex |       |   ✅    |   ✅   |       ✅        |       |            |                       |
| MangaUpdates |       |        |       |                |   ✅   |            |                       |
|  MyAnimeList |       |   ✅    |   ✅   |       ✅        |       |            |        MALXML         |
|       Notify |       |   ✅    |   ✅   |       ✅        |   ✅   |     ✅      |      MALXML[^7]       |
|   Otak Otaku |       |   ✅    |   ✅   |       ✅        |       |            |        MALXML         |
|    Shikimori |       |   ✅    |   ✅   |       ✅        |       |            |     MALXML, JSON      |
|        SIMKL |       |   ✅    |   ✅   |       ✅        |       |            | MALXML[^7], JSON, CSV |
|        Trakt |       |        |   ✅   |                |       |   ✅[^3]    |                       |
|         VNDB |   ✅   |        |   ✅   |                |       |            |                       |

<!-- markdownlint-enable MD013 MD033 -->

[^1]: [Ryuuganime Media Save File format][rymsf] is experimental standardized
      schema format for media list backup. While it is not supported by any
      sites yet, it does help Bokusu to be able to convert between
      different formats.
[^2]: The site allows you to reimport the exported file back to the site.
[^3]: Only user records will be exported as plain text for logging.
[^4]: AniList does not support reimporting JSON file natively, use Automail
      userscript to assist.
[^5]: Due to massive infrastructure differences between Annict with their
      "record" system and MyAnimeList/RYSMF simple tracking system, some data
      may be lost during the conversion process.
[^6]: Only Anime will be exported as MALXML due to Kaize and [AnimeAPI][aa] API
      limitations.
[^7]: To import from MALXML, you need to have either MyAnimeList, Kitsu, or
      AniList account connected to your account. Import XML file to one of those
      sites, then do a sync to target site.

## Requirements and Installations

Before you can use Bokusu, you need to install the following:

* Python 3.10 or higher, recommended to install 3.11 instead as it is the only
  version that is fully tested and supported.

We also recommend installing the following for better experience:

* [pipx](https://github.com/pypa/pipx) for installing Bokusu
  without polluting your system and easily upgrade or uninstall it.

After installing the above, you can install Bokusu by running the
following command:

```bash
pip install bokusu
```

> [!NOTE]
>
> * Replace `pip` with `pipx` if you mainly use `pipx` to install executables.
> * Depending on your system, you may need to use `pip3` instead of `pip`.
> * If `pip` is reported as not found, add `python3 -m` (or `python -m` in some
>  systems) before `pip` in the command above.

> [!IMPORTANT]
>
> If during installation you may encounter an error related to building the
> dependencies, you may need to install the following packages first:
>
> * Linux and macOS:
>   * `python3-dev` (or `python3-devel` in some systems, or omit `3` if the
>     system only has Python 3)
>   * `build-essential` (or `gcc` and `g++` in some systems)
> * Windows:
>   * [Visual Studio Build Tools](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019)
>     (or Visual Studio 2019 with C++ build tools)\
>     Installing above package may take a lot of space, so make sure you have
>     enough space in your system.
>   * [Microsoft Visual C++ Redistributable for Visual Studio 2019](https://visualstudio.microsoft.com/downloads/#microsoft-visual-c-redistributable-for-visual-studio-2019)

## Setup and Configuration

To use Bokusu, you need to configure it first. You can do so by running
the following command:

```bash
bokusu setup
```

This will ask you to enter your credentials for each site you want to backup,
and create a configuration file for you. The configuration file will be stored
in your user directory (`~/.bokusu`), and will be used by bokusu to
authenticate you when you run the backup command.

Follow the instructions on the screen to complete the setup, or visit the
[wiki](https://github.com/Animanga-Initiative/bokusu/wiki) for more
information.

Or, if you want to change your configuration, you can run the following command:

```bash
bokusu config --edit
```

## Usage

Bokusu is a command-line tool, so you need to run it in a terminal.

You can also call the program using `box` as an alias for `bokusu` if you want
to save some keystrokes... but it's not recommended if you have [Box](https://box.com)
(that one cloud storage service) CLI app installed in your system.

### Basic Usage

```bash
bokusu
# or, if you explicitly set an alias for bokusu
box
# or
python -m bokusu
```

This will show you the help message and the available commands.

## License

Bokusu is licensed under [GPL Affero v3.0 or later (AGPL-3.0+)](LICENSE)
due to heavy dependency of [AnimeAPI][aa] API for remapping IDs across sites.

We recommend you to use the program as-is and not integrating it to your other
open source project/suite, since it will force your project to be licensed under
AGPL-3.0+ as well unless the project is copylefted under GPL-3.0+ or compatible
GPL licenses.

We are not a lawyer, so please consult your lawyer to make sure you are not
violating the license.

[aa]: https://animeapi.my.id
[rymsf]: https://github.com/ryuuganime/mediaSaveFile
[amab]: https://github.com/Animanga-Initiative/animeManga-autoBackup
