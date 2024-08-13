from pathlib import Path

import click


def read_file(file_path):
    try:
        return file_path.read_text(encoding="utf-8")
    except Exception as e:
        return f"Error reading file: {str(e)}"


def should_exclude(path, exclude_dirs):
    return any(excluded in path.parts for excluded in exclude_dirs)


@click.command()
@click.argument("input_dir")
@click.argument("output_file")
@click.option(
    "--exclude", "-e", multiple=True, help="List of directory names to exclude"
)
def cli(input_dir, output_file, exclude):
    """Converts a directory of files to a markdown file."""
    # TODO: Respect the .gitignore file
    input_dir = Path(input_dir)
    with Path(output_file).open("w", encoding="utf-8") as out_file:
        for file_path in input_dir.rglob("*"):
            if file_path.is_file() and not should_exclude(file_path, exclude):
                relative_path = file_path.relative_to(input_dir)

                out_file.write(f"## File: {relative_path}\n\n")
                out_file.write("```\n")  # TODO: Add language detection
                out_file.write(read_file(file_path))
                out_file.write("\n```\n\n")

    click.echo(f"Contents have been written to {output_file}")


if __name__ == "__main__":
    cli()
