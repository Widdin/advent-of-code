from collections import defaultdict


class Day06:
    def __init__(self):
        self.puzzle_input = self.load_input()

    def part_one(self) -> int:
        return self.get_answers_group(self.puzzle_input)

    def part_two(self) -> int:
        return self.get_answers_everyone(self.puzzle_input)

    @staticmethod
    def get_answers_group(puzzle_input: list) -> int:
        answers = 0
        for groups in puzzle_input:
            groups_set = set()
            for group in groups:
                groups_set.update(set(group))
            answers += len(groups_set)
        return answers

    @staticmethod
    def get_answers_everyone(puzzle_input: list) -> int:
        answers = 0
        for groups in puzzle_input:
            count_letters = defaultdict(int)
            for group in groups:
                for letter in group:
                    count_letters[letter] += 1
            all_answered = [
                key for key, value in count_letters.items() if value == len(groups)
            ]
            answers += len(all_answered)
        return answers

    @staticmethod
    def load_input() -> list:
        list_input = []
        with open("input.txt") as file:
            group = []
            for line in file:
                if line == "\n":
                    list_input.append(group)
                    group = []
                else:
                    group.append(list(line.rstrip()))
            list_input.append(group)
        return list_input


day = Day06()
print(f"Result part 1: {day.part_one()}")
print(f"Result part 2: {day.part_two()}")
