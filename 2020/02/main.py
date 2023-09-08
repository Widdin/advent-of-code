from collections import Counter

class Day02:

    def __init__(self):
        self.puzzle_input = self.load_input()

    def part_one(self) -> int:
        valid_passwords = 0
        for line in self.puzzle_input:
            policy, letter, password = map(line.get, ['policy', 'letter', 'password'])
            collection = Counter(password)
            low, top = map(int, policy.split("-"))

            if low <= collection[letter] <= top:
                valid_passwords += 1

        return valid_passwords

    def part_two(self) -> int:
        valid_passwords = 0
        for line in self.puzzle_input:
            policy, letter, password = map(line.get, ['policy', 'letter', 'password'])
            low, top = map(int, policy.split("-"))

            first_char = password[low - 1]
            second_char = password[top - 1]

            if first_char != second_char:
                if first_char == letter or second_char == letter:
                    valid_passwords += 1
                    
        return valid_passwords

    @staticmethod
    def load_input() -> list:
        list_input = []
        with open("input.txt") as file:
            for line in file:
                policy, letter, password = line.replace(":", "").split()
                list_input.append({'policy': policy, 'letter': letter, 'password': password})
        return list_input


day = Day02()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
