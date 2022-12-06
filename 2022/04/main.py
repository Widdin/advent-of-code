class Day04:

    def __init__(self):
        self.puzzle_input = self.load_input()

    def part_one(self) -> int:
        return self.get_containing_pairs(overlap=False)

    def part_two(self) -> int:
        return self.get_containing_pairs(overlap=True)

    def get_containing_pairs(self, overlap: bool) -> int:
        num_pairs = 0
        for pair in self.puzzle_input:
            pair_1, pair_2 = [i.split("-") for i in pair.split(",")]

            pair_1_range = [i for i in range(int(pair_1[0]), int(pair_1[1]) + 1)]
            pair_2_range = [i for i in range(int(pair_2[0]), int(pair_2[1]) + 1)]

            if overlap and set(pair_1_range).intersection(pair_2_range):
                num_pairs += 1
            elif set(pair_1_range).issubset(pair_2_range) or set(pair_1_range).issuperset(pair_2_range):
                num_pairs += 1

        return num_pairs

    @staticmethod
    def load_input() -> list:
        list_input = []
        with open("input.txt") as file:
            for line in file:
                list_input.append(line.rstrip())

        return list_input


day = Day04()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
