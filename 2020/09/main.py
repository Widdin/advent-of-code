class Day09:
    def __init__(self):
        self.puzzle_input = self.load_input()
        self.invalid_number = None

    def part_one(self) -> int:
        self.invalid_number = self.find_invalid_number(self.puzzle_input, preample=25)
        return self.invalid_number

    def part_two(self) -> int:
        return self.find_contiguous_set(self.puzzle_input, self.invalid_number)

    @staticmethod
    def find_invalid_number(puzzle_input: list, preample: int) -> int:
        for i in range(preample, len(puzzle_input)):
            previous_numbers = puzzle_input[i - preample : i]
            current_number = puzzle_input[i]

            num_pair_found = False
            for num in previous_numbers:
                num_to_find = current_number - num

                if num_to_find in previous_numbers and num_to_find != num:
                    num_pair_found = True
                    break

            if not num_pair_found:
                return current_number

    @staticmethod
    def find_contiguous_set(puzzle_input: list, invalid_number: int) -> int:
        for i in range(len(puzzle_input)):
            for y in range(1, len(puzzle_input)):
                if sum(puzzle_input[i:y]) > invalid_number:
                    break
                if sum(puzzle_input[i:y]) == invalid_number:
                    return min(puzzle_input[i:y]) + max(puzzle_input[i:y])

    @staticmethod
    def load_input() -> list:
        list_input = []
        with open("input.txt") as file:
            for line in file:
                list_input.append(int(line.rstrip()))
        return list_input


day = Day09()
print(f"Result part 1: {day.part_one()}")
print(f"Result part 2: {day.part_two()}")
