import os
import subprocess

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

CAMEL_FILE = "camel.py"


def run_program(input_text):
    """Run camel.py with the given input and return its output."""
    result = subprocess.run(
        ["python3", CAMEL_FILE], input=input_text.encode(), capture_output=True
    )
    return result.stdout.decode().strip()


def check_case(test_name, input_text, expected):
    """Helper to check one test case."""
    output = run_program(input_text)

    if not output:
        print(f"{RED}FAIL{RESET} {test_name}")
        print(f"   input:    {input_text.strip()}")
        print(f"   expected: snake_case: {expected}")
        print(f"   got:      <no output>")
        return

    # Sometimes the prompt ("camelCase: ") and the result appear on one line
    # when running non-interactively. Find the last occurrence of "snake_case:".
    lines = output.splitlines()
    target_line = None
    for line in lines[::-1]:  # search from the end
        if "snake_case:" in line:
            target_line = line
            break

    if target_line is None:
        print(f"{RED}FAIL{RESET} {test_name}")
        print(f"   input:    {input_text.strip()}")
        print(f"   expected: snake_case: {expected}")
        print(f"   got:      {lines[-1] if lines else '<no output>'}")
        return

    # Extract the value after "snake_case:"
    actual = target_line.split("snake_case:", 1)[1].strip()

    if actual == expected:
        print(f"{GREEN}PASS{RESET} {test_name}")
    else:
        print(f"{RED}FAIL{RESET} {test_name}")
        print(f"   input:    {input_text.strip()}")
        print(f"   expected: snake_case: {expected}")
        print(f"   got:      snake_case: {actual}")


def main():
    # Check if camel.py exists
    if not os.path.exists(CAMEL_FILE):
        print(
            f"{YELLOW}WARNING:{RESET} {CAMEL_FILE} not found. Please create the file and start coding!"
        )
        return

    # Check if camel.py is empty
    if os.path.getsize(CAMEL_FILE) == 0:
        print(
            f"{YELLOW}NOTE:{RESET} {CAMEL_FILE} is empty. Begin writing your program!"
        )
        return

    # Run actual tests
    check_case("Test 1: single word", "name\n", "name")
    check_case("Test 2: two words", "firstName\n", "first_name")
    check_case("Test 3: three words", "preferredFirstName\n", "preferred_first_name")

    # Check if camel.py exists
    if not os.path.exists(CAMEL_FILE):
        print(
            f"{YELLOW}WARNING:{RESET} {CAMEL_FILE} not found. Please create the file and start coding!"
        )
        return

    # Check if camel.py is empty
    if os.path.getsize(CAMEL_FILE) == 0:
        print(
            f"{YELLOW}NOTE:{RESET} {CAMEL_FILE} is empty. Begin writing your program!"
        )
        return

    # Run actual tests
    check_case("Test 1: single word", "name\n", "name")
    check_case("Test 2: two words", "firstName\n", "first_name")
    check_case("Test 3: three words", "preferredFirstName\n", "preferred_first_name")


if __name__ == "__main__":
    main()
