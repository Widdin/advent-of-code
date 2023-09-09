class Day03:

    def __init__(self):
        self.puzzle_input = self.load_input()
        self.map_width = len(self.puzzle_input[0])
        self.map_height = len(self.puzzle_input)

    def part_one(self) -> int:
        return self.get_trees_in_slope(3, 1)

    def part_two(self) -> int:
        slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
        sum = 1
        for slope in slopes:
            sum *= self.get_trees_in_slope(*slope)
        return sum

    def get_trees_in_slope(self, right, down):
        pos_x, pos_y, trees = (0, 0, 0)
        while pos_y < self.map_height - 1:
            pos_x = (pos_x + right) % self.map_width
            pos_y += down

            current_pos = self.puzzle_input[pos_y][pos_x]
            if self.is_tree(current_pos):
                trees += 1

        return trees
    
    @staticmethod
    def is_tree(point):
        return point == '#'

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
