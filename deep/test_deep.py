import os
import re
import subprocess

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

DEEP_FILE = "deep.py"


def run_program(input_text: str) -> str:
    """Run deep.py with given input and return full stdout (unstripped)."""
    try:
        result = subprocess.run(
            ["python3", DEEP_FILE],
            input=input_text.encode(),
            capture_output=True,
            timeout=5,
        )
    except FileNotFoundError:
        return ""
    return result.stdout.decode()


def assert_yes_no(test_name: str, output: str, expected: str) -> None:
    """
    Find the last occurrence of 'Yes' or 'No' at the end of any line
    (handles cases where the prompt and answer share a line).
    """
    # Look for lines that end with Yes/No, then take the last one
    matches = re.findall(r"(Yes|No)\s*$", output, flags=re.MULTILINE)
    if not matches:
        print(f"{RED}FAIL{RESET} {test_name}")
        print("   expected to find 'Yes' or 'No' in the output but none was found")
        lines = output.splitlines()
        if lines:
            print("   last few lines:")
            for l in lines[-5:]:
                print("   ", l)
        else:
            print("   <no output>")
        return

    actual = matches[-1]
    if actual == expected:
        print(f"{GREEN}PASS{RESET} {test_name}")
    else:
        print(f"{RED}FAIL{RESET} {test_name}")
        print(f"   expected: {expected}")
        print(f"   got:      {actual}")


def main():
    # Friendly handling if deep.py doesn't exist or is empty
    if not os.path.exists(DEEP_FILE):
        print(
            f"{YELLOW}WARNING:{RESET} {DEEP_FILE} not found. Please create the file and start coding!"
        )
        return
    if os.path.getsize(DEEP_FILE) == 0:
        print(f"{YELLOW}NOTE:{RESET} {DEEP_FILE} is empty. Begin writing your program!")
        return

    # Tests
    assert_yes_no("Test 1: 42 -> Yes", run_program("42\n"), "Yes")
    assert_yes_no("Test 2: forty-two -> Yes", run_program("forty-two\n"), "Yes")
    assert_yes_no("Test 3: Forty Two -> Yes", run_program("Forty Two\n"), "Yes")
    assert_yes_no("Test 4: 50 -> No", run_program("50\n"), "No")


if __name__ == "__main__":
    main()
