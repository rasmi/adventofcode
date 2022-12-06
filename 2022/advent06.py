"""Day 6: Tuning Trouble"""
import collections


def parse_message(message, n_characters):
    """Parse through a message until N consecutive distinct characters are found.

    Arguments:
        message: String message to parse through.
        n_characters: Number of consecutive distinct characters necessary to find.
    Returns:
        The index of the character immediately after the N consecutive distinct characters.
    """
    buffer = collections.OrderedDict()
    for index, letter in enumerate(message):
        while letter in buffer:
            # Non-unique letter.
            # Keep clearing the buffer until only unique letters exist.
            buffer.popitem(last=False)

        buffer[letter] = index
        if len(buffer) == n_characters:
            return index + 1


if __name__ == '__main__':
    with open('input06.txt', 'r', encoding='utf-8') as input_file:
        input_message = input_file.read().strip()

    print(parse_message(input_message, 4))
    print(parse_message(input_message, 14))
