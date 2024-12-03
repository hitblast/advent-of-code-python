# Imports.
import subprocess

# Test parts and solutions key:value store.
test_data = {
    "1:1": "1603498",
    "1:2": "25574739",
    "2:1": "306",
    "2:2": "366",
    "3:1": "167090022",
    "3:2": "89823704",
}


# Test the Advent of Code 2024 solutions.
def test_2024() -> None:
    for part, expected_output in test_data.items():
        result = subprocess.run(
            f"advent run {part} --year 2024 --use-preincluded-data",
            shell=True,
            capture_output=True,
        ).stdout.decode("utf-8")
        assert expected_output in result
