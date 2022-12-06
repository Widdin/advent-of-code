class Day06:

    def __init__(self):
        self.puzzle_input = self.load_input()

    def part_one(self) -> int:
        return self.get_start_of_packet_marker(distinct_characters=4, input=self.puzzle_input)

    def part_two(self) -> int:
        return self.get_start_of_packet_marker(distinct_characters=14, input=self.puzzle_input)

@staticmethod
def get_start_of_packet_marker(distinct_characters: int, input: list) -> int:
    for index, _ in enumerate(input):
        range = input[index:index + distinct_characters]

        if len(set(range)) == len(range):
            return (index + distinct_characters)

    @staticmethod
    def load_input() -> list:
        with open("input.txt") as file:
            for line in file:
                return list(line.rstrip())


day = Day06()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
