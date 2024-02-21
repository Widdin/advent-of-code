import re


class Day18:
    def __init__(self):
        self.puzzle_input = self.load_input()
        self.parentheses_pattern = r"\(([^()]+)\)"
        self.num_plus_num_pattern = r"\b(\d+)\s*\+\s*(\d+)\b"
        self.operators = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y}

    def part_one(self) -> int:
        return self.eval_expressions(self.eval_left_to_right)

    def part_two(self) -> int:
        return self.eval_expressions(self.eval_add_then_mult)

    def eval_expressions(self, math_rule) -> int:
        total_sum = 0
        for line in self.puzzle_input:
            while re.search(self.parentheses_pattern, line):
                match = re.search(self.parentheses_pattern, line)
                eval_num = math_rule(match.group().strip("()"))
                line = line.replace(match.group(), str(eval_num))
            total_sum += math_rule(line)

        return total_sum

    def eval_left_to_right(self, string: str) -> int:
        splitted_string = string.split(" ")

        while len(splitted_string) > 1:
            first_num, operator, second_num = splitted_string[:3]
            eval_num = self.operators[operator](int(first_num), int(second_num))
            splitted_string = [eval_num] + splitted_string[3:]

        return int(splitted_string[0])

    def eval_add_then_mult(self, string: str) -> int:
        while re.search(self.num_plus_num_pattern, string) is not None:
            match = re.search(self.num_plus_num_pattern, string)
            first_num, operator, second_num = match.group().split(" ")
            eval_num = self.operators[operator](int(first_num), int(second_num))
            string = string.replace(match.group(), str(eval_num), 1)

        return eval(string)

    @staticmethod
    def load_input() -> list:
        list_input = []
        with open("input.txt", encoding="utf-8") as file:
            for line in file:
                list_input.append(line.rstrip())
        return list_input


day = Day18()
print(f"Result part 1: {day.part_one()}")
print(f"Result part 2: {day.part_two()}")
