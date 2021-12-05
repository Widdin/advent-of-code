import collections


class Day05:

    def __init__(self):
        self.puzzle_input = self.get_puzzle_input()

    def part_one(self) -> int:
        diagram = self.get_diagram()
        return self.get_sum_overlap(diagram)

    def part_two(self) -> int:
        diagram = self.get_diagram(diagonal=True)
        return self.get_sum_overlap(diagram)

    def get_diagram(self, diagonal: bool = False) -> dict:
        diagram = collections.defaultdict(int)

        for coords in self.puzzle_input:
            x1, y1 = (int(x) for x in coords[0].split(","))
            x2, y2 = (int(x) for x in coords[1].split(","))

            if x1 == x2:
                for i in range(min(y1, y2), max(y1, y2) + 1):
                    diagram["{0},{1}".format(x1, i)] += 1

            elif y1 == y2:
                for i in range(min(x1, x2), max(x1, x2) + 1):
                    diagram["{0},{1}".format(i, y1)] += 1

            elif diagonal and abs(x1 - x2) == abs(y1 - y2):
                direction_x = 1 if x1 < x2 else -1
                direction_y = 1 if y1 < y2 else -1
                for n in range(abs(x1 - x2) + 1):
                    diagram["{0},{1}".format(x1 + n * direction_x, y1 + n * direction_y)] += 1

        return diagram

    @staticmethod
    def get_sum_overlap(diagram: dict) -> int:
        return sum(1 for value in diagram.values() if value >= 2)

    @staticmethod
    def get_puzzle_input() -> list:
        list_input = []
        with open("input.txt") as file:
            for line in file:
                list_input.append((line.rstrip().split(" -> ")))
        return list_input


day = Day05()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
