"""Day 8: Treetop Tree House"""


def check_visible(row):
    """Check whether each tree in a row is visible from the left/start."""
    visibility = []
    current_max = -1
    for number in row:
        visibility.append(number > current_max)
        current_max = max(number, current_max)

    return visibility


def check_scenery(row):
    """Compute how many trees are visible from each tree from the left/start."""
    scenery_scores = []
    for (index, number) in enumerate(row):
        score = 0
        for adjacent_number in row[min(index+1, len(row)):len(row)]:
            if number > adjacent_number:
                score += 1
            else:
                # We count the end tree in the scenery score.
                score += 1
                break
        scenery_scores.append(score)

    return scenery_scores


def apply_to_grid(rows, apply, reduce):
    """Apply map and reduce operations to a grid.

    Arguments:
        rows: A grid represented as a list of rows of items.
        apply: The function to map vertically and horizontally to each item in the grid.
        reduce: The function used to reduce the vertical and horizontal values from 'apply'.
    Returns:
        A grid of the same shape as the input, with map and reduce operations applied.
    """
    columns = list(zip(*rows))

    horizontal = [
        [reduce(left, right) for (left, right) in
        zip(apply(row), reversed(apply(list(reversed(row)))))]
        for row in rows
    ]

    vertical = [
        [reduce(up, down) for (up, down) in
        zip(apply(column), reversed(apply(list(reversed(column)))))]
        for column in columns
    ]

    combined = [
        list(zip(horizontal[i], list(zip(*vertical))[i]))
        for i in range(len(horizontal))
    ]

    reduced = [
        [reduce(horizontal, vertical) for (horizontal, vertical) in row]
        for row in combined
    ]

    return reduced


def compute_total_visible(rows):
    """Compute the total number of trees visible from outside the grid."""
    # Use `or` to check for visibility from any direction.
    is_visible = apply_to_grid(rows, check_visible, lambda a, b: (a or b))
    total_visible = sum([sum(row) for row in is_visible])

    return total_visible


def compute_max_scenery(rows):
    """Compute the highest scenic score possible for any tree in the grid."""
    # Use `*` to compute scenery score as a multiple of scenery of all directions.
    scenery_scores = apply_to_grid(rows, check_scenery, lambda a, b: (a * b))
    max_scenery = max([max(row) for row in scenery_scores])

    return max_scenery


if __name__ == '__main__':
    with open('input08.txt', 'r', encoding='utf-8') as input_file:
        grid_raw = input_file.read().splitlines()

    grid_rows = [tuple(int(num) for num in row) for row in grid_raw]

    print(compute_total_visible(grid_rows))
    print(compute_max_scenery(grid_rows))
