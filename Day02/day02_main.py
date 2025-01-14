from common import vprint

def read_input(file_path):
    """Reads the input data from a file."""
    try:
        with open(file_path, 'r') as f:
            return [list(map(int, line.strip().split())) for line in f]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        exit(1)
    except ValueError:
        print(f"Error: Input file '{file_path}' contains invalid data")
        exit(1)
    
def solve_part_1(data):
    safe_count = sum(is_safe(report) for report in data)
    return safe_count

def solve_part_2(data):
    safe_count = sum(is_safe_with_dampener(report) for report in data)
    return safe_count

def is_safe(report):
    if any(abs(report[i+1] - report[i]) > 3 for i in range(len(report)-1)):
        return 0
    
    return 1 if ( \
        all(report[i] < report[i+1] for i in range(len(report)-1)) or \
        all(report[i] > report[i+1] for i in range(len(report)-1)) \
    ) else 0

def is_safe_with_dampener(report):
    if is_safe(report):
        return 1
    
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return 1
    return 0

def main(input_file):
    # read input
    data = read_input(input_file)

    part1_result = solve_part_1(data)
    part2_result = solve_part_2(data)
    print(f"Part 1: {part1_result}")
    print(f"Part 2: {part2_result}")
