class Day09:

    def __init__(self):
        self.puzzle_input = self.get_puzzle_input()

        self.row_length = len(self.puzzle_input[0]) - 1
        self.column_length = len(self.puzzle_input) - 1

        self.low_points = []
        self.basins = []

        self.find_low_points_and_basins()

    def part_one(self) -> int:
        return self.get_sum_risk_level()

    def part_two(self) -> int:
        return self.get_sum_three_largest_basin()

    def get_sum_risk_level(self) -> int:
        return sum([int(x) for x in self.low_points]) + len(self.low_points)

    def get_sum_three_largest_basin(self) -> int:
        self.basins.sort()
        return self.basins[-1] * self.basins[-2] * self.basins[-3]

    def find_low_points_and_basins(self):
        data = self.puzzle_input.copy()
        for x, line in enumerate(data):
            for y, number in enumerate(line):
                if self.is_low_point(data, x, y, int(number)):
                    self.low_points.append(number)
                    self.basins.append(self.get_basin(data, [x], [y], [number], [[x, y]]))

    def get_basin(self, data, x, y, number, visited):
        x_positions = []
        y_positions = []
        new_numbers = []

        for i in range(len(number)):
            current_number = int(number[i])
            x_pos = x[i]
            y_pos = y[i]

            # Right
            if self.is_within_row(y_pos + 1):
                if current_number < int(data[x_pos][y_pos + 1]) < 9:
                    if [x_pos, y_pos + 1] not in visited:
                        x_positions.append(x_pos)
                        y_positions.append(y_pos + 1)
                        new_numbers.append(int(data[x_pos][y_pos + 1]))
                        visited.append([x_pos, y_pos + 1])

            # Top
            if self.is_within_column(x_pos - 1):
                if current_number < int(data[x_pos - 1][y_pos]) < 9:
                    if [x_pos - 1, y_pos] not in visited:
                        x_positions.append(x_pos - 1)
                        y_positions.append(y_pos)
                        new_numbers.append(int(data[x_pos - 1][y_pos]))
                        visited.append([x_pos - 1, y_pos])

            # Left
            if self.is_within_row(y_pos - 1):
                if current_number < int(data[x_pos][y_pos - 1]) < 9:
                    if [x_pos, y_pos - 1] not in visited:
                        x_positions.append(x_pos)
                        y_positions.append(y_pos - 1)
                        new_numbers.append(int(data[x_pos][y_pos - 1]))
                        visited.append([x_pos, y_pos - 1])

            # Down
            if self.is_within_column(x_pos + 1):
                if current_number < int(data[x_pos + 1][y_pos]) < 9:
                    if [x_pos + 1, y_pos] not in visited:
                        x_positions.append(x_pos + 1)
                        y_positions.append(y_pos)
                        new_numbers.append(int(data[x_pos + 1][y_pos]))
                        visited.append([x_pos + 1, y_pos])

        return len(visited) if len(new_numbers) == 0 else self.get_basin(data, x_positions, y_positions, new_numbers, visited)

    def is_within_column(self, number):
        return 0 <= number <= self.column_length

    def is_within_row(self, number):
        return 0 <= number <= self.row_length

    def is_low_point(self, data, x, y, number):
        right = int(data[x][y + 1]) if self.is_within_column(y + 1) else 1e9
        left = int(data[x][y - 1]) if self.is_within_column(y - 1) else 1e9
        down = int(data[x + 1][y]) if self.is_within_row(x + 1) else 1e9
        top = int(data[x - 1][y]) if self.is_within_row(x - 1) else 1e9

        if min(right, left, down, top) > number:
            return True

    @staticmethod
    def get_puzzle_input() -> list:
        lst = []
        with open("input.txt") as file:
            for line in file:
                lst.append(line.rstrip())
        return lst


day = Day09()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
