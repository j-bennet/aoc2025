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
    if current < 0:
        current += 100
    print(f"The dial is rotated {direction}{amount} to point at {current}")
    return current


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
        dial_position = move_dial(dial_position, direction, amount)
        if dial_position == 0:
            result += 1
        crossovers = amount // 100
        result += crossovers
    return result


if __name__ == "__main__":
    print(f"Part 1: {part1(get_data('input.txt'))}")
    #print(f"Part 2: {part2(get_data('example.txt'))}")
