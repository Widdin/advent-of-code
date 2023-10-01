from collections import defaultdict, Counter


class Day10:
    def __init__(self):
        self.puzzle_input = self.load_input()
        self.memoize = {}

    def part_one(self) -> int:
        charging_outlet, built_in_adapter = 0, max(self.puzzle_input) + 3
        self.puzzle_input.extend([charging_outlet, built_in_adapter])
        self.puzzle_input.sort()

        # Differences between each element
        differences = [self.puzzle_input[i] - self.puzzle_input[i - 1] for i in range(1, len(self.puzzle_input))]
        difference_counts = Counter(differences)

        number = 1
        for occurrences in difference_counts.values():
            number *= occurrences

        return number

    def part_two(self) -> int:
        self.puzzle_input.reverse()
        connected_adapters = self.get_connected_adapters(self.puzzle_input)
        return self.get_distinct_ways(connected_adapters, max(self.puzzle_input), min(self.puzzle_input))

    @staticmethod
    def get_connected_adapters(puzzle_input: list) -> defaultdict(list):
        adapters = defaultdict(list)
        for i in range(len(puzzle_input)):
            for j in range(i + 1, len(puzzle_input)):
                if (puzzle_input[i] - 3) <= puzzle_input[j] <= puzzle_input[i]:
                    adapters[puzzle_input[i]].append(puzzle_input[j])
        return adapters

    def get_distinct_ways(self, adapters: defaultdict(list), adapter: int, min: int) -> int:
        if adapter == min:
            return 1

        if adapter in self.memoize:
            return self.memoize[adapter]

        count = 0
        for next_adapter in adapters[adapter]:
            count += self.get_distinct_ways(adapters, next_adapter, min)

        self.memoize[adapter] = count
        return count

    @staticmethod
    def load_input() -> list:
        list_input = []
        with open("input.txt") as file:
            for line in file:
                list_input.append(int(line.rstrip()))
        return list_input


day = Day10()
print(f"Result part 1: {day.part_one()}")
print(f"Result part 2: {day.part_two()}")
