class Day01:

    def __init__(self):
        self.puzzle_input = self.load_input()

    def part_one(self) -> int:
        return self.puzzle_input[0]

    def part_two(self) -> int:
        return sum(self.puzzle_input[0:3])

    @staticmethod
    def load_input() -> list:
        list_input = []
        with open("input.txt") as file:
            elf_calories = 0
            for line in file:
                if not line.rstrip():
                    list_input.append(elf_calories)
                    elf_calories = 0
                else:
                    elf_calories += int(line.rstrip())

        list_input.sort(reverse=True)
        return list_input


day = Day01()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
