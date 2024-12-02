# Imports.
import importlib
import sys
from datetime import datetime

import click

sys.path.append("../")

from sources import grab_data


# Create a new CLI group instance for storing the CLI commands.
@click.group()
def cli():
    pass


# Create a new CLI command for running the Advent of Code solutions.
# advent run <day_part> [options]
@cli.command()
@click.argument("day_part", type=str)
@click.option(
    "-f",
    "--file",
    type=str,
    help="The path to the data file.",
    required=False,
)
@click.option(
    "-y",
    "--year",
    type=int,
    help="The year of the Advent of Code.",
    required=False,
)
@click.option(
    "--use-preincluded-data",
    is_flag=True,
    help="Use the pre-included data for the day.",
)
def run(
    day_part: str,
    file: str | None = None,
    year: int | None = None,
    use_preincluded_data: bool = False,
) -> None:
    day, part = day_part.split(":")

    # Initial variables.
    # Necessary for accessing the inner structure of the project via importlib.
    current_year = datetime.now().year if not year else year
    data = ""
    module_name = f"advent.year_{current_year}.day{day}"
    function_name = f"part{part}"

    if file:
        with open(file, "r") as f:
            data = f.read()
            f.close()
    else:
        if use_preincluded_data:
            data = grab_data(day=int(day), year=current_year)
        else:
            print(
                "Error: Pass a data file using --file / -f or pass --use-preincluded-data to use developer-defined dataset."
            )
            return

    try:
        module = importlib.import_module(module_name)
        function = getattr(module, function_name)
        result = function(data)

    except ModuleNotFoundError as _:
        print(
            "Error: Year might be invalid. Type 'advent list-years' to see available years."
        )

    except AttributeError as _:
        print(
            "Error: Day or part might be invalid. Type 'advent list-days' to see available days."
        )

    else:
        print(f"Result: {result}")


if __name__ == "__main__":
    cli()
