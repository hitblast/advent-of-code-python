# Imports.
import re


# Day 3 - Part 1
def part1(data: str) -> int:
    result = 0

    mul_functions = re.findall(r"mul\(\d+,\d+\)", data)
    arguments = [re.findall(r"\d+", mul_function) for mul_function in mul_functions]

    for arg1, arg2 in arguments:
        result += int(arg1) * int(arg2)

    return result


# Day 3 - Part 2
def part2(data: str) -> int:
    result = 0
    enabled = True

    instructions = re.findall(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", data)

    for instruction in instructions:
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        else:
            if enabled:
                arg1, arg2 = re.findall(r"\d+", instruction)
                result += int(arg1) * int(arg2)

    return result
