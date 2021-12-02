class Day02:

    def __init__(self):
        self.puzzle_input = self.load_input()
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def reset_position(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def part_one(self) -> int:
        self.reset_position()

        for command in self.puzzle_input:
            direction, value = command.split()
            value = int(value)

            if direction == 'forward':
                self.horizontal += value

            elif direction == 'up':
                self.depth -= value

            elif direction == 'down':
                self.depth += value

        return self.horizontal * self.depth

    def part_two(self) -> int:
        self.reset_position()

        for command in self.puzzle_input:
            direction, value = command.split(' ')
            value = int(value)

            if direction == 'forward':
                self.horizontal += value
                self.depth += self.aim * value

            elif direction == 'up':
                self.aim -= value

            elif direction == 'down':
                self.aim += value

        return self.horizontal * self.depth

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
