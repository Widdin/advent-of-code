class Day05:

    def __init__(self):
        self.puzzle_input = self.load_input()

    def part_one(self) -> str:
        return self.move_crates(multiple_at_once=False)

    def part_two(self) -> str:
        return self.move_crates(multiple_at_once=True)

    @staticmethod
    def remove_nth_element(start: int, n: int, elements: str) -> str:
        elements_list = list(elements)
        del elements_list[start::n]

        return ''.join(elements_list)

    @staticmethod
    def split_nth_element(n: int, elements: list) -> list:
        return [elements[i:i+n] for i in range(0, len(elements), n)]

    def sanitize_input(self, input: str) -> str:
        input_nth = self.remove_nth_element(start=3, n=4, elements=input)
        return self.split_nth_element(n=3, elements=input_nth)

    @staticmethod
    def get_top_crates(crates: dict) -> str:
        top_crates = []
        for key in sorted(crates.keys()):
            top_crates.append((crates[key][0])[1])

        return "".join(top_crates)

    def move_crates(self, multiple_at_once: bool) -> str:
        crates = {}
        starting_crates = True

        for line in self.puzzle_input:
            input = self.sanitize_input(input=line)

            if starting_crates:
                index = 1
                for crate in input:
                    crate = crate.strip()
                    if crate and not crate.isdigit():
                        crates.setdefault(index, []).append(crate)

                    index += 1

                if not line:
                    starting_crates = False
                    continue

            elif not starting_crates:
                _, move, _, start, _, to = line.split(" ")
                move, start, to = int(move), int(start), int(to)

                if multiple_at_once:
                    elements_to_move = crates[start][:move]
                    del crates[start][:move]
                    crates[to] = elements_to_move + crates[to]
                else:
                    for _ in range(move):
                        first_element = crates[start].pop(0)
                        crates[to].insert(0, first_element)

        return self.get_top_crates(crates=crates)

    @staticmethod
    def load_input() -> list:
        list_input = []
        with open("input.txt") as file:
            for line in file:
                list_input.append(line.rstrip('\n'))

        return list_input


day = Day05()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
