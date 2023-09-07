class Day01:

    def __init__(self):
        self.puzzle_input = self.load_input()

    def part_one(self) -> int:
        num_set = set()
        for first in self.puzzle_input:
            second = 2020 - first
            if second in num_set:
                return first * second
            num_set.add(first)

    def part_two(self) -> int:
        for first in self.puzzle_input:
            num_to_find = 2020 - first
            num_set = set()
            for second in self.puzzle_input:
                third = num_to_find - second
                if third in num_set:
                    return first * second * third
                num_set.add(second)

    @staticmethod
    def load_input() -> list:
        list_input = []
        with open("input.txt") as file:
            for line in file:
                list_input.append(int(line.rstrip()))
        return list_input


day = Day01()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
