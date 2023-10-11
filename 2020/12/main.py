class BaseShip:
    def __init__(self, direction: str, rotation: int, units: dict, waypoint: dict):
        self.direction = direction
        self.rotation = rotation
        self.units = units
        self.waypoint = waypoint

    def get_manhattan_distance(self) -> int:
        return abs(self.units["N"] - self.units["S"]) + abs(self.units["E"] - self.units["W"])

    def get_opposite_direction(self, direction: str) -> str:
        return {"N": "S", "S": "N", "E": "W", "W": "E"}[direction]

    def balance_directions(self, data: dict) -> None:
        if data["N"] >= data["S"]:
            data["N"] -= data["S"]
            data["S"] = 0
        elif data["S"] >= data["N"]:
            data["S"] -= data["N"]
            data["N"] = 0

        if data["E"] >= data["W"]:
            data["E"] -= data["W"]
            data["W"] = 0
        elif data["W"] >= data["E"]:
            data["W"] -= data["E"]
            data["E"] = 0


class FirstShip(BaseShip):
    def rotate(self, direction: str, degrees: int) -> None:
        directions = ["N", "E", "S", "W"]

        rotations = degrees // 90
        rotations = -rotations if direction == "L" else rotations

        current_index = directions.index(self.direction)
        rotated_index = (current_index + rotations) % 4

        self.direction = directions[rotated_index]

    def move_forward(self, value: int) -> None:
        self.units[self.direction] += value
        self.balance_directions(self.units)

    def move(self, direction: str, value: int) -> None:
        self.units[direction] += value


class SecondShip(BaseShip):
    def rotate(self, direction: str, degrees: int) -> None:
        rotations = degrees // 90
        waypoint_values = list(self.waypoint.values())

        for _ in range(rotations):
            if direction == "R":
                waypoint_values.insert(0, waypoint_values.pop())
            elif direction == "L":
                waypoint_values.append(waypoint_values.pop(0))

        for i, (k, _) in enumerate(self.waypoint.items()):
            self.waypoint[k] = waypoint_values[i]

    def move_forward(self, value: int) -> None:
        move_units = {k: v * value for k, v in self.waypoint.items()}
        self.units = {i: move_units[i] + self.units[i] for i in move_units.keys()}
        self.balance_directions(self.units)

    def move(self, direction: str, value: int) -> None:
        self.waypoint[direction] += value
        self.balance_directions(self.waypoint)


class Day12:
    def __init__(self):
        self.puzzle_input = self.load_input()

    def execute_actions(self, ship: BaseShip) -> None:
        for line in self.puzzle_input:
            action, value = line[0], int(line[1:])

            match action:
                case "F":
                    ship.move_forward(value)
                case "L" | "R":
                    ship.rotate(action, value)
                case "N" | "S" | "E" | "W":
                    ship.move(action, value)

    def part_one(self) -> int:
        ship = FirstShip("E", 0, {"N": 0, "E": 0, "S": 0, "W": 0}, {"N": 0, "E": 0, "S": 0, "W": 0})
        self.execute_actions(ship)
        return ship.get_manhattan_distance()

    def part_two(self) -> int:
        ship = SecondShip("E", 0, {"N": 0, "E": 0, "S": 0, "W": 0}, {"N": 1, "E": 10, "S": 0, "W": 0})
        self.execute_actions(ship)
        return ship.get_manhattan_distance()

    @staticmethod
    def load_input() -> list:
        list_input = []
        with open("input.txt", encoding="utf-8") as file:
            for line in file:
                list_input.append(line.rstrip())
        return list_input


day = Day12()
print(f"Result part 1: {day.part_one()}")
print(f"Result part 2: {day.part_two()}")
