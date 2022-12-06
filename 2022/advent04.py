"""Day 4: Camp Cleanup"""


def split_assignments(assignment_pair):
    """Split assignment inputs into pairs.

    Arguments:
        assignment_pair: String of the form '2-4,6-8' representing
            assignment_a,assignment_b
    Returns:
        Tuple of tuples of int ranges for assignment_a and assignment_b.
    """
    assignments = assignment_pair.split(',')
    assignment_a, assignment_b = tuple(
        tuple(map(int, assignment.split('-')))
        for assignment in assignments)

    return (assignment_a, assignment_b)


def check_fully_overlap(assignment_a, assignment_b):
    """Check whether either assignment fully contains another.

    Arguments:
        assignment_a, assignment_b: Two tuples of int ranges representing
            assignment_a and assignment_b.
    Returns:
        Boolean of whether either assignment fully contains another.
    """
    ((a_start, a_end), (b_start, b_end)) = (assignment_a, assignment_b)
    fully_overlaps = (
        ((a_start <= b_start) and
        (a_end >= b_end)) or
        ((b_start <= a_start) and
        (b_end >= a_end))
    )
    return fully_overlaps


def check_any_overlap(assignment_a, assignment_b):
    """Check whether both assignments overlap at all.

    Arguments:
        assignment_a, assignment_b: Two tuples of int ranges representing
            assignment_a and assignment_b.
    Returns:
        Boolean of whether both assignments overlap at all.
    """
    ((a_start, a_end), (b_start, b_end)) = (assignment_a, assignment_b)
    no_overlap = (
        (a_end < b_start) or
        (a_start > b_end)
    )
    any_overlap = (not no_overlap)

    return any_overlap


if __name__ == '__main__':
    with open('input04.txt', 'r', encoding='utf-8') as input_file:
        assignment_pairs = input_file.read().splitlines()

    full_overlaps = [
        check_fully_overlap(*split_assignments(assignment_pair))
        for assignment_pair in assignment_pairs]
    total_full_overlaps = sum(full_overlaps)
    print(total_full_overlaps)

    any_overlaps = [
        check_any_overlap(*split_assignments(assignment_pair))
        for assignment_pair in assignment_pairs]
    total_any_overlaps = sum(any_overlaps)
    print(total_any_overlaps)
