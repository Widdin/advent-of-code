class Day06:

    def __init__(self):
        self.puzzle_input = self.get_puzzle_input()
        self.fish_stages = self.get_fish_stages()

    def part_one(self) -> int:
        return self.get_fishes(days=80)

    def part_two(self) -> int:
        return self.get_fishes(days=256)

    def get_fish_stages(self) -> list:
        fish_stage = [0] * 9
        for number in self.puzzle_input:
            fish_stage[number] += 1
        return fish_stage

    def get_fishes(self, days) -> int:
        fish_stage = self.fish_stages.copy()
        for i in range(days):
            new_fishes = fish_stage.pop(0)
            fish_stage.append(new_fishes)
            fish_stage[6] += new_fishes

        return sum(fish_stage)

    @staticmethod
    def get_puzzle_input() -> list:
        with open("input.txt") as file:
            for line in file:
                return list(map(int, line.split(',')))


day = Day06()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
