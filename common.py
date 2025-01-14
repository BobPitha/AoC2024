import argparse

NONE = 0
INFO = 1
DEBUG = 2
VERBOSITIES = { \
    "none": NONE, \
    "info": INFO, \
    "debug": DEBUG }

verbosity = NONE

def vprint(level, *args, **kwargs):
    if (level <= verbosity):
        print(*args, **kwargs)

def handle_arguments():
    parser = argparse.ArgumentParser(description="Advent of Code 2024, Day 5: Print Queue")
    parser.add_argument("day", help="Specify the day to run (e.g., '1' or 'Day01')")
    parser.add_argument("--input", "-i", help="Filename of the input file")
    parser.add_argument("-v", "--verbosity", default="none", help="Verbosity level: none, info, debug")
    args = parser.parse_args()

    if args.verbosity not in VERBOSITIES:
        parser.error(f"Invalid verbosity option: {args.verbosity}. Allowed values are: {', '.join(VERBOSITIES.keys())}")
    
    global verbosity
    verbosity = VERBOSITIES[args.verbosity]

    return args