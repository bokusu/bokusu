# hikaru-aegis

Spiritual successor for [animeManga-autoBackup][amab] rewritten in Python, easily
backups your media lists from 15 sites and counting.

> [!WARNING]
>
> This project is not available to install yet, as it is still in development.
> You can help by contributing to the project so that it can be released
> sooner.

## Supported Sites

<!-- markdownlint-disable MD033 -->
<table>
  <tr>
    <td align="center"><a href="https://anilist.co"><img src="images/anilist.png" alt="AniList" width="100"></a></td>
    <td align="center"><a href="https://anime-planet.com"><img src="images/animeplanet.png" alt="Anime-Planet" width="100"></a></td>
    <td align="center"><a href="https://annict.com"><img src="https://github.com/annict/annict-logo/blob/master/annict-logo-ver3.png?raw=true" alt="Annict" width="100"></a></td>
    <td align="center"><a href="https://mangaupdates.com"><img src="https://www.mangaupdates.com/images/mascot.gif" alt="Baka-Updates Manga" width="100"></a></td>
    <td align="center"><a href="https://bgm.tv"><img src="images/bangumi.png" alt="Bangumi" width="100"></a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://anilist.co">AniList</a><br>🍥📔 / 🔐⌛</td>
    <td align="center"><a href="https://anime-planet.com">Anime-Planet</a><br>🍥📔 / 👥📸</td>
    <td align="center"><a href="https://annict.com">Annict</a><br>🍥 / 🔐📸⌛</td>
    <td align="center"><a href="https://mangaupdates.com">Baka-Updates Manga</a><br>📔 / 🔐📸</td>
    <td align="center"><a href="https://bgm.tv">Bangumi</a><br>🍥📔📺 / 🔐📸</td>
  </tr>
  <tr>
    <td align="center"><a href="https://kaize.io"><img src="images/kaize.png" alt="Kaize" width="100"></a></td>
    <td align="center"><a href="https://kitsu.io"><img src="images/kitsu.png" alt="Kitsu" width="100"></a></td>
    <td align="center"><a href="https://mangadex.org"><img src="images/mangadex.png" alt="MangaDex" width="100"></a></td>
    <td align="center"><a href="https://myanimelist.net"><img src="images/myanimelist.png" alt="MyAnimeList" width="100"></a></td>
    <td align="center"><a href="https://notify.moe"><img src="images/notifymoe.png" alt="notify.moe" width="100"></a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://kaize.io">Kaize</a><br>🍥📔 / 👥📸🧼</td>
    <td align="center"><a href="https://kitsu.io">Kitsu</a><br>🍥📔 / 🔐📸</td>
    <td align="center"><a href="https://mangadex.org">MangaDex</a><br>📔 / 🔐</td>
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
    <td align="center"><a href="https://otakotaku.com">Otak Otaku</a><br>🍥 / 👥📸</td>
    <td align="center"><a href="https://shikimori.one">Shikimori</a><br>🍥📔 / 🔐📸</td>
    <td align="center"><a href="https://simkl.com">Simkl</a><br>🍥📺🎬 / 🔐📸</td>
    <td align="center"><a href="https://trakt.tv">Trakt</a><br>📺🎬 / 🔐📸⌛</td>
    <td align="center"><a href="https://vndb.org">VNDB</a><br>🎮 / 🔐📸</td>
  </tr>
</table>

### Legends

<table>
  <tr>
    <th>🍥</th>
    <td>Anime</td>
    <th>📔</th>
    <td>Manga</td>
    <th>🎮</th>
    <td>Games</td>
    <th>📺</th>
    <td>TV Show</td>
    <th>🎬</th>
    <td>Movie</td>
  </tr>
  <tr>
    <th>👥</th>
    <td>List/entry must public</td>
    <th>🔐</th>
    <td>Requires login</td>
    <th>📸</th>
    <td>Wayback Machine support</td>
    <th>🧼</th>
    <td>No Explicit Content</td>
    <th>⌛</th>
    <td>Exports history log</td>
</table>
<!-- markdownlint-enable MD033 -->

### Planned for The Integration

> [!NOTE]
>
> The following sites are planned to be integrated in the future, but not
> guaranteed to be implemented due some known issues or limitations.

* [ ] [aniSearch](https://anisearch.com) &mdash; Anime / Manga
* [ ] [Goodreads](https://goodreads.com) &mdash; Books
* [ ] [IMDb](https://imdb.com) &mdash; TV Show / Movie
* [ ] [LiveChart.me](https://livechart.me) &mdash; Anime
* [ ] [MyDramaList](https://mydramalist.com) &mdash; TV Show / Movie
* [ ] [Nautiljon](https://nautiljon.com) &mdash; Anime / Manga
* [ ] [RAWG](https://rawg.io) &mdash; Games
* [ ] [The Movie Database](https://themoviedb.org) &mdash; TV Show / Movie

If you want to see a site that is not listed here, please open an issue and we'll
see what we can do.

### Export File Interoperability

Hikaru-Aegis offers multiple export file formats to choose from, so you can
choose the one that is most suitable for your use case. In most cases, you
only need MAL-flavored XML format so you can import it to other sites that
support importing from MAL.

|               Site | XML Plain | MALXML | JSON  | RYMSF YAML[^1] |  CSV  | Plain Text |     Reimportable[^2]      |
| -----------------: | :-------: | :----: | :---: | :------------: | :---: | :--------: | :-------------------: |
|            AniList |           |   ✅    |   ✅   |       ✅        |       |     ✅[^3]       |   MALXML, JSON[^4]    |
|       Anime-Planet |           |   ✅    |   ✅   |       ✅        |       |            |        MALXML         |
|             Annict |           | ⭕[^5]  |   ✅   |     ⭕[^5]      |       |   ✅[^3]    |                       |
| Baka-Updates Manga |           |        |       |                |   ✅   |            |                       |
|            Bangumi |           |        |   ✅   |       ✅        |       |            |                       |
|              Kaize |           | ✅[^6]  |   ✅   |       ✅        |       |            |        MALXML         |
|              Kitsu |           |   ✅    |   ✅   |       ✅        |       |            |        MALXML         |
|           MangaDex |           |   ✅    |   ✅   |       ✅        |       |            |                       |
|             Notify |           |   ✅    |   ✅   |       ✅        |   ✅   |     ✅      |      MALXML[^7]       |
|         Otak Otaku |           |   ✅    |   ✅   |                |       |            |        MALXML         |
|          Shikimori |           |   ✅    |   ✅   |       ✅        |       |            |     MALXML, JSON      |
|              SIMKL |           |   ✅    |   ✅   |       ✅        |       |            | MALXML[^7], JSON, CSV |
|              Trakt |           |        |   ✅   |                |       |   ✅[^3]    |                       |
|               VNDB |     ✅     |        |   ✅   |       ✅        |       |            |                       |

[^1]: [Ryuuganime Media Save File format][rymsf] is experimental standardized
      schema format for media list backup. While it is not supported by any
      sites yet, it does help `hikaru-aegis` to be able to convert between
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

Before you can use hikaru-aegis, you need to install the following:

* Python 3.10 or higher, recommended to install 3.11 instead as it is the only
  version that is fully tested and supported.
* Keyring daemon/service/agent available in your system, such as
  [gnome-keyring](https://wiki.gnome.org/Projects/GnomeKeyring) for Linux,
  [Keychain](https://www.funtoo.org/Keychain) for macOS, or
  [Windows Credential Manager](https://support.microsoft.com/en-us/windows/accessing-credential-manager-1b5c916a-6a16-889f-8581-fc16e8165ac0)
  for Windows. Required IF you want to use hikaru-aegis locally, otherwise
  you can use hikaru-aegis in a CI/CD environment (such as GitHub Actions) and
  provide the secrets as environment variables.

We also recommend installing the following for better experience:

* [pipx](https://github.com/pypa/pipx) for installing hikaru-aegis
  without polluting your system and easily upgrade or uninstall it.

After installing the above, you can install hikaru-aegis by running the
following command:

```bash
pip install hikaru-aegis
```

> [!NOTE]
>
> * Replace `pip` with `pipx` if you are using pipx.
> * Depending on your system, you may need to use `pip3` instead of `pip`.
> * If `pip` is reported as not found, add `python -m` (or `python3 -m` in some
>  systems) before `pip` in the command above.

## Usage

`hikaru-aegis` is a command-line tool, so you need to run it in a terminal.

### Basic Usage

```bash
hikaruaegis
```

This will show you the help message and the available commands.

[aa]: https://animeapi.my.id
[amab]: https://github.com/Animanga-Initiative/animeManga-autoBackup
[rymsf]: https://github.com/ryuuganime/mediaSaveFile
