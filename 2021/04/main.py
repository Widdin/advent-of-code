class Day04:

    def __init__(self):
        self.puzzle_input = self.get_puzzle_input()
        self.numbers = self.get_numbers(self.puzzle_input)
        self.boards = self.get_boards(self.puzzle_input)
        self.winning_boards_sum = self.get_winning_boards_sum()

    def part_one(self) -> int:
        return self.winning_boards_sum[0]

    def part_two(self) -> int:
        return self.winning_boards_sum[-1]

    def get_winning_boards_sum(self) -> list:
        winning_boards_sum = []

        for i in range(1, len(self.numbers)):
            numbers = self.numbers[:i]

            for index, board in enumerate(self.boards):
                if self.is_bingo(numbers, board):
                    self.boards.pop(index)

                    unmarked_sum = self.get_sum_unmarked(numbers, board) * int(numbers[-1])
                    winning_boards_sum.append(unmarked_sum)

        return winning_boards_sum

    def is_bingo(self, numbers, board) -> bool:
        if any([self.is_cols_bingo(numbers, board),
                self.is_rows_bingo(numbers, board)]):
            return True
        return False

    @staticmethod
    def get_sum_unmarked(numbers, board) -> int:
        total = 0
        for row in board:
            for num in row:
                if num not in numbers:
                    total += int(num)
        return total

    @staticmethod
    def is_rows_bingo(numbers: list, board: list) -> bool:
        for row in board:
            if set(row).issubset(set(numbers)):
                return True
        return False

    @staticmethod
    def is_cols_bingo(numbers: list, board: list) -> bool:
        for col in zip(*board):
            col = list(col)
            if set(col).issubset(set(numbers)):
                return True
        return False

    @staticmethod
    def get_puzzle_input() -> list:
        list_input = []
        with open("input.txt") as file:
            for line in file:
                list_input.append((line.rstrip()))
        return list_input

    @staticmethod
    def get_numbers(list_input) -> list:
        return list_input.pop(0).split(',')

    def get_boards(self, list_input) -> list:
        lst = self.remove_empty_lines(list_input)
        lst = self.split_into_boards(lst)
        lst = self.split_into_chunks(lst, size=5)
        return lst

    @staticmethod
    def remove_empty_lines(list_input) -> list:
        return [x for x in list_input if x]

    @staticmethod
    def split_into_boards(list_input) -> list:
        return [word for line in list_input for word in [line.split()]]

    @staticmethod
    def split_into_chunks(list_input, size) -> list:
        lst = []
        for i in range(0, len(list_input), size):
            lst.append(list_input[i:i + size])
        return lst


day = Day04()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
