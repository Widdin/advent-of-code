from math import prod, ceil


class Monkey:
    def __init__(self) -> None:
        self.id = 0
        self.items = []
        self.operation = ""
        self.test = {}
        self.inspected = 0

    def get_first_item(self) -> int:
        self.inspected += 1
        return self.items.pop(0)


class Day11:

    def part_one(self) -> int:
        puzzle_input, _ = self.load_input()
        return self.get_most_active(monkeys=puzzle_input, rounds=20)

    def part_two(self) -> int:
        puzzle_input, LCM = self.load_input()
        return self.get_most_active(monkeys=puzzle_input, rounds=10000, least_common_multiple=LCM)

    def get_most_active(self, monkeys: list, rounds: int, least_common_multiple: int = None) -> int:
        for _ in range(rounds):
            for monkey in monkeys:
                for _ in range(len(monkey.items)):
                    item = monkey.get_first_item()

                    right = monkey.operation.split()[-1]
                    left = monkey.operation.split()[-3]
                    operator = monkey.operation.split()[-2]

                    operators = {'+': lambda x, y: x + y,
                                 '-': lambda x, y: x - y,
                                 '*': lambda x, y: x * y}

                    right = item if right == 'old' else int(right)
                    left = item if left == 'old' else int(left)

                    item = operators[operator](right, left)

                    if least_common_multiple:
                        item = item % least_common_multiple
                    else:
                        item //= 3

                    throw_to = item % monkey.test['divisible'] == 0
                    monkeys[monkey.test[throw_to]].items.append(item)

        inspected = sorted([monkey.inspected for monkey in monkeys])

        return inspected[-1] * inspected[-2]

    @staticmethod
    def load_input() -> tuple[list, int]:
        monkeys, divisibles = [], []
        with open("input.txt") as file:
            lines = file.read().splitlines()
            num_monkeys = ceil(len(lines)/7)
            for i in range(0, num_monkeys):
                row_start = i * 7
                rows = lines[row_start:row_start + 7]

                monkey = Monkey()
                monkey.id = rows[0].replace(":", "").split()[-1]

                starting_items = map(int, rows[1].replace(",", "").split(":")[-1].split())
                monkey.items.extend(starting_items)

                monkey.operation = rows[2].split(":")[-1].strip()
                monkey.test = {
                    'divisible': int(rows[3].split()[-1]),
                    True: int(rows[4].split()[-1]),
                    False: int(rows[5].split()[-1])
                }
                divisibles.append(monkey.test['divisible'])
                monkeys.append(monkey)

        return monkeys, prod(divisibles)


day = Day11()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
