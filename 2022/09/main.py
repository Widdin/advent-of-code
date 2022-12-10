from collections import defaultdict

import matplotlib.pylab as plt


class Node:

    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.pos_x, self.pos_y = x, y

    def set_xy(self, x: int, y: int) -> None:
        self.pos_x, self.pos_y = x, y

    def get_xy(self) -> tuple:
        return (self.pos_x, self.pos_y)

    def is_close_enough(self, node: 'Node') -> bool:
        return False if abs(node.pos_x - self.pos_x) > 1 or abs(node.pos_y - self.pos_y) > 1 else True

    def move_up(self, node: 'Node') -> bool:
        return True if node.pos_y > self.pos_y else False

    def move_right(self, node: 'Node') -> bool:
        return True if node.pos_x > self.pos_x else False

    def is_diagonal_movement(self, node: 'Node') -> bool:
        return True if abs(node.pos_x - self.pos_x) > 0 and abs(node.pos_y - self.pos_y) > 0 else False


class Day09:

    def __init__(self):
        self.puzzle_input = self.load_input()

    def part_one(self) -> int:
        tails = [Node()]
        return self.simulate_rope(tails=tails)

    def part_two(self) -> int:
        tails = [Node() for _ in range(9)]
        return self.simulate_rope(tails=tails)

    def simulate_rope(self, tails: list, plot: bool = False):
        tail_visited = defaultdict(int)
        tail_visited[(0, 0)] = 1

        if plot:
            all_tail_visited = defaultdict(list)

        head = Node()
        for line in self.puzzle_input:
            direction, steps = line.split()
            for _ in range(int(steps)):
                if direction == "R":
                    head.pos_x += 1

                if direction == "U":
                    head.pos_y += 1

                if direction == "L":
                    head.pos_x -= 1

                if direction == "D":
                    head.pos_y -= 1

                previous = Node(x=head.pos_x, y=head.pos_y)

                for index, tail in enumerate(tails):
                    if not tail.is_close_enough(previous):
                        move_up = tail.move_up(previous)
                        move_right = tail.move_right(previous)

                        if tail.is_diagonal_movement(previous):
                            tail.pos_y += 1 if move_up else -1
                            tail.pos_x += 1 if move_right else -1
                        else:
                            if tail.pos_x == previous.pos_x:
                                tail.pos_y += 1 if move_up else -1

                            if tail.pos_y == previous.pos_y:
                                tail.pos_x += 1 if move_right else -1

                    if index == (len(tails) - 1):
                        tail_visited[tail.get_xy()] += 1

                    if plot:
                        all_tail_visited[index].append(tail.get_xy())

                    previous.set_xy(x=tail.pos_x, y=tail.pos_y)

        if plot:
            self.plot_tails(tails=all_tail_visited)
        return len(list(tail_visited.keys()))

    @staticmethod
    def plot_tails(tails: defaultdict) -> None:
        fig, axs = plt.subplots(9)
        fig.set_size_inches(5, 25)
        fig.tight_layout()
        fig.subplots_adjust(hspace=0.25)

        for i, item in enumerate(tails.values()):
            x, y = zip(*item)
            axs[i].plot(0, 0, "g*")
            axs[i].plot(x, y, ".")
            axs[i].set_title(f'Tail {i+1}')
            axs[i].axis([-15, 15, -10, 15])

        fig.savefig("tails")

    @staticmethod
    def load_input() -> list:
        list_input = []
        with open("input.txt") as file:
            for line in file:
                list_input.append(line.rstrip())

        return list_input


day = Day09()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
