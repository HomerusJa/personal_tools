from pathlib import Path

import click

from tools.shared.path_utils import should_exclude


def count_lines(file_path: Path) -> int:
    try:
        return sum(1 for _ in file_path.open())
    except Exception as e:
        print(f"Error reading file at '{file_path}': {str(e)}")
        return 0


@click.command()
@click.argument("input_dir", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--exclude", "-e", multiple=True, help="List of directory names to exclude"
)
def cli(input_dir: Path, exclude: list[str]):
    """Count the lines of code a folder."""
    line_count = 0
    for file_path in input_dir.rglob("*"):
        if file_path.is_file() and not should_exclude(file_path, exclude):
            line_count += count_lines(file_path)
    click.echo(f"Total line count: {line_count}")


if __name__ == "__main__":
    # Make the tool executable on its own
    cli()
