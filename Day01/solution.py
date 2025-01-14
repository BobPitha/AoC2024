def read_input(path):
    with open(path, 'r') as f:
        lines = f.readlines()

    first = []
    second = []

    for line in lines:
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

if __name__ == "__main__":
    # read input
    list1, list2 = read_input("input.txt")

    part1_result = solve_part_1(list1, list2)
    part2_result = solve_part_2(list1, list2)

    print(f"Part 1: {part1_result}")
    print(f"Part 2: {part2_result}")

