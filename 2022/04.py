from aocd.models import Puzzle
from aocd.transforms import lines

# Input
puzzle = Puzzle(year=2022, day=4)
input_data = lines(puzzle.input_data)
pair_section_assignments_string = [data.split(',') for data in input_data]
pair_section_assignments = []
for pair_section_assignment_string in pair_section_assignments_string:
    section_assignment_numbers = []
    for section_assignment_string in pair_section_assignment_string:
        section_assignment_number = [int(value) for value in
                                     section_assignment_string.split('-')]
        section_assignment_numbers.append(section_assignment_number)
    pair_section_assignments.append(section_assignment_numbers)


# Solution
# Answer A
def contains_section(first_section, second_section):
    def contains_section_helper(a, b):
        if a[0] <= b[0] and \
                a[1] >= b[1]:
            return True
        return False

    return contains_section_helper(first_section, second_section) or \
           contains_section_helper(second_section, first_section)


total_duplicate_assignments_part_a = 0
for pair_section_assignment in pair_section_assignments:
    first_section_assignment = pair_section_assignment[0]
    second_section_assignment = pair_section_assignment[1]

    if contains_section(first_section_assignment, second_section_assignment):
        total_duplicate_assignments_part_a += 1

puzzle.answer_a = total_duplicate_assignments_part_a


# Answer B
def overlaps_section(first_section, second_section):
    max_start = max(first_section[0], second_section[0])
    min_end = min(first_section[1], second_section[1])
    if min_end < max_start:
        return False
    return True


total_duplicate_assignments_part_b = 0
for pair_section_assignment in pair_section_assignments:
    first_section_assignment = pair_section_assignment[0]
    second_section_assignment = pair_section_assignment[1]

    if overlaps_section(first_section_assignment, second_section_assignment) or \
            contains_section(first_section_assignment, second_section_assignment):
        total_duplicate_assignments_part_b += 1

puzzle.answer_b = total_duplicate_assignments_part_b
