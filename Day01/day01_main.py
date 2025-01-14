from AoC2024.common import vprint, DEBUG, INFO

def read_input(path):
    first = []
    second = []
    with open(path, 'r') as f:
        for line in f:
            num1, num2 = map(int, line.split())
            first.append(num1)
            second.append(num2)
    return first, second

def solve_part_1(list1, list2):
    list1.sort()
    list2.sort()

    total_distance = sum(abs(l - r) for l, r in zip(list1, list2))
    return total_distance

def solve_part_2(list1, list2):
    sim = 0
    for i in list1:
        sim += i * list2.count(i)

    sim = sum(i * list2.count(i) for i in list1)
    return sim

def main(input_file):
    # Read input
    list1, list2 = read_input(input_file)

    # Solve and print results
    part1_result = solve_part_1(list1, list2)
    vprint(1, f"Part 1: {part1_result}")
    
    part2_result = solve_part_2(list1, list2)
    vprint(1, f"Part 2: {part2_result}")