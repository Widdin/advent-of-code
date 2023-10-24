from collections import defaultdict


class Day15:
    def __init__(self):
        self.puzzle_input = self.load_input()

    def part_one(self) -> int:
        return self.play_memory(turns=2020)

    def part_two(self) -> int:
        return self.play_memory(turns=30_000_000)

    def play_memory(self, turns):
        memory, prev_num = defaultdict(int), None

        for index, value in enumerate(self.puzzle_input):
            memory[value] = index + 1
            prev_num = value

        for turn in range(len(self.puzzle_input), turns):
            curr_num = turn - memory[prev_num] if prev_num in memory else 0
            memory[prev_num] = turn
            prev_num = curr_num

        return prev_num

    @staticmethod
    def load_input() -> list:
        with open("input.txt", encoding="utf-8") as file:
            for line in file:
                return list(map(int, line.split(",")))


day = Day15()
print(f"Result part 1: {day.part_one()}")
print(f"Result part 2: {day.part_two()}")
