"""Day 5: Supply Stacks"""
import copy
import re


def parse_stacks(stacks_raw):
    """Parse stacks from raw input text.

    Arguments:
        stacks_raw: Raw input text representing stacks.
    Returns:
        Stacks of crates represented as lists of lists of letters.
            Lists are sorted bottom-to-top (end of list = top of crate stack).
    """
    stacks_parsed = [
        [stack[i:i+3].strip('[ ]') for i in range(0, len(stack), 4)]
        for stack in stacks_raw]
    stacks_list = [list(reversed(stack_transposed)) for stack_transposed in zip(*stacks_parsed)]
    stacks = [[letter for letter in stack if letter] for stack in stacks_list]

    return stacks


def parse_procedures(procedures_raw):
    """Parse procedures from raw input text.

    Arguments:
        procedures_raw: Raw input text representing procedures.
    Returns:
        List of tuples of procedures of the form (n_items, from_stack, to_stack)
    """
    procedure_pattern = re.compile(r'move (\d+) from (\d+) to (\d+)')
    procedures_string = [
        procedure_pattern.match(procedure_text).groups() for procedure_text in procedures_raw]
    procedures = [tuple(int(number) for number in procedure) for procedure in procedures_string]

    return procedures


def apply_procedures_individual(procedures, stacks):
    """Apply movement procedures to the stacks, moving each crate individually.

    Arguments:
        procedures: List of tuples of procedures to apply.
        stacks: List-of-list of stacks to apply procedures to.
    Returns:
        Mutated stacks list-of-lists with procedures applied.
    """
    for procedure in procedures:
        n_moves, from_stack, to_stack = procedure
        for _ in range(n_moves):
            crate = stacks[from_stack-1].pop()
            stacks[to_stack-1].append(crate)

    return stacks


def apply_procedures_bulk(procedures, stacks):
    """Apply movement procedures to the stacks, moving crates in bulk.

    Arguments:
        procedures: List of tuples of procedures to apply.
        stacks: List-of-list of stacks to apply procedures to.
    Returns:
        Mutated stacks list-of-lists with procedures applied.
    """
    for procedure in procedures:
        n_items, from_stack, to_stack = procedure
        move = stacks[from_stack - 1][-n_items:]
        del stacks[from_stack - 1][-n_items:]
        stacks[to_stack - 1].extend(move)

    return stacks


if __name__ == '__main__':
    with open('input05.txt', 'r', encoding='utf-8') as input_file:
        input_raw = input_file.read()
        stacks_lines_raw, procedures_lines_raw = input_raw.split(
            ' 1   2   3   4   5   6   7   8   9 \n\n')

    stacks_raw_input = stacks_lines_raw.splitlines()
    procedures_raw_input = procedures_lines_raw.splitlines()

    input_stacks = parse_stacks(stacks_raw_input)
    input_procedures = parse_procedures(procedures_raw_input)

    output_stacks = apply_procedures_individual(input_procedures, copy.deepcopy(input_stacks))
    top_crates_individual = [stack[-1] for stack in output_stacks]
    print(''.join(top_crates_individual))

    output_stacks_new = apply_procedures_bulk(input_procedures, copy.deepcopy(input_stacks))
    top_crates_bulk = [stack[-1] for stack in output_stacks_new]
    print(''.join(top_crates_bulk))
