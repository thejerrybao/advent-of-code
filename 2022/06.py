from aocd.models import Puzzle

# Input
puzzle = Puzzle(year=2022, day=6)
device_datastream = puzzle.input_data


def find_start_of_marker(datastream, marker_length):
    for i in range(0, len(datastream) - marker_length):
        substr = device_datastream[i:i+marker_length]
        if len(set(substr)) == marker_length:
            return i + marker_length


# Solution
# Answer A
puzzle.answer_a = find_start_of_marker(device_datastream, 4)

# Answer B
puzzle.answer_b = find_start_of_marker(device_datastream, 14)
