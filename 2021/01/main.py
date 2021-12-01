class Day01:

    def __init__(self):
        self.puzzle_input = self.load_input()

    def part_one(self):
        previous_number = self.puzzle_input[0]
        increased = 0

        for number in self.puzzle_input:
            if number > previous_number:
                increased += 1

            previous_number = number

        return increased

    def part_two(self):
        increased = 0

        for index, number in enumerate(self.puzzle_input):
            if not index + 3 > len(self.puzzle_input) - 1:

                window_one = 0
                window_two = 0

                for i in range(0, 3):
                    window_one += self.puzzle_input[index + i]
                    window_two += self.puzzle_input[index + i + 1]

                if window_two > window_one:
                    increased += 1

        return increased

    @staticmethod
    def load_input():
        list_input = []
        with open("input.txt") as file:
            for line in file:
                list_input.append(int(line.rstrip()))
        return list_input


day1 = Day1()
print(f'Result part 1: {day1.part_one()}')
print(f'Result part 2: {day1.part_two()}')
