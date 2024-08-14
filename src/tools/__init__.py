"""This is the main entry point for the tools package.

This script dynamically adds all the subcommands to the main command.

A subcommand is a standalone script in this directory. It should define a main click entry point called cli(). The
subcommand will pop up with the file name as its name.
"""

from pathlib import Path

import click


@click.group()
def cli():
    """All sorts of tools for personal use."""


def main():
    # Add all the subcommands to the main command dynamically
    for file_path in Path(__file__).parent.glob("*.py"):
        if file_path.stem != "__init__":
            command = getattr(
                __import__(f"tools.{file_path.stem}", fromlist=["cli"]), "cli"
            )
            cli.add_command(command, name=file_path.stem)

    cli()


if __name__ == "__main__":
    main()
