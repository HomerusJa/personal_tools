# Tools

This directory contains several little scripts I wrote over the past times. Some of them are also taken from Github.

## Installation

I will describe the installation using pipx, but you can also use other methods.

1. Clone this repository
2. Run `pipx install .`

Now the tools should be globally available using the `tools` command.

## Scripts

Following is a list of all the scripts included in this repository. Run those single scripts using `python scriptname.py`, or use the global command.

- `dir_to_md.py`: Write the content of a directory to a markdown file. Also includes the ability to exclude files and directories.
- `dir_tree.py`: Build a directory tree

## Adding new tools

If you want to add a new tool, just add a new file with the same structure as `tool_template.py` to the `src\tools` folder. The tool will be called the same name as the python file.

Remember to reinstall the tools everytime you add a new one using the following commands:

```shell
cd personal_tools
pipx uninstall tools
pipx install .
```

Note that `pipx reinstall` is not working here due to the dynamic imports to include all commands.
