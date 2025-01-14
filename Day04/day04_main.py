from AoC2024.common import vprint, DEBUG, INFO

SEARCH_WORD = "XMAS"
SEARCH_DIRS = { \
    "UL": [-1, -1], \
    "U":  [-1, 0], \
    "UR": [-1, 1], \
    "L":  [0, -1], \
    "R":  [0, 1], \
    "DL": [1, -1], \
    "D":  [1, 0], \
    "DR": [1, 1] }

def read_input(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = list(line.strip() for line in f)
        return lines
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found. Please check the file path")
        exit(1)

def count_xmases_starting_at(data, y, x):
    NumXmases = 0
    vprint(1, f"X at [{y}, {x}]: ", end="")
    for dir in SEARCH_DIRS:
        offset = SEARCH_DIRS[dir]
        end=[y+ offset[0]*(len(SEARCH_WORD)-1), x + offset[1]*(len(SEARCH_WORD)-1)]
        if end[0] >= 0 and end[0] < len(data) and end[1] >= 0 and end[1] < len(data[0]):
            for i in range(1, len(SEARCH_WORD)):
                letter = data[y+(i*offset[0])][x+(i*offset[1])]
                if (data[y+(i*offset[0])][x+(i*offset[1])] != SEARCH_WORD[i]):
                    break
            else:
                vprint(1, f"{dir }")
                NumXmases += 1
    vprint(1, "")
    return NumXmases

def is_x_mas(data, y, x):
    if y >= 1 and y <= len(data)-2 and x >= 1 and x <= len(data[y])-2:
        if ((data[y-1][x-1] == 'M' and data[y+1][x+1] == 'S') or \
             data[y-1][x-1] == 'S' and data[y+1][x+1] == 'M') and \
           ((data[y-1][x+1] == 'M' and data[y+1][x-1] == 'S') or \
             data[y-1][x+1] == 'S' and data[y+1][x-1] == 'M'):
            return True
    return False

def solve_part_1(data):
    TotalXmases = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if (data[y][x] == 'X'):
                TotalXmases += count_xmases_starting_at(data, y, x)
    return TotalXmases

def solve_part_2(data):
    TotalXMases = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if (data[y][x] == 'A'):
                if (is_x_mas(data, y, x)):
                    TotalXMases += 1
    return TotalXMases

def main(input_file):
    # read input
    lines = read_input(input_file)

    part1_result = solve_part_1(lines)
    part2_result = solve_part_2(lines)

    print(f"Part 1: {part1_result}")
    print(f"Part 2: {part2_result}")

