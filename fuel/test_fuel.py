import os
import re
import subprocess

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

FUEL_FILE = "fuel.py"

# Match any percentage like "75%" anywhere in the output
PCT_RE = re.compile(r"(\d+)%")


def run_program(inputs):
    """Run fuel.py with a list of inputs and return full stdout."""
    data = "\n".join(inputs) + "\n"
    try:
        result = subprocess.run(
            ["python3", FUEL_FILE],
            input=data.encode(),
            capture_output=True,
            timeout=5,
        )
    except FileNotFoundError:
        return ""
    return result.stdout.decode()


def assert_percent(test_name, output, expected_pct):
    """Expect a numeric percentage like '75%' exactly (use the last occurrence)."""
    matches = PCT_RE.findall(output)
    if not matches:
        print(f"{RED}FAIL{RESET} {test_name}")
        print(f"   expected a percentage like '{expected_pct}%' but none was found")
        lines = output.splitlines()
        if lines:
            print("   last few lines:")
            for l in lines[-5:]:
                print("   ", l)
        else:
            print("   <no output>")
        return

    actual = int(matches[-1])
    if actual == expected_pct:
        print(f"{GREEN}PASS{RESET} {test_name}")
    else:
        print(f"{RED}FAIL{RESET} {test_name}")
        print(f"   expected: {expected_pct}%")
        print(f"   got:      {actual}%")


def assert_letter(test_name, output, expected_letter):
    """Expect 'E' or 'F' (use the last occurrence)."""
    # Tokenize to avoid matching letters inside words
    tokens = re.findall(r"[A-Za-z]+|[\S]", output)
    letters = [t for t in tokens if t in ("E", "F")]
    if not letters:
        print(f"{RED}FAIL{RESET} {test_name}")
        print(f"   expected: {expected_letter}")
        lines = output.splitlines()
        if lines:
            print("   last few lines:")
            for l in lines[-5:]:
                print("   ", l)
        else:
            print("   <no output>")
        return

    actual = letters[-1]
    if actual == expected_letter:
        print(f"{GREEN}PASS{RESET} {test_name}")
    else:
        print(f"{RED}FAIL{RESET} {test_name}")
        print(f"   expected: {expected_letter}")
        print(f"   got:      {actual}")


def main():
    if not os.path.exists(FUEL_FILE):
        print(
            f"{YELLOW}WARNING:{RESET} {FUEL_FILE} not found. Please create the file and start coding!"
        )
        return
    if os.path.getsize(FUEL_FILE) == 0:
        print(f"{YELLOW}NOTE:{RESET} {FUEL_FILE} is empty. Begin writing your program!")
        return

    # Straight valid inputs
    assert_percent("3/4 -> 75%", run_program(["3/4"]), 75)
    assert_percent("1/4 -> 25%", run_program(["1/4"]), 25)
    assert_letter("4/4 -> F", run_program(["4/4"]), "F")
    assert_letter("0/4 -> E", run_program(["0/4"]), "E")

    # Invalid first, then valid (re-prompts)
    assert_percent("4/0 then 1/4 -> 25%", run_program(["4/0", "1/4"]), 25)
    assert_percent("three/four then 3/4 -> 75%", run_program(["three/four", "3/4"]), 75)
    assert_percent("1.5/3 then 1/2 -> 50%", run_program(["1.5/3", "1/2"]), 50)
    assert_percent("-3/4 then 3/4 -> 75%", run_program(["-3/4", "3/4"]), 75)
    assert_percent("5/4 then 1/4 -> 25%", run_program(["5/4", "1/4"]), 25)


if __name__ == "__main__":
    main()
