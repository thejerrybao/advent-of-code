from aocd.models import Puzzle
from aocd.transforms import lines
from collections import deque
from copy import deepcopy

puzzle = Puzzle(year=2022, day=5)
input_data = lines(puzzle.input_data)


class CrateStacks:

    def __init__(self, number_of_stacks):
        self.stacks = [deque() for _ in range(number_of_stacks)]

    def add_crate_to_stack(self, crate_stack_idx, crate):
        self.stacks[crate_stack_idx].append(crate)

    def execute_operation_crate_mover_9000(self, operation):
        for _ in range(operation.number_of_crates_to_move):
            crate = self.stacks[operation.from_crate_stack].pop()
            self.stacks[operation.to_crate_stack].append(crate)

    def execute_operation_crate_mover_9001(self, operation):
        crates_to_move = deque()
        for _ in range(operation.number_of_crates_to_move):
            crates_to_move.appendleft(
                self.stacks[operation.from_crate_stack].pop()
            )

        self.stacks[operation.to_crate_stack].extend(crates_to_move)

    def get_top_of_stacks(self):
        string = ""
        for stack in self.stacks:
            string += stack[-1]
        return string

    @classmethod
    def parse_crate_stacks(cls, crate_stacks_string):
        number_of_stacks = int(crate_stacks_string.pop().split()[-1])
        new_crate_stacks = CrateStacks(number_of_stacks)

        # Process in reverse for a stack like processing
        for crate_stack_string in reversed(crate_stacks_strings):
            crate_stack_row = [crate_stack_string[i:i+3].strip()
                               for i
                               in range(0, len(crate_stack_string), 4)]
            for crate_stack_idx, crate in enumerate(crate_stack_row):
                if crate:
                    crate_parsed = crate[1]
                    new_crate_stacks.add_crate_to_stack(crate_stack_idx,
                                                        crate_parsed)
        return new_crate_stacks


class Operation:
    _move_number = 'move'
    _from_crate = 'from'
    _to_crate = 'to'

    def __init__(self,
                 number_of_crates_to_move,
                 from_crate_stack,
                 to_crate_stack):
        self.number_of_crates_to_move = number_of_crates_to_move
        self.from_crate_stack = from_crate_stack
        self.to_crate_stack = to_crate_stack

    @classmethod
    # move number_of_crates from crate_stack to crate_stack
    def parse_operation(cls, operation_string):
        operation_list = operation_string.split(' ')
        move_number_idx = operation_list.index(cls._move_number) + 1
        from_crate_idx = operation_list.index(cls._from_crate) + 1
        to_crate_idx = operation_list.index(cls._to_crate) + 1

        return Operation(int(operation_list[move_number_idx]),
                         int(operation_list[from_crate_idx]) - 1,
                         int(operation_list[to_crate_idx]) - 1)


data_separator_index = input_data.index('')
crate_stacks_strings = input_data[:data_separator_index]
crate_stacks = CrateStacks.parse_crate_stacks(crate_stacks_strings)
operation_strings = input_data[data_separator_index + 1:]
operations = [Operation.parse_operation(operation_string)
              for operation_string
              in operation_strings]

crate_stacks_part_a = deepcopy(crate_stacks)
for operation in operations:
    crate_stacks_part_a.execute_operation_crate_mover_9000(operation)

puzzle.answer_a = crate_stacks_part_a.get_top_of_stacks()

crate_stacks_part_b = deepcopy(crate_stacks)
for operation in operations:
    crate_stacks_part_b.execute_operation_crate_mover_9001(operation)

puzzle.answer_b = crate_stacks_part_b.get_top_of_stacks()
