class Day10:

    def __init__(self):
        self.puzzle_input = self.get_puzzle_input()
        self.lines_corrupted = []
        self.lines_incomplete = []
        self.parse_lines()

    def part_one(self) -> int:
        return self.get_corrupted_score()

    def part_two(self) -> int:
        return self.get_incomplete_score()

    def get_corrupted_score(self) -> int:
        point_system = {')': 3, ']': 57, '}': 1197, '>': 25137}
        return sum([point_system[x] for x in self.lines_corrupted])

    def get_incomplete_score(self) -> int:
        point_system = {'(': 1, '[': 2, '{': 3, '<': 4}

        def calc_score(lst):
            lst.reverse()

            score = 0
            for char in lst:
                score = (score * 5) + point_system[char]

            return score

        scores = [calc_score(lst) for lst in self.lines_incomplete]
        scores.sort()

        return scores[len(scores) // 2]

    def parse_lines(self):
        data = self.puzzle_input.copy()

        for line in data:
            stack = []
            is_incomplete = True
            for char in line:
                if self.is_opening_bracket(char):
                    stack.append(char)
                else:
                    if stack[-1] == self.get_closing_bracket(char):
                        stack.pop()
                    else:
                        is_incomplete = False
                        self.lines_corrupted.append(char)
                        break

            if is_incomplete:
                self.lines_incomplete.append(stack)

    @staticmethod
    def get_closing_bracket(char):
        return {')': '(', ']': '[', '>': '<', '}': '{'}[char]

    @staticmethod
    def is_opening_bracket(char):
        return True if char in ['(', '[', '<', '{'] else False

    @staticmethod
    def get_puzzle_input() -> list:
        lst = []
        with open("input.txt") as file:
            for line in file:
                lst.append(line.rstrip())
        return lst


day = Day10()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
