# Imports.
import importlib
import sys
from datetime import datetime

import click
import pytest

sys.path.append("../")

from sources import grab_data


# Create a new CLI group instance for storing the CLI commands.
@click.group()
def cli():
    pass


# Create a new CLI command for running unit tests.
@cli.command()
def test() -> None:
    result = pytest.main(["-q", "tests"])

    if result == 0:
        print("The solutions are all integrated and tested.")
    else:
        print("The solutions might not be integrated well.")


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
    current_year = year or datetime.now().year
    module_name = f"advent.year_{current_year}.day{day}"
    function_name = f"part{part}"

    # Check if the file exists / the user has selected to use the --use-preincluded-data flag.
    if file:
        try:
            with open(file, "r") as f:
                data = f.read()
        except FileNotFoundError:
            print(
                f"\nError: Code solution for Advent of Code {current_year} (Day {day}, Part {part}) wasn't found."
            )
            return
    elif use_preincluded_data:
        try:
            data = grab_data(day=int(day), year=current_year)
        except FileNotFoundError:
            print(
                f"\nError: Solution for challenge: Advent of Code {current_year} (Day {day}, Part {part}) wasn't found."
            )
            return
    else:
        print(
            "\nError: Pass a data file using --file / -f or pass --use-preincluded-data to use developer-defined dataset."
        )
        return

    # Final (and most important layer) of checks.
    try:
        module = importlib.import_module(module_name)
        function = getattr(module, function_name)
        result = function(data)
    except ModuleNotFoundError:
        print(
            f"\nError: Year {current_year} or day {day} might be invalid. Type 'advent list-years' to see available years."
        )
    except AttributeError:
        print(
            f"\nError: Part {part} for day {day} might be invalid. Type 'advent list-days' to see available days."
        )
    except FileNotFoundError as e:
        print(f"\nError: {e}")
    else:
        print(f"\nResult: {result}")
