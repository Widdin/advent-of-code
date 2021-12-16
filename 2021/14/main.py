from collections import defaultdict, Counter


class Day14:

    def __init__(self):
        self.puzzle_input = self.get_puzzle_input()

    def part_one(self) -> int:
        return self.run_steps(steps=10)

    def part_two(self) -> int:
        return self.run_steps(steps=40)

    def run_steps(self, steps):
        data = self.get_puzzle_input().copy()

        polymer_template = None
        pair_insertion_rules = defaultdict(str)

        for line in data:
            if '->' in line:
                pair_from, pair_to = line.split(' -> ')
                pair_insertion_rules[pair_from] = pair_to
            elif line != '':
                polymer_template = list(line)

        polymer_template_pairs = defaultdict(int)
        for i in range(len(polymer_template) - 1):
            a, b = polymer_template[i], polymer_template[i + 1]
            polymer_template_pairs[a + b] += 1

        for i in range(steps):
            polymer_template_pairs = self.find_new_pairs(polymer_template_pairs, pair_insertion_rules)

        letters = self.count_letters(polymer_template_pairs)
        letters[polymer_template[-1]] += 1

        c = Counter(letters)
        most_letter, most_count = c.most_common()[0]
        least_letter, least_count = c.most_common()[-1]

        return most_count - least_count

    @staticmethod
    def count_letters(polymer_template_pairs):
        letters = defaultdict(int)
        for key, value in polymer_template_pairs.items():
            first_letter = key[0]
            letters[first_letter] += value

        return letters

    @staticmethod
    def find_new_pairs(polymer_template, pair_insertion_rules):
        new_polymer_template = defaultdict(int)

        for key, value in polymer_template.items():

            first_letter = key[0]
            second_letter = key[1]

            new_letter = pair_insertion_rules[key]

            new_polymer_template[first_letter + new_letter] += value
            new_polymer_template[new_letter + second_letter] += value

        return new_polymer_template

    @staticmethod
    def get_puzzle_input() -> list:
        lst = []
        with open("input.txt") as file:
            for line in file:
                lst.append(line.rstrip())
        return lst


day = Day14()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
