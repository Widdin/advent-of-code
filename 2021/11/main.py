class Day11:

    def __init__(self):
        self.puzzle_input = self.get_puzzle_input()
        self.row_length = len(self.puzzle_input[0]) - 1
        self.column_length = len(self.puzzle_input) - 1
        self.flashes = 0

    def part_one(self) -> int:
        return self.simulate_octopuses(steps=100)

    def part_two(self) -> int:
        return self.simulate_octopuses(steps=9999)

    def simulate_octopuses(self, steps) -> int:
        data = self.puzzle_input.copy()
        for i in range(steps):

            for index, line in enumerate(data):
                data[index] = [int(x)+1 for x in line]

            for x, line in enumerate(data):
                for y, number in enumerate(line):
                    if number > 9:
                        data[x][y] = 0
                        self.flashes += 1
                        self.increase_adjacent(data, x, y)

            if self.is_all_flashing(data):
                return i + 1

        return self.flashes

    @staticmethod
    def is_all_flashing(data) -> bool:
        flashing = True
        for line in data:
            if sum(line) > 0:
                flashing = False

        return flashing

    def increase_adjacent(self, data, x, y):
        d = {
            'right':        [x, y + 1],
            'left':         [x, y - 1],
            'down':         [x + 1, y],
            'down_right':   [x + 1, y + 1],
            'down_left':    [x + 1, y - 1],
            'top':          [x - 1, y],
            'top_right':    [x - 1, y + 1],
            'top_left':     [x - 1, y - 1]
        }

        for pos in d.values():
            x, y = pos
            if self.is_within_row(x) and self.is_within_column(y):
                if data[x][y] != 0:
                    data[x][y] += 1
                    if data[x][y] > 9:
                        data[x][y] = 0
                        self.flashes += 1
                        self.increase_adjacent(data, x, y)

    def is_within_column(self, number) -> bool:
        return 0 <= number <= self.column_length

    def is_within_row(self, number) -> bool:
        return 0 <= number <= self.row_length

    @staticmethod
    def get_puzzle_input() -> list:
        lst = []
        with open("input.txt") as file:
            for line in file:
                lst.append(list(line.rstrip()))
        return lst


day = Day11()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
