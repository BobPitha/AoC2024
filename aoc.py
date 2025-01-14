from pathlib import Path
import importlib
from AoC2024.common import handle_arguments, vprint, DEBUG, INFO

def main():
    args = handle_arguments()

    vprint(DEBUG, args)

    # Normalize the day argument to match directory names
    day = f"Day{int(args.day):02d}" if args.day.isdigit() else args.day

    try:
        # Dynamically load the solution module for the specified day
        solution_module = importlib.import_module(f"AoC2024.{day}.day{int(args.day):02d}_main")

        # Load the input file from the day's directory
        input_filename = args.input or "input.txt"
        input_file = Path(f"{day}/{input_filename}")
        if not input_file.exists():
            raise FileNotFoundError(f"Input file not found: {input_file}")

        # Run the solution's main function (assumes each solution.py has a main())
        solution_module.main(str(input_file))
    except ModuleNotFoundError:
        print(f"Error: Solution for {day} not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()