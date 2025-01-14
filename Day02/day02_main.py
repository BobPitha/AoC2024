from common import vprint, DEBUG, INFO

def read_input(file_path):
    """Reads the input data from a file."""
    try:
        with open(file_path, 'r') as f:
            return [list(map(int, line.strip().split())) for line in f]
    except FileNotFoundError:
        vprint(DEBUG, f"File not found: {file_path}")
        raise FileNotFoundError(f"File '{file_path}' not found")
    except ValueError:
        vprint(DEBUG, f"Value error")
        raise ValueError(f"Input file '{file_path}' contains invalid data")
    
def solve_part_1(data):
    safe_count = sum(is_safe(report) for report in data)
    return safe_count

def solve_part_2(data):
    safe_count = sum(is_safe_with_dampener(report) for report in data)
    return safe_count

def is_safe(report):
    increasing, decreasing = True, True
    for i in range(len(report) - 1):
        if abs(report[i + 1] - report[i]) > 3:
            return 0
        if report[i] >= report[i + 1]:
            increasing = False
        if report[i] <= report[i + 1]:
            decreasing = False
    return 1 if increasing or decreasing else 0

def is_safe_with_dampener(report):
    if is_safe(report):
        return 1
    
    for i in range(len(report)):
        if is_safe(report[:i] + report[i+1:]):
            return 1
    return 0

def main(input_file):
    # read input
    try:
        vprint(DEBUG, f"Reading file {input_file}")
        data = read_input(input_file)
    except (FileNotFoundError, ValueError) as err:
        print(f"Error: {err}")
        exit(1)

    part1_result = solve_part_1(data)
    part2_result = solve_part_2(data)
    print(f"Part 1: {part1_result}")
    print(f"Part 2: {part2_result}")
