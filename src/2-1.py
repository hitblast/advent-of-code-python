# The second challenge (part two) of Advent of Code 2024.

# This is the result variable.
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
with open("2-data.txt") as f:
    lines = f.read().splitlines()
    data = [[int(i) for i in line.split()] for line in lines]

# Iterate through the data.
for data_list in data:
    # Check if the list is ordered and has valid differences
    if (is_ordered(data_list) and valid_differences(data_list)) or dampener(data_list):
        safe_reports += 1


# Print the result
print(safe_reports)
