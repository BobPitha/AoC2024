from AoC2024.common import vprint, DEBUG, INFO

def read_input(path):
    rules = {}
    updates = []

    with open(path, 'r') as f:
        line = f.readline()
        while line != '\n':
            rule = list(map(int, line.strip().split("|")))
            if rule[0] in rules:
                rules[rule[0]].append(rule[1])
            else:
                rules[rule[0]] = [rule[1]]
            vprint(DEBUG, f"Rule: {line.strip().split("|")} -> {rules[rule[0]]}")
            line = f.readline()
        line = f.readline()
        while line:
            updates.append(list(map(int, line.strip().split(","))))
            vprint(DEBUG, f"Update: {line.strip().split(",")}")
            line = f.readline()
    return rules, updates

def update_ok(update, rules):
    seen = set()
    for page in update:
        if page in rules:
            for second in rules[page]:
                if second in seen:
                    return False
        seen.add(page)
    return True
        

def solve_part_1(rules, updates):
    result = 0
    for update in updates:
        vprint(DEBUG, f"Processing update: {update}")
        if update_ok(update, rules):
            result += update[len(update)//2]
    return result

def fix_update(update, rules):
    seen = set()
    for page in update:
        if page in rules:
            for second in rules[page]:
                if second in seen:
                    update.remove(page)
                    update.insert(update.index(second), page)
                    return fix_update(update, rules)
        seen.add(page)
    return True, update

def solve_part_2(rules, updates):
    result = 0
    for update in updates:
        if not update_ok(update, rules):
            fixed, fixed_update = fix_update(update, rules)
            if fixed:
                result += fixed_update[len(fixed_update)//2]
    return result

def main(input_file):
    rules, updates = read_input(input_file)
    vprint(INFO, f"Read {len(rules)} rules, {len(updates)} updates")
    vprint(DEBUG, f"{rules}")

    result1 = solve_part_1(rules, updates)
    print(f"Part 1: {result1}")

    result2 = solve_part_2(rules, updates)
    print(f"Part 2: {result2}")
