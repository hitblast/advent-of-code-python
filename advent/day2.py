# Imports.
from sources import data_decorator


# Day 2 - Part 1
@data_decorator(day=2)
def part1(data: str) -> int:
    safe_reports = 0

    # Function to check if ascending or descending.
    def check_asc_desc(data_list):
        asc = all(data_list[i] < data_list[i + 1] for i in range(len(data_list) - 1))
        desc = all(data_list[i] > data_list[i + 1] for i in range(len(data_list) - 1))
        return asc or desc

    # Read data and split each line into a list of integers.
    data_lines = [[int(i) for i in line.split()] for line in data.splitlines()]

    # Iterate through the data.
    for data_list in data_lines:
        # Rules:
        # Check: Each list must be in either ascending or descending order. Otherwise it is invalid.
        # Any two numbers in the list must differ by at least 1 and at most 3.

        if check_asc_desc(data_list):
            if all(
                1 <= abs(data_list[i] - data_list[i + 1]) <= 3
                for i in range(len(data_list) - 1)
            ):
                safe_reports += 1

    return safe_reports


# Day 2 - Part 2
@data_decorator(day=2)
def part2(data: str) -> int:
    safe_reports = 0

    # Function to check if a list is in ascending or descending order
    def is_ordered(data_list):
        asc = all(data_list[i] < data_list[i + 1] for i in range(len(data_list) - 1))
        desc = all(data_list[i] > data_list[i + 1] for i in range(len(data_list) - 1))
        return asc or desc

    # Function to check if the differences between adjacent elements are within the allowed range
    def valid_differences(data_list):
        return all(
            1 <= abs(data_list[i] - data_list[i + 1]) <= 3
            for i in range(len(data_list) - 1)
        )

    # Function to check if a list can be made ordered by removing one element
    def dampener(data_list):
        for i in range(len(data_list)):
            temp_list = data_list[:i] + data_list[i + 1 :]
            if is_ordered(temp_list) and valid_differences(temp_list):
                return True
        return False

    # Read 2-data.txt and split each line into a list of integers.
    data_lines = [[int(i) for i in line.split()] for line in data.splitlines()]

    # Iterate through the data.
    for data_list in data_lines:
        if (is_ordered(data_list) and valid_differences(data_list)) or dampener(
            data_list
        ):
            safe_reports += 1

    return safe_reports
