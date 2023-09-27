from collections import defaultdict


class Day07:
    def __init__(self):
        self.puzzle_input = self.load_input()

    def part_one(self) -> int:
        bags = self.get_bags_sorted(self.puzzle_input)
        counted_bags = set()
        for key in bags.keys():
            if self.contains_shiny_gold(bags, key, counted_bags):
                counted_bags.add(key)

        return len(counted_bags)

    def part_two(self) -> int:
        bags = self.get_bags_sorted(self.puzzle_input)
        return self.get_bags_inside("shiny gold", bags)

    @staticmethod
    def get_bags_sorted(puzzle_input: list) -> defaultdict:
        bags = defaultdict(list)

        for line in puzzle_input:
            splitted = line.split()
            current_bag_name = splitted[0] + " " + splitted[1]

            # Contains at least one bag
            if splitted[4].isdigit():
                additional_bags = []

                sum_bags = len(splitted[4:]) // 4
                name_index, amount_index = 5, 4
                for _ in range(1, sum_bags + 1):
                    child_bag_name = (
                        splitted[name_index] + " " + splitted[name_index + 1]
                    )
                    additional_bags.append(
                        {"name": child_bag_name, "amount": int(splitted[amount_index])}
                    )
                    name_index += 4
                    amount_index += 4

                bags[current_bag_name].extend(additional_bags)
        return bags

    def get_bags_inside(self, key, bags) -> int:
        bag_contents = bags.get(key)

        if bag_contents is None:
            return 0

        total_bags = 0
        for val in bag_contents:
            total_bags += val["amount"] + val["amount"] * self.get_bags_inside(
                val["name"], bags
            )

        return total_bags

    def contains_shiny_gold(self, bags, key, counted_bags) -> bool:
        if bags.get(key) is None:
            return False

        if any(entry.get("name") == "shiny gold" for entry in bags.get(key)):
            return True

        for val in bags.get(key):
            if self.contains_shiny_gold(bags, val["name"], counted_bags):
                counted_bags.add(val["name"])
                return True

    @staticmethod
    def load_input() -> list:
        list_input = []
        with open("input.txt") as file:
            for line in file:
                list_input.append(line.rstrip())
        return list_input


day = Day07()
print(f"Result part 1: {day.part_one()}")
print(f"Result part 2: {day.part_two()}")
