import math


class Day08:

    def __init__(self):
        self.puzzle_input = self.load_input()
        self.scenic_score, self.visible_trees = self.find_trees()

    def part_one(self) -> int:
        return self.visible_trees

    def part_two(self) -> int:
        return self.scenic_score

    def find_trees(self):
        visible_trees, scenic_score = 0, 0
        for x, row in enumerate(self.puzzle_input):
            for y, tree in enumerate(row):
                left, right, top, down = self.get_views(x=x, y=y, input=self.puzzle_input)

                if (self.is_visible(tree=tree, input=left)
                        or self.is_visible(tree=tree, input=right)
                        or self.is_visible(tree=tree, input=top)
                        or self.is_visible(tree=tree, input=down)):
                    visible_trees += 1

                viewing_distance = [
                    self.get_viewing_distance(tree=tree, input=right),
                    self.get_viewing_distance(tree=tree, input=reversed(left)),
                    self.get_viewing_distance(tree=tree, input=reversed(top)),
                    self.get_viewing_distance(tree=tree, input=down)
                ]

                if not self.is_edge(x=x, y=y, input=self.puzzle_input):
                    score = math.prod(map(int, [x for x in viewing_distance if x > 0]))
                    if score > scenic_score:
                        scenic_score = score

        return scenic_score, visible_trees

    @staticmethod
    def get_views(x: int, y: int, input: list) -> tuple:
        left = input[x][:y]
        right = input[x][y+1:]
        column = [i[y] for i in input]
        top = column[:x]
        down = column[x+1:]

        return (left, right, top, down)

    @staticmethod
    def is_edge(x: int, y: int, input: list) -> bool:
        return x in [0, len(input[0]) - 1] and y in [0, len(input) - 1]

    @staticmethod
    def is_visible(tree: int, input: list) -> bool:
        if all(i < tree for i in input):
            return True
        return False

    @staticmethod
    def get_viewing_distance(tree: int, input: list) -> int:
        trees = 0
        for num in input:
            trees += 1
            if num >= tree:
                break
        return trees

    @staticmethod
    def load_input() -> list:
        list_input = []
        with open("input.txt") as file:
            for line in file:
                list_input.append(line.rstrip())

        return list_input


day = Day08()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
