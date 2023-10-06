from copy import deepcopy


class Day11:
    OCCUPIED_LIMIT_ADJACENT = 4
    OCCUPIED_LIMIT_IN_SIGHT = 5
    DIRECTIONS = {
        "RIGHT": [0, +1],
        "LEFT": [0, -1],
        "DOWN": [+1, 0],
        "DOWN_RIGHT": [+1, +1],
        "DOWN_LEFT": [+1, -1],
        "TOP": [-1, 0],
        "TOP_RIGHT": [-1, +1],
        "TOP_LEFT": [-1, -1],
    }

    def __init__(self):
        self.puzzle_input = self.load_input()
        self.row_length = len(self.puzzle_input[0])
        self.column_length = len(self.puzzle_input)
        self.modified_grid = deepcopy(self.puzzle_input)

    def part_one(self) -> int:
        original_grid = deepcopy(self.puzzle_input)
        while True:
            has_modified = has_modified = self.iterate_grid(original_grid, in_sight=False)

            if not has_modified:
                return self.get_occupied_seats(self.modified_grid)

            original_grid = deepcopy(self.modified_grid)

    def part_two(self) -> int:
        original_grid = deepcopy(self.puzzle_input)
        while True:
            has_modified = self.iterate_grid(original_grid, in_sight=True)

            if not has_modified:
                return self.get_occupied_seats(self.modified_grid)

            original_grid = deepcopy(self.modified_grid)

    def iterate_grid(self, original_grid: list, in_sight: bool) -> bool:
        has_modified = False
        for x in range(self.column_length):
            for y in range(self.row_length):
                if self.is_seat_occupied(original_grid[x][y]):
                    if in_sight:
                        modify = self.get_occupied_seats_in_sight(x, y, original_grid) >= self.OCCUPIED_LIMIT_IN_SIGHT
                    else:
                        modify = self.get_occupied_seats_adjacent(x, y, original_grid) >= self.OCCUPIED_LIMIT_ADJACENT
                    if modify:
                        self.modified_grid[x][y] = "L"
                        has_modified = True

                elif self.is_seat_empty(original_grid[x][y]):
                    if in_sight:
                        modify = self.get_occupied_seats_in_sight(x, y, original_grid) < 1
                    else:
                        modify = self.get_occupied_seats_adjacent(x, y, original_grid) < 1
                    if modify:
                        self.modified_grid[x][y] = "#"
                        has_modified = True

        return has_modified

    def get_occupied_seats_in_sight(self, x: int, y: int, grid: list) -> int:
        occupied_seats = 0
        for x_dir, y_dir in self.DIRECTIONS.values():
            next_x, next_y = (x + x_dir, y + y_dir)
            while self.is_within_column(next_x) and self.is_within_row(next_y):
                current_seat = grid[next_x][next_y]
                if self.is_seat_occupied(current_seat):
                    occupied_seats += 1
                    break

                if self.is_seat_empty(current_seat):
                    break

                next_x += x_dir
                next_y += y_dir

        return occupied_seats

    @staticmethod
    def get_occupied_seats(grid: list) -> int:
        return sum([len([seat for seat in row if seat == "#"]) for row in grid])

    @staticmethod
    def is_seat_occupied(seat: str) -> bool:
        return seat == "#"

    @staticmethod
    def is_seat_empty(seat: str) -> bool:
        return seat == "L"

    def is_within_column(self, number: int) -> bool:
        return 0 <= number < self.column_length

    def is_within_row(self, number: int) -> bool:
        return 0 <= number < self.row_length

    def get_occupied_seats_adjacent(self, x_pos: int, y_pos: int, grid: list) -> int:
        occupied_seats = [
            (x, y)
            for (x, y) in self.DIRECTIONS.values()
            if self.is_within_column(x + x_pos)
            and self.is_within_row(y + y_pos)
            and self.is_seat_occupied(grid[x + x_pos][y + y_pos])
        ]

        return len(occupied_seats)

    @staticmethod
    def load_input() -> list:
        list_input = []
        with open("input.txt", encoding="utf-8") as file:
            for line in file:
                list_input.append([*line.rstrip()])
        return list_input


day = Day11()
print(f"Result part 1: {day.part_one()}")
print(f"Result part 2: {day.part_two()}")
