import os
import re
import subprocess

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

COKE_FILE = "coke.py"


def run_program(inputs):
    """Run coke.py with a list of inputs and return full stdout as text."""
    data = "\n".join(str(x) for x in inputs) + "\n"
    try:
        result = subprocess.run(
            ["python3", COKE_FILE],
            input=data.encode(),
            capture_output=True,
            timeout=5,
        )
    except FileNotFoundError:
        return ""
    return result.stdout.decode()


def assert_contains(test_name, output, expected_snippet):
    """Check that expected_snippet appears anywhere in output."""
    if expected_snippet in output:
        print(f"{GREEN}PASS{RESET} {test_name}")
        return

    print(f"{RED}FAIL{RESET} {test_name}")
    print("   expected text not found:", expected_snippet)
    lines = output.splitlines()
    if lines:
        print("   last few lines:")
        for l in lines[-5:]:
            print("   ", l)
    else:
        print("   <no output>")


def assert_final_change(test_name, output, expected_change):
    """Check that the last Change Owed line has the expected value."""
    lines = output.splitlines()
    idx = output.rfind("Change Owed:")
    if idx == -1:
        print(f"{RED}FAIL{RESET} {test_name}")
        print("   expected a 'Change Owed:' but none was found")
        if lines:
            print("   last few lines:")
            for l in lines[-5:]:
                print("   ", l)
        else:
            print("   <no output>")
        return

    tail = output[idx:]
    first_line = tail.splitlines()[0]
    m = re.search(r"Change Owed:\s*(\d+)", first_line)
    if not m:
        print(f"{RED}FAIL{RESET} {test_name}")
        print("   could not parse change from:", first_line)
        return

    actual = int(m.group(1))
    if actual == expected_change:
        print(f"{GREEN}PASS{RESET} {test_name}")
    else:
        print(f"{RED}FAIL{RESET} {test_name}")
        print(f"   expected: Change Owed: {expected_change}")
        print(f"   got:      Change Owed: {actual}")


def main():
    if not os.path.exists(COKE_FILE):
        print(
            f"{YELLOW}WARNING:{RESET} {COKE_FILE} not found. Please create the file and start coding!"
        )
        return
    if os.path.getsize(COKE_FILE) == 0:
        print(f"{YELLOW}NOTE:{RESET} {COKE_FILE} is empty. Begin writing your program!")
        return

    # Tests
    out = run_program([25, 25])
    assert_contains("Starts at 50", out, "Amount Due: 50")
    assert_contains("After 25 -> Amount Due 25", out, "Amount Due: 25")
    assert_final_change("25 + 25 -> change 0", out, 0)

    out = run_program([10, 25, 25])
    assert_contains("After 10 -> Amount Due 40", out, "Amount Due: 40")
    assert_final_change("10 + 25 + 25 -> change 10", out, 10)

    out = run_program([5, 25, 10, 10])
    assert_contains("After 5 -> Amount Due 45", out, "Amount Due: 45")
    assert_final_change("5 + 25 + 10 + 10 -> change 0", out, 0)

    out = run_program([30, 25, 25])
    assert_contains("Invalid 30 keeps due at 50", out, "Amount Due: 50")
    assert_final_change("30 (ignored) + 25 + 25 -> change 0", out, 0)

    out = run_program([25, 10, 10, 5])
    assert_final_change("25 + 10 + 10 + 5 -> change 0", out, 0)


if __name__ == "__main__":
    main()
