import os
import re
import subprocess

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

NUTRITION_FILE = "nutrition.py"


def run_program(input_text: str) -> str:
    """Run nutrition.py with given input and return full stdout."""
    try:
        result = subprocess.run(
            ["python3", NUTRITION_FILE],
            input=input_text.encode(),
            capture_output=True,
            timeout=5,
        )
    except FileNotFoundError:
        return ""
    return result.stdout.decode()


def assert_calories(test_name: str, output: str, expected_value: int) -> None:
    """
    Find the last 'Calories: N' in the output (handles prompts on same line)
    and compare N with expected_value.
    """
    matches = re.findall(r"Calories:\s*(\d+)", output)
    if not matches:
        print(f"{RED}FAIL{RESET} {test_name}")
        print("   expected a 'Calories: N' line but none was found")
        lines = output.splitlines()
        if lines:
            print("   last few lines:")
            for l in lines[-5:]:
                print("   ", l)
        else:
            print("   <no output>")
        return

    actual = int(matches[-1])
    if actual == expected_value:
        print(f"{GREEN}PASS{RESET} {test_name}")
    else:
        print(f"{RED}FAIL{RESET} {test_name}")
        print(f"   expected: Calories: {expected_value}")
        print(f"   got:      Calories: {actual}")


def assert_no_output(test_name: str, output: str) -> None:
    """Pass if no 'Calories:' line appears at all."""
    if re.search(r"Calories:\s*\d+", output):
        print(f"{RED}FAIL{RESET} {test_name}")
        print("   expected no calories output, but found one")
        lines = output.splitlines()
        if lines:
            print("   last few lines:")
            for l in lines[-5:]:
                print("   ", l)
        else:
            print("   <no output>")
    else:
        print(f"{GREEN}PASS{RESET} {test_name}")


def main():
    if not os.path.exists(NUTRITION_FILE):
        print(
            f"{YELLOW}WARNING:{RESET} {NUTRITION_FILE} not found. Please create the file and start coding!"
        )
        return
    if os.path.getsize(NUTRITION_FILE) == 0:
        print(
            f"{YELLOW}NOTE:{RESET} {NUTRITION_FILE} is empty. Begin writing your program!"
        )
        return

    # Spec tests (case-insensitive)
    assert_calories("Apple -> 130", run_program("Apple\n"), 130)
    assert_calories("Avocado -> 50", run_program("Avocado\n"), 50)
    assert_calories("Sweet Cherries -> 100", run_program("Sweet Cherries\n"), 100)
    assert_no_output("Tomato -> no output", run_program("Tomato\n"))

    # A few more
    assert_calories("banana -> 110", run_program("banana\n"), 110)
    assert_calories("ORANGE -> 80", run_program("ORANGE\n"), 80)
    assert_calories("honeydew melon -> 50", run_program("honeydew melon\n"), 50)
    assert_calories("STRAWBERRIES -> 50", run_program("STRAWBERRIES\n"), 50)
    assert_no_output("unknown item -> no output", run_program("chocolate\n"))


if __name__ == "__main__":
    main()
