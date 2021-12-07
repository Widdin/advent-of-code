class Day07:

    def __init__(self):
        self.puzzle_input = self.get_puzzle_input()

    def part_one(self) -> int:
        return self.get_fuel_cost(constant_rate=True)

    def part_two(self) -> int:
        return self.get_fuel_cost(constant_rate=False)

    def get_fuel_cost(self, constant_rate: bool) -> int:
        positions = self.puzzle_input.copy()

        min_fuel_cost = 1e9
        for index in range(min(positions), max(positions)):

            fuel_cost = 0
            for position in positions:
                distance = self.get_distance(position, index)

                if not constant_rate:
                    distance += self.get_inf_series(distance - 1)

                fuel_cost += distance

            if fuel_cost < min_fuel_cost:
                min_fuel_cost = fuel_cost

        return min_fuel_cost

    def get_fuel_cost_oneliner(self):
        return int(min(list(map(lambda i: sum(map(lambda n: (abs(n - i) + ((abs(n - i) - 1) * ((abs(n - i) - 1) + 1)) * 0.5), self.get_puzzle_input())), range(max(self.get_puzzle_input()) + 1)))))

    @staticmethod
    def get_distance(index, position):
        return abs(position - index)

    @staticmethod
    def get_inf_series(distance):
        return (distance * (distance + 1)) // 2

    @staticmethod
    def get_puzzle_input() -> list:
        with open("input.txt") as file:
            for line in file:
                return list(map(int, line.split(',')))


day = Day07()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
