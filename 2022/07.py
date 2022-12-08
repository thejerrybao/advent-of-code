from aocd.models import Puzzle
from aocd.transforms import lines

puzzle = Puzzle(year=2022, day=7)
terminal_output = lines(puzzle.input_data)


class File:

    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory:

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = {}

    @property
    def size(self):
        size = 0
        for child in self.children.values():
            size += child.size

        return size

    @property
    def directories(self):
        return filter(
            lambda child: isinstance(child, Directory),
            self.children.values())

    def add(self, file):
        if file.name not in self.children:
            self.children[file.name] = file

    def cd(self, directory):
        if directory == '..':
            return self.parent
        if directory not in self.children:
            raise NotADirectoryError()
        return self.children[directory]

    def parse_ls(self, ls_output):
        for ls_line in ls_output:
            ls_line_split = ls_line.split()

            if ls_line_split[0] == 'dir' and \
                    ls_line_split[1] not in self.children:
                new_directory = Directory(ls_line_split[1], self)
                self.add(new_directory)
            else:
                new_file = File(ls_line_split[1], int(ls_line_split[0]))
                self.add(new_file)


root_directory = Directory('/', None)
current_directory = root_directory

i = 1
while i < len(terminal_output):
    terminal_cmd_args = terminal_output[i].split()

    if terminal_cmd_args[0] == '$':
        if terminal_cmd_args[1] == 'cd':
            current_directory = current_directory.cd(terminal_cmd_args[2])
            i += 1
        elif terminal_cmd_args[1] == 'ls':
            start_ls = i + 1
            end_ls = start_ls

            next_terminal_line = terminal_output[end_ls].split()
            while next_terminal_line[0] != '$' and end_ls < len(terminal_output):
                end_ls += 1
                if end_ls < len(terminal_output):
                    next_terminal_line = terminal_output[end_ls].split()

            i = end_ls
            current_directory.parse_ls(terminal_output[start_ls:end_ls])

directories_to_traverse = [root_directory]
total_directories_at_most_100000 = 0
while len(directories_to_traverse) > 0:
    current_directory = directories_to_traverse.pop()
    current_directory_size = current_directory.size

    if current_directory_size < 100_000:
        total_directories_at_most_100000 += current_directory_size

    directories_to_traverse.extend(current_directory.directories)

puzzle.answer_a = total_directories_at_most_100000

total_diskspace = 70_000_000
unused_space_needed_for_update = 30_000_000
root_diskspace = root_directory.size
unused_diskspace = total_diskspace - root_diskspace
diskspace_needed_for_update = unused_space_needed_for_update - unused_diskspace

directories_to_traverse = [root_directory]
smallest_size_to_delete = float("inf")
while len(directories_to_traverse) > 0:
    current_directory = directories_to_traverse.pop()
    current_directory_size = current_directory.size

    if current_directory_size >= diskspace_needed_for_update:
        smallest_size_to_delete = min(smallest_size_to_delete,
                                      current_directory_size)

    directories_to_traverse.extend(current_directory.directories)

puzzle.answer_b = smallest_size_to_delete
