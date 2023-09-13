import math

class Day05:

    def __init__(self):
        self.puzzle_input = self.load_input()

    def part_one(self) -> int:
        return max(self.get_seat_ids(self.puzzle_input))

    def part_two(self) -> int:
        seat_ids = self.get_seat_ids(self.puzzle_input)
        return self.get_missing_seat(seat_ids)

    def get_seat_ids(self, boarding_passes) -> list:
        seat_ids = set()

        for boarding_pass in boarding_passes:
            row = self.get_region(boarding_pass[:7], 0, 127, "F", "B")
            column = self.get_region(boarding_pass[7:], 0, 7, "L", "R")
            seat_id = row * 8 + column
            seat_ids.add(seat_id)

        return seat_ids
    
    @staticmethod
    def get_missing_seat(seat_ids):
        for id in range(min(seat_ids), max(seat_ids) + 1):
            if id not in seat_ids:
                return id

    @staticmethod
    def get_region(letters, low, high, region_lower, region_upper) -> int:
        for letter in letters:
            if letter == region_lower:
                high = math.floor((high + low) / 2)

            elif letter == region_upper:
                low = math.ceil((high + low) / 2)

        return low

    @staticmethod
    def load_input() -> list:
        list_input = []
        with open("input.txt") as file:
            for line in file:
                list_input.append(line.rstrip())
        return list_input


day = Day05()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
