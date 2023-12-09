# hikaru-aegis

Spiritual successor for animeManga-autoBackup rewritten in Python, easily
backups your media lists from 17 sites and counting.

## Requirements and Installations

Before you can use hikaru-aegis, you need to install the following:

* Python 3.10 or higher, recommended to install 3.11 instead as it is the only
  version that is fully tested and supported.
* [Keepass v2.47 or higher](https://keepass.info/download.html) for secrets
  management.
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
