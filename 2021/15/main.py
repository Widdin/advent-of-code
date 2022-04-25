from collections import deque


class Day15:

    def __init__(self):
        self.rows = [-1, 0, 0, 1]
        self.cols = [0, -1, 1, 0]

        self.row_length = 0
        self.column_length = 0

        self.start = Point(0, 0)

    def part_one(self) -> int:
        return self.dijkstra(self.get_puzzle_input(full_map=False), self.start)

    def part_two(self) -> int:
        return self.dijkstra(self.get_puzzle_input(full_map=True), self.start)

    def dijkstra(self, mat, start):
        self.row_length = len(mat)
        self.column_length = len(mat[0])

        for x in range(len(mat)):
            for y in range(len(mat[x])):
                mat[x][y] = Vertex(Point(x, y), 0, mat[x][y], False)

        mat[start.x][start.y].weight = 0

        queue = deque()
        queue.append(mat[start.x][start.y])

        while queue:
            current = queue.popleft()

            if current.visited:
                continue

            current.visited = True

            for i in range(4):
                row = current.point.x + self.rows[i]
                col = current.point.y + self.cols[i]

                if self.is_within_matrix(row, col):
                    new_dist = current.dist + mat[row][col].weight

                    if mat[row][col].dist == 0:
                        mat[row][col].dist = new_dist
                    elif mat[row][col].dist > new_dist:
                        mat[row][col].dist = new_dist
                        mat[row][col].visited = False

                    queue.append(mat[row][col])

        return mat[-1][-1].dist

    def is_within_matrix(self, row, column):
        return (0 <= row < self.row_length) and (0 <= column < self.column_length)

    @staticmethod
    def pretty_print_matrix(mat):
        for row in mat:
            print(["{:02d}".format(vertex.dist) for vertex in row])

    @staticmethod
    def get_puzzle_input(full_map: bool) -> list:
        lst = []
        with open("input.txt") as file:
            for line in file:
                numbers = list(map(int, line.rstrip()))
                if full_map:
                    big_map_row = []
                    for i in range(5):
                        big_map_row += [number + i if number + i <= 9 else ((number + i) % 10) + 1 for number in numbers]
                    numbers = big_map_row
                lst.append(numbers)

        if full_map:
            big_map_col = []
            for i in range(5):
                for row in lst:
                    big_map_col.append([number + i if number + i <= 9 else ((number + i) % 10) + 1 for number in row])
            lst = big_map_col

        return lst


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vertex:
    def __init__(self, point, dist, weight, visited):
        self.point = point
        self.dist = dist
        self.weight = weight
        self.visited = visited


DAY = Day15()
print(f'Result part 1: {DAY.part_one()}')
print(f'Result part 2: {DAY.part_two()}')
