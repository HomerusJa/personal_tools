from pathlib import Path

import click

# prefix components:
space = "    "
branch = "│   "
# pointers:
tee = "├── "
last = "└── "


def tree(dir_path: Path, exclude, prefix: str = ""):
    """A recursive generator, given a directory Path object
    will yield a visual tree structure line by line
    with each line prefixed by the same characters
    """
    contents = list(dir_path.iterdir())
    # contents each get pointers that are ├── with a final └── :
    pointers = [tee] * (len(contents) - 1) + [last]
    for pointer, path in zip(pointers, contents):
        if any(excluded in path.parts for excluded in exclude):
            continue
        yield prefix + pointer + path.name
        if path.is_dir():  # extend the prefix and recurse:
            extension = branch if pointer == tee else space
            # i.e. space because last, └── , above so no more |
            yield from tree(path, exclude, prefix=prefix + extension)


@click.command()
@click.argument("dir_path", type=click.Path(exists=True, file_okay=False))
@click.option(
    "--exclude", "-e", multiple=True, help="List of directory names to exclude"
)
def cli(dir_path, exclude):
    """Prints a visual tree structure of DIR_PATH"""
    path = Path(dir_path)
    click.echo(f"{path.name}")
    for line in tree(path, exclude):
        click.echo(line)


if __name__ == "__main__":
    cli()
