from aocd.models import Puzzle
from aocd.transforms import lines
from string import ascii_letters

# Input
puzzle = Puzzle(year=2022, day=3)
rucksacks = lines(puzzle.input_data)

# Solution
item_priority = {
    letter: index + 1
    for index, letter
    in enumerate(ascii_letters)
}
def get_common_rucksack_item(list_of_rucksacks):
    rucksack_sets = [set(x) for x in list_of_rucksacks]
    intersecting_set = rucksack_sets.pop()
    for rucksack_set in rucksack_sets:
        intersecting_set = intersecting_set.intersection(rucksack_set)

    # Checking that only one item intersects
    assert len(intersecting_set) == 1
    return intersecting_set.pop()

# Answer A
total_item_priority_sum_part_a = 0
for rucksack in rucksacks:
    halfway_index = len(rucksack) // 2
    first_rucksack = rucksack[:halfway_index]
    second_rucksack = rucksack[halfway_index:]
    # Checking that both rucksacks are the same size
    assert len(first_rucksack) == len(second_rucksack)

    common_rucksack_item = get_common_rucksack_item((first_rucksack, second_rucksack))
    total_item_priority_sum_part_a += item_priority.get(common_rucksack_item)

puzzle.answer_a = total_item_priority_sum_part_a

# Answer B
total_item_priority_sum_part_b = 0
rucksack_groups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]
for rucksack_group in rucksack_groups:
    common_rucksack_item = get_common_rucksack_item(rucksack_group)
    total_item_priority_sum_part_b += item_priority.get(common_rucksack_item)

puzzle.answer_b = total_item_priority_sum_part_b
