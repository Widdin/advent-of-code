from collections import defaultdict


class Day10:

    def __init__(self):
        self.puzzle_input = self.load_input()

    def part_one(self) -> int:
        cycles, _ = self.do_stuff()
        signal_strengths = [cycles[i] * i for i in [20, 60, 100, 140, 180, 220]]
        return sum(signal_strengths)

    def part_two(self) -> None:
        _, all_CRT_rows = self.do_stuff()
        return '\n' + '\n'.join(' '.join(map(str, sublist)) for sublist in all_CRT_rows)

    def do_stuff(self) -> None:
        cycles = defaultdict(int)
        x_register = 1
        current_cycle = 0

        current_CRT_row = []
        all_CRT_rows = []

        for line in self.puzzle_input:
            if line == 'noop':
                current_cycle += 1
                cycles[current_cycle] = x_register

                pixel = self.draw_pixel(cycle=current_cycle, x=x_register)
                current_CRT_row.append(pixel)

                if len(current_CRT_row) % 40 == 0:
                    all_CRT_rows.append(current_CRT_row)
                    current_CRT_row = []

            else:
                _, num = line.split()
                for _ in range(2):
                    current_cycle += 1
                    cycles[current_cycle] = x_register

                    pixel = self.draw_pixel(cycle=current_cycle, x=x_register)
                    current_CRT_row.append(pixel)

                    if len(current_CRT_row) % 40 == 0:
                        all_CRT_rows.append(current_CRT_row)
                        current_CRT_row = []

                x_register += int(num)

        return cycles, all_CRT_rows

    @staticmethod
    def draw_pixel(cycle, x) -> str:
        if cycle % 40 in [x, x + 1, x + 2]:
            return "#"
        return "."

    @staticmethod
    def load_input() -> list:
        list_input = []
        with open("input.txt") as file:
            for line in file:
                list_input.append(line.rstrip())

        return list_input


day = Day10()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
