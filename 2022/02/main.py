import collections


class Day02:

    def __init__(self):
        self.puzzle_input = self.load_input()

    def part_one(self) -> int:
        return self.calculate_score(elf_strategy=False)

    def part_two(self) -> int:
        return self.calculate_score(elf_strategy=True)

    @staticmethod
    def shape_to_score(shape: str) -> int:
        return {'A': 1, 'B': 2, 'C': 3}[shape]

    @staticmethod
    def XYZ_to_ABC(letter: str) -> str:
        return {'X': 'A', 'Y': 'B', 'Z': 'C'}[letter]

    def calculate_score(self, elf_strategy: bool) -> int:
        wins_to = {'A': 'B', 'B': 'C', 'C': 'A'}

        round_counter = collections.Counter(self.puzzle_input)

        total_score = 0
        for round, times in round_counter.items():
            opponent, you = round.split(" ")

            if elf_strategy:
                if you == 'X':
                    you = (dict([(value, key) for key, value in wins_to.items()]))[opponent]
                elif you == 'Y':
                    you = opponent
                elif you == 'Z':
                    you = wins_to[opponent]
            else:
                you = self.XYZ_to_ABC(letter=you)

            if you == wins_to[opponent]:
                total_score += ((self.shape_to_score(shape=you) + 6) * times)
            elif opponent == wins_to[you]:
                total_score += ((self.shape_to_score(shape=you) + 0) * times)
            else:
                total_score += ((self.shape_to_score(shape=you) + 3) * times)

        return total_score

    @staticmethod
    def load_input() -> list:
        list_input = []
        with open("input.txt") as file:
            for line in file:
                list_input.append(line.rstrip())

        return list_input


day = Day02()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
