# The first challenge (part two) of Advent of Code 2024.
# This uses the same data file as the first challenge.

# This is the result variable.
result = 0

# Read 1-data.txt and split by lines, then since each line has two parts, split them and store the first element in list_1 and the second element in list_2
with open("1-data.txt") as f:
    lines = f.read().splitlines()
    list_1 = sorted([int(i.split()[0]) for i in lines])
    list_2 = sorted([int(i.split()[1]) for i in lines])

# Once again...
# Pre-flight checks sire!
if len(list_1) != len(list_2):
    print("The lists are not of the same length")
    exit()

# Iterate through two of the lists together.
for i in list_1:
    similarity_score = i
    multiply_by = 0

    for j in list_2:
        if i == j:
            multiply_by += 1

    result_for_one = similarity_score * multiply_by
    result += result_for_one


# Print the result
print(result)
