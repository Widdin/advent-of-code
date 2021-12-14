class Day13:

    def __init__(self):
        self.puzzle_input = self.get_puzzle_input()

    def part_one(self) -> int:
        return self.fold_paper(once=True)

    def part_two(self) -> int:
        paper = self.fold_paper()
        for line in paper:
            print(line)
        return paper

    def fold_paper(self, once: bool = False):
        data = self.puzzle_input.copy()

        coords, folds = self.get_coords_and_folds(data)
        x_max, y_max = self.get_x_and_y_max(coords)
        paper = self.get_empty_paper(x_max, y_max)
        self.fill_with_coords(coords, paper)

        for fold in folds:
            axis, num = fold
            paper = self.fold_on(axis, int(num), paper)

            if once:
                return self.get_visible_dots(paper)

        return paper

    @staticmethod
    def get_coords_and_folds(data) -> (list, list):
        coords = []
        folds = []

        for line in data:
            if ',' in line:
                coords.append([int(x) for x in line.split(',')])
            elif line != '':
                folds.append(line.split()[-1].split('='))

        return coords, folds

    @staticmethod
    def get_x_and_y_max(coords) -> (int, int):
        x_max = y_max = 0

        for coord in coords:
            x, y = coord
            x_max = max(x, x_max)
            y_max = max(y, y_max)

        return x_max, y_max

    @staticmethod
    def get_empty_paper(x_max, y_max) -> list:
        return [[0] * (x_max + 1) for _ in range(y_max + 1)]

    @staticmethod
    def fill_with_coords(coords, paper) -> None:
        for coord in coords:
            x, y = coord
            paper[y][x] = 1

    @staticmethod
    def get_visible_dots(mat) -> int:
        return sum([sum(line) for line in mat])

    @staticmethod
    def fold_on(axis, number, paper) -> list:
        folded_paper = []

        if axis == 'x':  # Left
            right_side = [x[number + 1:] for x in paper]
            for line in right_side:
                line.reverse()

            left_side = [x[:number] for x in paper]

            for right, left in zip(right_side, left_side):
                folded_paper.append([1 if x or y > 0 else 0 for x, y in zip(right, left)])

        elif axis == 'y':  # Up
            lower_half = paper[number + 1:]
            lower_half.reverse()

            upper_half = paper[:number]

            for lower, top in zip(lower_half, upper_half):
                folded_paper.append([1 if x or y > 0 else 0 for x, y in zip(lower, top)])

        return folded_paper

    @staticmethod
    def get_puzzle_input() -> list:
        lst = []
        with open("input.txt") as file:
            for line in file:
                lst.append(line.rstrip())
        return lst


day = Day13()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
