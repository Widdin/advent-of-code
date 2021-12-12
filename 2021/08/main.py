class Day08:

    def __init__(self):
        self.puzzle_input = self.get_puzzle_input()
        self.output_decoded = []
        self.count_easy_digits = 0
        self.parse_seven_segment()

    def part_one(self) -> int:
        return self.count_easy_digits

    def part_two(self) -> int:
        return sum(self.output_decoded)

    def parse_seven_segment(self) -> None:
        notes = self.puzzle_input.copy()
        for note in notes:
            segments = note.split(' | ')[1].split()
            signal_patterns = note.split(' | ')[0].split()
            signal_patterns.sort(key=len)

            mapping = {
                1: signal_patterns[0],
                4: signal_patterns[2],
                7: signal_patterns[1],
                8: signal_patterns[-1]
            }

            unknowns = []
            for signal in signal_patterns:
                if signal not in mapping.values():
                    unknowns.append(signal)

            mapping[3] = self.get_number_three(mapping, unknowns)
            mapping[9] = self.get_number_nine(mapping, unknowns)
            mapping[6] = self.get_number_six(mapping, unknowns)
            mapping[0] = self.get_number_zero(unknowns)
            mapping[5] = self.get_number_five(mapping, unknowns)
            mapping[2] = unknowns[0]

            score = ""
            for seg in segments:
                for key, value in mapping.items():
                    if set(value).issubset(seg) and len(value) == len(seg):
                        if key in [1, 4, 7, 8]:
                            self.count_easy_digits += 1

                        score += str(key)

            self.output_decoded.append(int(score))

    @staticmethod
    def get_number_five(mapping, unknowns) -> str:
        for num in unknowns:
            if set(num).issubset(mapping[6]):
                return unknowns.pop(unknowns.index(num))

    @staticmethod
    def get_number_zero(unknowns) -> str:
        for num in unknowns:
            if len(num) == 6:
                return unknowns.pop(unknowns.index(num))

    @staticmethod
    def get_number_six(mapping, unknowns) -> str:
        substr = mapping[8]
        for i in mapping[1]:
            substr = substr.replace(i, '')

        for num in unknowns:
            if (set(substr + mapping[1][0]).issubset(num) or set(substr + mapping[1][1]).issubset(num)) and len(num) == 6:
                return unknowns.pop(unknowns.index(num))

    @staticmethod
    def get_number_nine(mapping, unknowns) -> str:
        substr = mapping[4]
        for i in mapping[3]:
            substr = substr.replace(i, '')

        for num in unknowns:
            if set(substr + mapping[3]).issubset(num) and len(num) == 6:
                return unknowns.pop(unknowns.index(num))

    @staticmethod
    def get_number_three(mapping, unknowns) -> str:
        substr = mapping[4].replace(mapping[7][0], '').replace(mapping[7][1], '').replace(mapping[7][2], '')
        for num in unknowns:
            if (set(substr[1] + mapping[7]).issubset(num) or set(substr[0] + mapping[7]).issubset(num)) and len(num) == 5:
                return unknowns.pop(unknowns.index(num))

    @staticmethod
    def get_puzzle_input() -> list:
        lst = []
        with open("input.txt") as file:
            for line in file:
                lst.append(line.rstrip())
        return lst


day = Day08()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
