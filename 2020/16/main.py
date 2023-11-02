from re import match
from math import prod


class Day16:
    def __init__(self):
        self.rules, self.nearby_tickets, self.your_ticket = self.load_input()
        self.categorize_tickets(self.rules, self.nearby_tickets)

    def part_one(self) -> int:
        return sum(
            number["num"]
            for ticket in self.nearby_tickets
            for number in ticket
            if len(number["valid_ranges"]) == 0
        )

    def part_two(self) -> int:
        nearby_tickets = self.remove_invalid_tickets(self.nearby_tickets)

        while not self.is_order_determined(nearby_tickets):
            for i in range(len(nearby_tickets[0])):
                ranges_set = [set(x[i]["valid_ranges"]) for x in nearby_tickets]
                ranges_in_common = set.intersection(*ranges_set)

                if len(ranges_in_common) == 1:
                    self.remove_field(nearby_tickets, ranges_in_common, i)

        indexes = self.get_indexes_of_rule(nearby_tickets, "departure")
        return prod([self.your_ticket[i] for i in indexes])

    @staticmethod
    def is_order_determined(tickets: list) -> bool:
        return all(len(number["valid_ranges"]) == 1 for ticket in tickets for number in ticket)

    @staticmethod
    def remove_field(tickets: list, range_in_common: set, i: int) -> None:
        for ticket in tickets:
            for j, number in enumerate(ticket):
                if j != i:
                    num_to_remove = list(range_in_common)[0]
                    if num_to_remove in number["valid_ranges"]:
                        number["valid_ranges"].remove(num_to_remove)
                else:
                    number["valid_ranges"] = list(range_in_common)

    @staticmethod
    def get_indexes_of_rule(tickets: list, rule_name: str) -> list:
        return [
            i
            for i, num in enumerate(tickets[0])
            if any(rule_name in s for s in num["valid_ranges"])
        ]

    def categorize_tickets(self, rules: dict, tickets: list) -> None:
        for ticket in tickets:
            for number in ticket:
                for name, ranges in rules.items():
                    if self.in_range(ranges, number):
                        number["valid_ranges"].append(name)

    @staticmethod
    def in_range(ranges: list, number: dict) -> bool:
        return ranges[0] <= number["num"] <= ranges[1] or ranges[2] <= number["num"] <= ranges[3]

    @staticmethod
    def remove_invalid_tickets(tickets: list) -> list:
        return [ticket for ticket in tickets if all(len(x["valid_ranges"]) > 0 for x in ticket)]

    @staticmethod
    def load_input() -> (dict, list):
        rules = {}
        rules_pattern = r"(\b\w+\b|\b\w+ \w+\b): (\d+)-(\d+) or (\d+)-(\d+)"

        nearby_tickets = []
        your_ticket = None

        with open("input.txt", encoding="utf-8") as file:
            is_nearby_tickets = False
            is_your_ticket = False

            for line in file:
                line = line.rstrip()

                res = match(rules_pattern, line)
                if res:
                    name, f1, t1, f2, t2 = res.groups()
                    rules[name] = [int(f1), int(t1), int(f2), int(t2)]

                if is_nearby_tickets:
                    nearby_tickets.append(
                        [{"num": int(x), "valid_ranges": []} for x in line.split(",")]
                    )

                if is_your_ticket:
                    your_ticket = [int(x) for x in line.split(",")]
                    is_your_ticket = False

                if "nearby tickets" in line:
                    is_nearby_tickets = True

                if "your ticket" in line:
                    is_your_ticket = True

        return rules, nearby_tickets, your_ticket


day = Day16()
print(f"Result part 1: {day.part_one()}")
print(f"Result part 2: {day.part_two()}")
