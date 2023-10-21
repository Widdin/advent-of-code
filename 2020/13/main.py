from itertools import count
from math import ceil


class Day13:
    def __init__(self):
        self.puzzle_input = self.load_input()

    def part_one(self) -> int:
        earliest_timestamp = int(self.puzzle_input[0])
        bus_ids = [int(x) for x in self.puzzle_input[1].split(",") if self.is_bus_in_service(x)]
        departure, bus_id = min((ceil(earliest_timestamp / x) * x, int(x)) for x in bus_ids)

        return (departure - earliest_timestamp) * bus_id

    def part_two(self) -> int:
        buses = [
            (int(bus_id), offset)
            for offset, bus_id in enumerate(self.puzzle_input[1].split(","))
            if self.is_bus_in_service(bus_id)
        ]

        step, timestamp = 1, 0
        for bus_id, offset in buses:
            for current_timestamp in count(timestamp, step):
                if (current_timestamp + offset) % bus_id == 0:
                    timestamp = current_timestamp
                    break
            step *= bus_id
        return timestamp

    @staticmethod
    def is_bus_in_service(bus_id):
        return bus_id.isdigit()

    @staticmethod
    def load_input() -> list:
        list_input = []
        with open("input.txt", encoding="utf-8") as file:
            for line in file:
                list_input.append(line.rstrip())
        return list_input


day = Day13()
print(f"Result part 1: {day.part_one()}")
print(f"Result part 2: {day.part_two()}")
