"""Day 7: No Space Left On Device"""
from pathlib import PurePosixPath


class FileSystem:
    """FileSystem class for parsing input commands and computing sizes."""

    def __init__(self, lines):
        self.tree = {}
        self.parse_directory_tree(lines)
        self.compute_subdirectory_sizes()

    def parse_directory_tree(self, lines):
        """Parse input lines into a directory tree."""
        self.tree.clear()

        current_directory = ''

        while lines:
            line = lines.pop(0)
            if line.startswith('$ cd'):
                # Change directory.
                _, new_directory = line.split('$ cd ')
                if new_directory == '..':
                    # Switch to parent directory.
                    current_directory = self.tree[current_directory]['parent']
                else:
                    # Switch to child directory.
                    new_directory_path = str(
                        PurePosixPath(current_directory).joinpath(new_directory))
                    if new_directory_path not in self.tree:
                        # Initialize new directory in directory tree.
                        self.tree[new_directory_path] = {
                            'parent': current_directory,
                            'children': [],
                            'files': []
                        }
                    current_directory = new_directory_path
            elif line == '$ ls':
                # List all files and folders in the current directory (move on to the next line)
                continue
            elif line.startswith('dir'):
                # Directory information.
                _, child_directory = line.split('dir ')
                child_directory_path = str(
                    PurePosixPath(current_directory).joinpath(child_directory))
                self.tree[current_directory]['children'].append(child_directory_path)
            elif line[0].isdigit():
                # File information.
                filesize, filename = line.split(' ')
                self.tree[current_directory]['files'].append(
                    {'filename': filename, 'filesize': int(filesize)})

    def compute_subdirectory_sizes(self, root_directory='/'):
        """Compute the total directory size for each directory in the tree."""
        directory_size = 0

        # Sum file sizes in current directory.
        for file in self.tree[root_directory]['files']:
            directory_size += file['filesize']

        # Recursively compute sizes through all child directories.
        for directory in self.tree[root_directory]['children']:
            directory_size += self.compute_subdirectory_sizes(directory)

        self.tree[root_directory]['directory_size'] = directory_size

        return directory_size

    def sum_directories_under_size(self, max_size):
        """Sum of total sizes of directories under size max_size."""
        directory_sizes = [directory['directory_size'] for directory in self.tree.values()]
        small_directory_sizes = [size for size in directory_sizes if size < max_size]
        sum_directory_sizes = sum(small_directory_sizes)

        return sum_directory_sizes

    def smallest_to_delete(self, total_capacity, required_space):
        """Smallest directory to be deleted to clear the minimum necessary amount of space."""
        current_free_space = total_capacity - self.tree['/']['directory_size']
        need_to_delete = required_space - current_free_space

        directory_sizes = [directory['directory_size'] for directory in self.tree.values()]
        for size in sorted(directory_sizes):
            if size >= need_to_delete:
                return size
        return None


if __name__ == '__main__':
    with open('input07.txt', 'r', encoding='utf-8') as input_file:
        input_lines = input_file.read().splitlines()

    file_system = FileSystem(input_lines)

    print(file_system.sum_directories_under_size(100000))
    print(file_system.smallest_to_delete(total_capacity=70000000, required_space=30000000))
