import re

class Day04:

    def __init__(self):
        self.puzzle_input = self.load_input()

    def part_one(self) -> int:
        return self.validate_passports(validate_data=False)

    def part_two(self) -> int:
        return self.validate_passports(validate_data=True)

    @staticmethod
    def validate_digits(num, req_len, min, max):
        return not len(num) == req_len or not min <= int(num) <= max

    def validate_passports(self, validate_data):
        valid_passports = 0
        expected_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

        for passport in self.puzzle_input:
            passport = passport.rstrip().lstrip().split(" ")
            passport_dict = {key: value for item in passport for key, value in [item.split(':')]}
            difference = set(expected_fields) - set(passport_dict.keys())
            if len(difference) == 0 or (len(difference) == 1 and 'cid' in difference):
                
                if validate_data:
                    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
                    if self.validate_digits(passport_dict['byr'], 4, 1920, 2002):
                        continue

                    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
                    if self.validate_digits(passport_dict['iyr'], 4, 2010, 2020):
                        continue

                    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
                    if self.validate_digits(passport_dict['eyr'], 4, 2020, 2030):
                        continue

                    # hgt (Height) - a number followed by either cm or in:
                    if 'cm' not in passport_dict['hgt'] and 'in' not in passport_dict['hgt']:
                        continue

                    # If cm, the number must be at least 150 and at most 193.
                    if 'cm' in passport_dict['hgt']:
                        if not 150 <= int(passport_dict['hgt'][:-2]) <= 193:
                            continue

                    # If in, the number must be at least 59 and at most 76.
                    if 'in' in passport_dict['hgt']:
                        if not 59 <= int(passport_dict['hgt'][:-2]) <= 76:
                            continue

                    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
                    if not re.match('^#[0-9a-fA-F]{6}$', passport_dict['hcl']):
                        continue

                    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
                    if passport_dict['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                        continue

                    # pid (Passport ID) - a nine-digit number, including leading zeroes.
                    if not len(passport_dict['pid']) == 9 or not passport_dict['pid'].isdigit():
                        continue

                    # cid (Country ID) - ignored, missing or not.
                    
                valid_passports += 1

        return valid_passports

    @staticmethod
    def load_input() -> list:
        list_input = []
        with open("input.txt") as file:
            str = ""
            for line in file:
                line = line.replace("\n", " ")

                if line.rstrip() == "":
                    list_input.append(str)
                    str = ""

                str += line
            list_input.append(str)

        return list_input


day = Day04()
print(f'Result part 1: {day.part_one()}')
print(f'Result part 2: {day.part_two()}')
