class Day08:
    def __init__(self):
        self.puzzle_input = self.load_input()
        self.puzzle_input_copy = self.load_input()

    def part_one(self) -> int:
        return self.run_boot_code(self.create_deep_copy(self.puzzle_input))[0]

    def part_two(self) -> int:
        return self.repair_boot_code()

    def repair_boot_code(self):
        for index in range(len(self.puzzle_input)):
            puzzle_input = self.create_deep_copy(self.puzzle_input)

            swap_instruction = {"nop": "jmp", "jmp": "nop"}
            current_instruction = puzzle_input[index]["argument"]

            if current_instruction in swap_instruction.keys():
                puzzle_input[index]["argument"] = swap_instruction[current_instruction]

                accumulator, terminated = self.run_boot_code(puzzle_input)
                if terminated:
                    return accumulator

    @staticmethod
    def create_deep_copy(lst) -> list:
        return [dict(entry) for entry in lst]

    @staticmethod
    def run_boot_code(puzzle_input: list) -> (int, bool):
        index, accumulator = (0, 0)
        while True:
            if index > len(puzzle_input) - 1:
                return (accumulator, True)

            argument, number, executed = puzzle_input[index].values()

            if executed:
                return (accumulator, False)
            else:
                puzzle_input[index]["executed"] = True

            match argument:
                case "nop":
                    index += 1
                case "acc":
                    accumulator += number
                    index += 1
                case "jmp":
                    index += number

    @staticmethod
    def load_input() -> list:
        list_input = []
        with open("input.txt") as file:
            for line in file:
                argument, number = line.rstrip().split(" ")
                list_input.append({"argument": argument, "number": int(number), "executed": False})
        return list_input


day = Day08()
print(f"Result part 1: {day.part_one()}")
print(f"Result part 2: {day.part_two()}")
