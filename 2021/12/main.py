from collections import defaultdict


class Day12:

    def __init__(self):
        self.puzzle_input = self.get_puzzle_input()
        self.graph = self.get_connected_caves()
        self.paths = []

    def part_one(self) -> int:
        graph = self.graph.copy()
        self.get_cave_paths(graph, 'start', [], single=True)
        return len(self.paths)

    def part_two(self) -> int:
        graph = self.graph.copy()
        self.get_cave_paths(graph, 'start', [], single=False)
        return len(self.paths)

    def get_connected_caves(self) -> defaultdict:
        data = self.puzzle_input.copy()
        graph = defaultdict(list)

        for line in data:
            path_from, path_to = line.split('-')

            graph[path_from].append(path_to)

            if path_from != 'start':
                graph[path_to].append(path_from)

        return graph

    def get_cave_paths(self, graph, current_cave, path, single) -> None:
        path.append(current_cave)

        if current_cave == 'end':
            if path not in self.paths:
                self.paths.append(path)
            return

        for i in graph[current_cave]:
            path_copy = path.copy()

            if i == 'start' and 'start' in path_copy:
                continue

            # Already visited
            if i.islower() and i in path_copy:

                # P1 or P2
                if single or self.visited_twice(path_copy):
                    continue

            # No return back
            if len(graph[current_cave]) == 1 and path_copy[-2].islower() and graph[current_cave] == path_copy[-2]:
                continue

            self.get_cave_paths(graph, i, path_copy, single)

    @staticmethod
    def visited_twice(path) -> bool:
        for cave in path:
            if cave.islower() and path.count(cave) == 2:
                return True
        return False

    @staticmethod
    def get_puzzle_input() -> list:
        lst = []
        with open("input.txt") as file:
            for line in file:
                lst.append(line.rstrip())
        return lst


day = Day12()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
