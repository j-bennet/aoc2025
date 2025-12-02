from os import path

ROOT_DIR = path.dirname(__file__)


def get_data(filename="input.txt"):
    full_name = path.join(ROOT_DIR, filename)
    with open(full_name) as f:
        return f.read().splitlines()
    

def parse_data(data):
    instructions = []
    for line in data:
        direction = line[0]
        amount = int(line[1:])
        instructions.append((direction, amount))
    return instructions
    

def move_dial(current, direction, amount):
    if direction == 'L':
        current = (current - amount) % 100
    elif direction == 'R':
        current = (current + amount) % 100
    # print(f"The dial is rotated {direction}{amount} to point at {current}")
    return current


def move_dial2(current, direction, amount):
    previous = current
    crossovers = amount // 100
    offset = amount % 100
    if direction == "L":
        offset = -offset
    current = previous + offset
    if previous != 0 and (current > 100 or current < 0):
        crossovers += 1
    current = current % 100
    # message = f"The dial is rotated {direction}{amount} to point at {current}"
    # print(f"--- {previous}\t+\t{direction}{amount}\t->\t{current}\t({cross})")
    # if crossovers > 0:
    #     message += f"; during this rotation, it points at 0 {crossovers}x."
    # print(message)
    return current, crossovers


def part1(data):
    """Part 1"""
    result = 0
    instructions = parse_data(data)
    dial_position = 50
    result = 0
    for direction, amount in instructions:
        dial_position = move_dial(dial_position, direction, amount)
        if dial_position == 0:
            result += 1
    return result


def part2(data):
    """Part 2"""
    result = 0
    instructions = parse_data(data)
    dial_position = 50
    result = 0
    for direction, amount in instructions:
        dial_position, cross = move_dial2(dial_position, direction, amount)
        if dial_position == 0:
            result += 1
        result += cross
    return result


if __name__ == "__main__":
    # print(f"Part 1: {part1(get_data('example.txt'))}")
    # print(f"Part 2: {part2(get_data('example.txt'))}")
    print(f"Part 1: {part1(get_data('input.txt'))}")
    print(f"Part 2: {part2(get_data('input.txt'))}")
