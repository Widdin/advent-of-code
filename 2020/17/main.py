class Day17:
    def __init__(self):
        self.puzzle_input = self.load_input()
        self.cycles = 6

    def part_one(self) -> int:
        cubes = self.get_active_cubes(self.puzzle_input)

        for _ in range(self.cycles):
            cubes = self.simulate(cubes, dimensions=3)

        return len(cubes)

    def part_two(self) -> int:
        cubes = self.get_active_cubes(self.puzzle_input)

        for _ in range(self.cycles):
            cubes = self.simulate(cubes, dimensions=4)

        return len(cubes)

    @staticmethod
    def get_neighbors(cube, dimensions) -> set:
        neighbors = set()
        x, y, z, w = cube

        for delta_x in range(-1, 2):
            for delta_y in range(-1, 2):
                for delta_z in range(-1, 2):
                    if dimensions == 4:
                        for delta_w in range(-1, 2):
                            neighbor = (x + delta_x, y + delta_y, z + delta_z, w + delta_w)
                            neighbors.add(neighbor)
                    else:
                        neighbor = (x + delta_x, y + delta_y, z + delta_z, w)
                        neighbors.add(neighbor)

        neighbors.remove(cube)
        return neighbors

    @staticmethod
    def get_active_cubes(grid) -> set:
        active_cubes = set()

        for x, _ in enumerate(grid):
            for y, _ in enumerate(grid):
                if grid[x][y] == "#":
                    active_cubes.add((x, y, 0, 0))

        return active_cubes

    def simulate(self, cubes, dimensions) -> set:
        new_cubes = set()
        could_activate = {}

        for cube in cubes:
            neighbors = self.get_neighbors(cube, dimensions)
            active_neighbors_count = 0

            for neighbor in neighbors:
                if neighbor in cubes:
                    active_neighbors_count += 1
                else:
                    if neighbor not in could_activate:
                        could_activate[neighbor] = 0
                    could_activate[neighbor] += 1

            if active_neighbors_count in (2, 3):
                new_cubes.add(cube)

        for cube, count in could_activate.items():
            if count == 3:
                new_cubes.add(cube)

        return new_cubes

    @staticmethod
    def load_input() -> list:
        list_input = []
        with open("input.txt", encoding="utf-8") as file:
            for line in file:
                list_input.append(list(line.rstrip()))
        return list_input


day = Day17()
print(f"Result part 1: {day.part_one()}")
print(f"Result part 2: {day.part_two()}")
