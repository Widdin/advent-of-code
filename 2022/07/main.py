from collections import defaultdict


class Day07:

    def __init__(self):
        self.puzzle_input = self.load_input()
        self.filetree = self.get_filetree(input=self.puzzle_input)

    def part_one(self) -> int:
        return sum([i for i in self.filetree.values() if i <= 100000])

    def part_two(self) -> int:
        MAX_SPACE, MIN_SPACE = 70000000, 30000000
        USED_SPACE = self.get_filesize_used(filetree=self.filetree)
        SPACE_AVAILABLE = MAX_SPACE - USED_SPACE
        SPACE_NEEDED = MIN_SPACE - SPACE_AVAILABLE

        return min(i for i in list(self.filetree.values()) if i > SPACE_NEEDED)

    @staticmethod
    def get_filesize_used(filetree: defaultdict(int)) -> int:
        return (list(filetree.values()))[0]

    @staticmethod
    def get_filetree(input: list) -> defaultdict(int):
        filetree = defaultdict(int)

        current_dir = []
        for line in input:
            match line.strip().replace("$", "").split():
                case ["cd", "/"]:
                    current_dir.append("/")

                case ["cd", ".."]:
                    current_dir.pop()

                case ["cd", folder]:
                    current_dir.append(folder + "/")

                case [filesize, _] if filesize.isdigit():
                    parent_dirs = len(current_dir) - 1
                    for i in range(0, parent_dirs + 1):
                        filepath = "".join(current_dir[0:i+1])
                        filetree[filepath] += int(filesize)

        return filetree

    @staticmethod
    def load_input() -> list:
        list_input = []
        with open("input.txt") as file:
            for line in file:
                list_input.append(line.rstrip())

        return list_input


day = Day07()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
