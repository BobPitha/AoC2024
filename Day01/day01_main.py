from AoC2024.common import vprint, DEBUG, INFO
from collections import Counter

def read_input(path):
    first = []
    second = []
    with open(path, 'r') as f:
        for line in f:
            try:
                num1, num2 = map(int, line.split())
            except ValueError:
                raise ValueError(f"Malformed line: {line.strip()}")
            first.append(num1)
            second.append(num2)
    return first, second

def solve_part_1(list1, list2):
    list1.sort()
    list2.sort()

    total_distance = sum(abs(val1 - val2) for val1, val2 in zip(list1, list2))
    return total_distance

def solve_part_2(list1, list2):
    count_list_2 = Counter(list2)
    sim = sum(i * count_list_2[i] for i in list1)
    return sim

def main(input_file):
    # Read input
    try:
        list1, list2 = read_input(input_file)
    except (FileNotFoundError, ValueError) as err:
        print(f"Error reading {input_file}: {err}")
        return

    # Solve and print results
    part1_result = solve_part_1(list1, list2)
    print(f"Part 1: {part1_result}")
    
    part2_result = solve_part_2(list1, list2)
    print(f"Part 2: {part2_result}")