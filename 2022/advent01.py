"""Day 1: Calorie Counting"""
from collections import defaultdict


def count_elf_calories(records):
    """Count the total calories per elf.

    Args:
        List of strings of lines from Advent 01 input.
    Returns:
        Dict mapping each elf (represented by their order in the input file)
            to their total calorie count.
    """
    elf_calories = defaultdict(int)
    elf_count = 1

    while records:
        record = records.pop(0)
        if record:
            elf_calories[elf_count] += int(record)
        else:
            elf_count += 1

    return elf_calories


def sort_elf_calories(elf_calories):
    """Sort the elves by their calorie count, highest to lowest.
    Args:
        Dict mapping each elf (represented by their order in the input file)
            to their total calorie count.
    Returns:
        List of tuples of (elf, elf_calories) sorted from highest to lowest.
    """
    highest_calorie_elves = sorted(elf_calories, key=elf_calories.get, reverse=True)
    sorted_elf_calories = [(elf, elf_calories[elf]) for elf in highest_calorie_elves]

    return sorted_elf_calories


def top_n_calories(sorted_elf_calories, n):
    """Sum the total calories across the top N elves.
    
    Args:
        List of tuples of (elf, elf_calories) sorted from highest to lowest.
    Returns:
        Total calories across the top N elves.
    """
    total_calories = 0
    top_n_elves = sorted_elf_calories[:n]
    for (elf, calories) in top_n_elves:
        total_calories += calories

    return total_calories


if __name__ == '__main__':
    with open('input01.txt', 'r') as input_file:
        records = input_file.read().splitlines()
    
    elf_calories = count_elf_calories(records)
    sorted_elf_calories = sort_elf_calories(elf_calories)

    print(top_n_calories(sorted_elf_calories, 1))
    print(top_n_calories(sorted_elf_calories, 3))
