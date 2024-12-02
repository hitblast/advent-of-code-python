# The second challenge (part two) of Advent of Code 2024.

# This is the result variable.
safe_reports = 0


# Function to check if ascending or descending.
def check_asc_desc(data_list):
    asc = all(data_list[i] < data_list[i + 1] for i in range(len(data_list) - 1))
    desc = all(data_list[i] > data_list[i + 1] for i in range(len(data_list) - 1))
    return asc or desc


# Read 2-data.txt and split each line into a list of integers.
with open("2-data.txt") as f:
    data = [[int(i) for i in line.split()] for line in f]

# Iterate through the data.
for data_list in data:
    # Rules:
    # Check: Each list must be in either ascending or descending order. Otherwise it is invalid.
    # Any two numbers in the list must differ by at least 1 and at most 3.

    if check_asc_desc(data_list):
        if all(
            1 <= abs(data_list[i] - data_list[i + 1]) <= 3
            for i in range(len(data_list) - 1)
        ):
            safe_reports += 1

# Print the result
print(safe_reports)
