# Day 1 - Part 1
def part1(data: str) -> int | None:
    result = 0

    # Sanitize data, split by lines and sort in ascending order.
    lines = data.splitlines()
    list_1 = sorted([int(i.split()[0]) for i in lines])
    list_2 = sorted([int(i.split()[1]) for i in lines])

    # Pre-flight checks sire!
    if len(list_1) != len(list_2):
        print(
            "Operation not possible for current data since the lists are not of the same length."
        )
        return

    # Iterate through two of the lists together.
    # Also dynamically calculate the distance between each levels.
    for i, j in zip(list_1, list_2):
        distance = i - j if i > j else j - i
        result += distance

    # Print the result
    return result


# Day 1 - Part 2
def part2(data: str) -> int | None:
    result = 0

    # Like previous, read file, split by lines and sort in ascending order.
    lines = data.splitlines()
    list_1 = sorted([int(i.split()[0]) for i in lines])
    list_2 = sorted([int(i.split()[1]) for i in lines])

    # Once again...
    # Pre-flight checks sire!
    if len(list_1) != len(list_2):
        print(
            "Operation not possible for current data since the lists are not of the same length."
        )
        return

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
    return result
