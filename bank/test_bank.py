import os
import re
import subprocess

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

BANK_FILE = "bank.py"


def run_program(input_text: str) -> str:
    """Run bank.py with given input and return stdout as string."""
    try:
        result = subprocess.run(
            ["python3", BANK_FILE],
            input=input_text.encode(),
            capture_output=True,
            timeout=5,
        )
    except FileNotFoundError:
        return ""
    return result.stdout.decode()


def assert_output(test_name: str, output: str, expected: str) -> None:
    """
    Find the last occurrence of a dollar amount ($0, $20, $100)
    and compare it to the expected output.
    """
    matches = re.findall(r"\$\d+", output)
    if not matches:
        print(f"{RED}FAIL{RESET} {test_name}")
        print("   expected to find a dollar amount in output but none was found")
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
    # Friendly handling if bank.py doesn't exist or is empty
    if not os.path.exists(BANK_FILE):
        print(
            f"{YELLOW}WARNING:{RESET} {BANK_FILE} not found. Please create the file and start coding!"
        )
        return
    if os.path.getsize(BANK_FILE) == 0:
        print(f"{YELLOW}NOTE:{RESET} {BANK_FILE} is empty. Begin writing your program!")
        return

    # Actual tests
    assert_output("Test 1: Hello -> $0", run_program("Hello\n"), "$0")
    assert_output("Test 2: Hello, Newman -> $0", run_program("Hello, Newman\n"), "$0")
    assert_output("Test 3: Hey -> $20", run_program("Hey\n"), "$20")
    assert_output(
        "Test 4: How you doing? -> $20", run_program("How you doing?\n"), "$20"
    )
    assert_output(
        "Test 5: What's happening? -> $100", run_program("What's happening?\n"), "$100"
    )
    assert_output(
        "Test 6: Random greeting -> $100", run_program("Good morning\n"), "$100"
    )


if __name__ == "__main__":
    main()
