import os
import re
import subprocess

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

INTERP_FILE = "interpreter.py"


def run_program(input_text: str) -> str:
    """Run interpreter.py with given input and return full stdout."""
    try:
        result = subprocess.run(
            ["python3", INTERP_FILE],
            input=input_text.encode(),
            capture_output=True,
            timeout=5,
        )
    except FileNotFoundError:
        return ""
    return result.stdout.decode()


def assert_result(test_name: str, output: str, expected: str) -> None:
    """
    Pass if program output ends with the expected result string.
    Handles prompt and output on the same line.
    """
    pattern = rf"(?:^|.*)({re.escape(expected)})\s*$"
    if re.search(pattern, output, flags=re.MULTILINE):
        print(f"{GREEN}PASS{RESET} {test_name}")
    else:
        print(f"{RED}FAIL{RESET} {test_name}")
        print(f"   expected: {expected}")
        lines = output.splitlines()
        if lines:
            print("   last few lines:")
            for l in lines[-5:]:
                print("   ", l)
        else:
            print("   <no output>")


def main():
    if not os.path.exists(INTERP_FILE):
        print(
            f"{YELLOW}WARNING:{RESET} {INTERP_FILE} not found. Please create the file and start coding!"
        )
        return
    if os.path.getsize(INTERP_FILE) == 0:
        print(
            f"{YELLOW}NOTE:{RESET} {INTERP_FILE} is empty. Begin writing your program!"
        )
        return

    # Spec tests
    assert_result("1 + 1 -> 2.0", run_program("1 + 1\n"), "2.0")
    assert_result("2 - 3 -> -1.0", run_program("2 - 3\n"), "-1.0")
    assert_result("2 * 2 -> 4.0", run_program("2 * 2\n"), "4.0")
    assert_result("50 / 5 -> 10.0", run_program("50 / 5\n"), "10.0")
    assert_result("-1 + 100 -> 99.0", run_program("-1 + 100\n"), "99.0")


if __name__ == "__main__":
    main()
