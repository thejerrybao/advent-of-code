from aocd.models import Puzzle
from aocd.transforms import lines

puzzle = Puzzle(year=2022, day=1)
calories = lines(puzzle.input_data)

running_calorie_count = 0
elf_calorie_totals = []
for calorie in calories:
    if not calorie:
        # If it's an empty string, it's a new elf's set of snacks
        elf_calorie_totals.append(running_calorie_count)
        running_calorie_count = 0
    else:
        # Otherwise, same elf's set of snacks
        running_calorie_count += int(calorie)
elf_calorie_totals.sort(reverse=True)
# Checking that we have at least 3 totals
assert len(elf_calorie_totals) >= 3

puzzle.answer_a = elf_calorie_totals[0]
puzzle.answer_b = sum(elf_calorie_totals[:3])
