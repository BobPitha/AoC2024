import re
from AoC2024.common import vprint, DEBUG, INFO

MUL_PATTERN = r"mul\(\d{1,3},\d{1,3}\)"
CONTROL_PATTERN = r"do\(\)|don't\(\)"

def read_input(file_path):
    """Reads the input data from a file."""
    try:
        with open(file_path, 'r') as f:
            data = [line.strip() for line in f]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        exit(1)
    vprint(INFO, f"Read {len(data)} lines from file {file_path}")
    return data

def mul(instruction):
    match = re.match(r"mul\((\d+),(\d+)\)", instruction)
    if match:
        vprint(DEBUG, f"{instruction} -> {match.group(1)}, {match.group(2)}")
        return int(match.group(1)) * int(match.group(2))
    raise ValueError(f"Error parsing mul instruction '{instruction}'")

def solve_part_1(data):
    sum = 0
    for line in data:
        for match in re.findall(MUL_PATTERN, line):
            sum += mul(match)
    return sum

def solve_part_2(data):
    sum = 0
    enabled = True
    for line in data:
        for match in re.findall(f"{MUL_PATTERN}|{CONTROL_PATTERN}", line):
            if (match == "do()"):
                enabled = True
            elif (match == "don't()"):
                enabled = False
            elif (enabled):
                sum += mul(match)
    return sum

def main(input_file):
    # read input
    data = read_input(input_file)

    part1_result = solve_part_1(data)
    print(f"Part 1: {part1_result}")
    
    part2_result = solve_part_2(data)
    print(f"Part 2: {part2_result}")
