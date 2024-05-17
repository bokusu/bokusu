from os import getenv
from platform import (
    architecture,
    platform,
    processor,
    python_build,
    python_implementation,
    python_version,
    system,
)
from re import sub
from sys import executable
from typing import Annotated

import typer as ty

app = ty.Typer(no_args_is_help=True)


def ci(text: str, ansi: str) -> str:
    return f"\033[1;{ansi}m{text}\033[0m"


@app.command(
    name="about",
    help="Show the about information of the application",
)
def cli_about(
    hide_logo: Annotated[
        bool,
        ty.Option(
            "--hide-logo",
            help="Hide the logo",
        ),
    ] = False,
    monochrome: Annotated[
        bool,
        ty.Option(
            "--monochrome",
            help="Use monochrome logo",
        ),
    ] = False,
):
    from bokusu.core.commons import read_resource
    from bokusu.core.const import __version__

    user = getenv("USERPROFILE") or getenv("HOME") or ""
    exe = executable.replace(user, "~")

    infos = [
        f"Bokusu v{__version__}",
        "A CLI to assist on exporting your media lists.",
        "",
        "Licensed under the AGPL-3.0 License.",
        "Homepage: https://github.com/bokusu/bokusu",
        "",
        f"Python {python_version()} ({python_implementation()} {python_build()})",
        f"{exe}",
        "",
        f"Platform: {platform()}",
        f"Processor: {processor()}",
        f"Architecture: {architecture()[0]}",
    ]
    # if platform is windows, remove ansii color
    catinabox = read_resource("assets", "logo.ans")
    if system() == "Windows" or monochrome:
        catinabox = sub(r"\033\[[0-9;]*m", "", catinabox)
    max_info = max(len(info) for info in infos)
    if not hide_logo:
        lines = catinabox.split("\n")
        # TODO: Bro, this is a mess, refactor this :'D
        for i, info in enumerate(infos, 1):
            border = "│" if i not in [1, len(infos) + 1] else "╭─" if i == 1 else "╰─"
            end_border = "│" if i != len(infos) + 1 else "╯"
            # add end border after calculating the length of the info
            if info == "":
                # change to dashes if the info is empty
                info = ci("─" * max_info, "37")
            if i != 1:
                info += " " * (max_info - len(info)) + " " + end_border
            lines[i] += "  " + border + " " + info  # type: ignore
            if i == 1:
                lines[i] += " " + "─" * (max_info - len(info) - 1) + "╮"
            elif i == len(infos):
                lines[i + 1] += "  " + "╰" + "─" * (max_info + 2) + "╯"
        ty.echo("\n".join(lines))
    else:
        ty.echo("\n".join(infos))


# use grey color for aliases
@app.command(
    name="version",
    help=f"Show the version of the application. Aliases: {ci('ver', '34')}, {ci('v', '34')}",
)
@app.command(name="ver", hidden=True)
@app.command(name="v", hidden=True)
def version():
    from bokusu.core.const import __version__

    ty.echo(f"Bokusu v{__version__}")


if __name__ == "__main__":
    app()
