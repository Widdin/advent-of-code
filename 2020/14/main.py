from itertools import product


class Day14:
    def __init__(self):
        self.puzzle_input = self.load_input()

    def part_one(self) -> int:
        current_mask, memory = [], {}
        for line in self.puzzle_input:
            split = line.split(" ")

            if "mask" in split:
                current_mask = split[-1]
            else:
                key = int("".join(filter(str.isdigit, split[0])))
                value = self.decimal_to_binary(split[-1])

                value_masked = "".join(
                    [val if current_mask[i] == "X" else current_mask[i] for i, val in enumerate(value)]
                )

                memory[key] = self.binary_to_decimal(value_masked)

        return sum(memory.values())

    def part_two(self) -> int:
        current_mask, memory = [], {}
        for line in self.puzzle_input:
            split = line.split(" ")

            if "mask" in split:
                current_mask = split[-1]
            else:
                key = self.decimal_to_binary(int("".join(filter(str.isdigit, split[0]))))
                value = split[-1]

                key_masked = "".join(
                    [
                        current_mask[i] if current_mask[i] == "X" or current_mask[i] == "1" else val
                        for i, val in enumerate(key)
                    ]
                )

                masks = self.get_mask_combinations(key_masked)

                for mask in masks:
                    memory[self.binary_to_decimal(mask)] = int(value)

        return sum(memory.values())

    @staticmethod
    def decimal_to_binary(decimal: int) -> str:
        return f"{int(decimal):036b}"

    @staticmethod
    def binary_to_decimal(binary: str) -> int:
        return int(str(binary), 2)

    @staticmethod
    def get_mask_combinations(mask: str) -> list:
        combinations = list(product([0, 1], repeat=mask.count("X")))

        masks = []
        for combination in combinations:
            tmp_mask = mask
            for num in combination:
                tmp_mask = tmp_mask.replace("X", str(num), 1)
            masks.append(tmp_mask)

        return masks

    @staticmethod
    def load_input() -> list:
        list_input = []
        with open("input.txt", encoding="utf-8") as file:
            for line in file:
                list_input.append(line.rstrip())
        return list_input


day = Day14()
print(f"Result part 1: {day.part_one()}")
print(f"Result part 2: {day.part_two()}")
