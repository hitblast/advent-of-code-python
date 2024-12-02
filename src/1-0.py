# The first challenge (part one) of Advent of Code 2024

# This is the result variable.
result = 0

# Read 1-data.txt and split by lines, then since each line has two parts, split them and store the first element in list_1 and the second element in list_2
with open("1-data.txt") as f:
    lines = f.read().splitlines()
    list_1 = sorted([int(i.split()[0]) for i in lines])
    list_2 = sorted([int(i.split()[1]) for i in lines])

# Pre-flight checks sire!
if len(list_1) != len(list_2):
    print("The lists are not of the same length")
    exit()

# Iterate through two of the lists together.
for i, j in zip(list_1, list_2):
    distance = i - j if i > j else j - i
    result += distance

# Print the result
print(result)
