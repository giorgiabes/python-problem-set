import os
import re
import subprocess

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

TWTTR_FILE = "twttr.py"


def run_program(input_text: str) -> str:
    """Run twttr.py with given input and return full stdout (not stripped)."""
    try:
        result = subprocess.run(
            ["python3", TWTTR_FILE],
            input=input_text.encode(),
            capture_output=True,
            timeout=5,
        )
    except FileNotFoundError:
        return ""
    return result.stdout.decode()


def assert_output(test_name: str, output: str, expected: str) -> None:
    """
    Find the last occurrence of 'Output:' anywhere in the program output,
    and compare the text on that same line after it to the expected string.
    """
    idx = output.rfind("Output:")
    if idx == -1:
        print(f"{RED}FAIL{RESET} {test_name}")
        print("   expected an 'Output:' line but none was found")
        lines = output.splitlines()
        if lines:
            print("   last few lines:")
            for l in lines[-5:]:
                print("   ", l)
        else:
            print("   <no output>")
        return

    # Take the line that contains the final "Output:"
    tail = output[idx:]
    first_line = tail.splitlines()[0]  # e.g., "Output: Twttr" or "Output:    Twttr"
    m = re.search(r"Output:\s*(.*)$", first_line)
    if not m:
        print(f"{RED}FAIL{RESET} {test_name}")
        print("   could not parse output from:", first_line)
        return

    actual = m.group(1)
    if actual == expected:
        print(f"{GREEN}PASS{RESET} {test_name}")
    else:
        print(f"{RED}FAIL{RESET} {test_name}")
        print(f"   expected: Output: {expected}")
        print(f"   got:      Output: {actual}")


def main():
    # Friendly handling if twttr.py doesn't exist or is empty
    if not os.path.exists(TWTTR_FILE):
        print(
            f"{YELLOW}WARNING:{RESET} {TWTTR_FILE} not found. Please create the file and start coding!"
        )
        return
    if os.path.getsize(TWTTR_FILE) == 0:
        print(
            f"{YELLOW}NOTE:{RESET} {TWTTR_FILE} is empty. Begin writing your program!"
        )
        return

    # Tests
    out = run_program("Twitter\n")
    assert_output("Test 1: Twitter -> Twttr", out, "Twttr")

    out = run_program("What's your name?\n")
    assert_output("Test 2: What's your name? -> Wht's yr nm?", out, "Wht's yr nm?")

    out = run_program("PY3\n")
    assert_output("Test 3: PY3 -> PY3", out, "PY3")

    out = run_program("YEAR2025\n")
    assert_output("Test 4: YEAR2025 -> YR2025", out, "YR2025")


if __name__ == "__main__":
    main()
