import collections


class Day03:

    def __init__(self):
        self.puzzle_input = self.load_input()

    def part_one(self) -> int:
        bits = collections.defaultdict(list)

        for number in self.puzzle_input:
            for index in range(len(number)):
                bits[index].append(number[index])

        most_common = least_common = ""
        for key, value in bits.items():
            counter = collections.Counter(value)

            most_common += counter.most_common(1)[0][0]
            least_common += counter.most_common()[-1][0]

        gamma_rate = self.binary_to_decimal(most_common)
        epsilon_rate = self.binary_to_decimal(least_common)

        return gamma_rate * epsilon_rate

    def part_two(self) -> int:
        co2_scrubber_rating = self.get_rating(self.puzzle_input, True)
        oxygen_generator_rating = self.get_rating(self.puzzle_input, False)

        csr = self.binary_to_decimal(co2_scrubber_rating)
        ogr = self.binary_to_decimal(oxygen_generator_rating)

        return csr * ogr

    def get_rating(self, input_list, least: bool, index: int = 0) -> str:
        bits_one, bits_zero = [], []

        for number in input_list:
            bits_one.append(number) if number[index] == "1" else bits_zero.append(number)

        if least:  # Keep list with least numbers
            result = bits_zero if (len(bits_one) >= len(bits_zero)) else bits_one
        else:  # Keep list with most numbers
            result = bits_one if len(bits_one) >= len(bits_zero) else bits_zero

        if len(result) == 1:
            return result[0]

        return self.get_rating(input_list=result, least=least, index=index + 1)

    @staticmethod
    def load_input() -> list:
        list_input = []
        with open("input.txt") as file:
            for line in file:
                list_input.append((line.rstrip()))
        return list_input

    @staticmethod
    def binary_to_decimal(binary: str) -> int:
        return int(binary, 2)


day = Day03()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
