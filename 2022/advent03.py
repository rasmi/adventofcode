"""Day 3: Rucksack Reorganization"""
import string


item_priority = {item: priority for (priority, item) in enumerate(string.ascii_letters, 1)}


def find_duplicate_item(rucksack):
    """Find the duplicate item in a rucksack.

    Arguments:
        rucksack: String representing a rucksack. Will be split in half
            to represent both compartments of the rucksack.
    Returns:
        String of single item duplicated across both rucksack compartments.
    """
    first_compartment, second_compartment = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    (duplicate_item,) = set(first_compartment) & set(second_compartment)

    return duplicate_item


def find_badges(rucksack_group):
    """Find the badge item duplicated across all rucksacks in the group.

    Arguments:
        rucksack_group: List of strings representing rucksacks in the group.
    Returns:
        String of single badge item duplicated across all rucksacks in the group.
    """
    rucksack_group_sets = [set(rucksack) for rucksack in rucksack_group]
    (badge_item,) = set.intersection(*rucksack_group_sets)

    return badge_item


if __name__ == '__main__':
    with open('input03.txt', 'r', encoding='utf-8') as input_file:
        rucksacks = input_file.read().splitlines()

    duplicate_items = [find_duplicate_item(rucksack) for rucksack in rucksacks]
    sum_duplicate_priorities = sum([item_priority[item] for item in duplicate_items])
    print(sum_duplicate_priorities)

    rucksack_groups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]
    badge_items = [find_badges(rucksack_group) for rucksack_group in rucksack_groups]
    sum_badge_priorities = sum([item_priority[item] for item in badge_items])
    print(sum_badge_priorities)
