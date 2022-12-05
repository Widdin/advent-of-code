class Day03:

    def __init__(self):
        self.puzzle_input = self.load_input()

    def part_one(self) -> int:
        total_letter_sum = 0
        for rucksack in self.puzzle_input:
            compartment_1 = rucksack[:len(rucksack)//2]
            compartment_2 = rucksack[len(rucksack)//2:]

            intersection = set(compartment_1).intersection(compartment_2)

            total_letter_sum += self.letter_to_number(letter=list(intersection)[0])

        return total_letter_sum

    def part_two(self) -> int:
        total_letter_sum = 0
        for rucksack in self.puzzle_input[::3]:
            index = self.puzzle_input.index(rucksack)
            intersection = set(self.puzzle_input[index]).intersection(self.puzzle_input[index + 1]).intersection(self.puzzle_input[index + 2])

            total_letter_sum += self.letter_to_number(letter=list(intersection)[0])

        return total_letter_sum

    @staticmethod
    def letter_to_number(letter: str) -> int:
        if letter.islower():
            return ord(letter) - ord('a') + 1
        return ord(letter) - 38

    @staticmethod
    def load_input() -> list:
        list_input = []
        with open("input.txt") as file:
            for line in file:
                list_input.append(line.rstrip())

        return list_input


day = Day03()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
