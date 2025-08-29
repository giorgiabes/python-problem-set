import os
import re
import subprocess

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

TAQ_FILE = "taqueria.py"

TOTAL_RE = re.compile(r"Total:\s*\$(\d+\.\d{2})")


def run_program(inputs):
    """
    Run taqueria.py with a list of inputs and return full stdout.
    Ending the input list simulates EOF (Ctrl-D) in subprocess.
    """
    data = "\n".join(inputs) + "\n"
    try:
        result = subprocess.run(
            ["python3", TAQ_FILE],
            input=data.encode(),
            capture_output=True,
            timeout=5,
        )
    except FileNotFoundError:
        return ""
    return result.stdout.decode()


def assert_totals(test_name, output, expected_totals):
    """
    Extract all 'Total: $X.YY' amounts in order and compare with expected list of strings.
    """
    found = TOTAL_RE.findall(output)  # list of "X.YY" strings
    if found == expected_totals:
        print(f"{GREEN}PASS{RESET} {test_name}")
        return

    print(f"{RED}FAIL{RESET} {test_name}")
    print(f"   expected totals: {expected_totals}")
    print(f"   found totals:    {found}")
    lines = output.splitlines()
    if lines:
        print("   last few lines:")
        for l in lines[-8:]:
            print("   ", l)
    else:
        print("   <no output>")


def main():
    if not os.path.exists(TAQ_FILE):
        print(
            f"{YELLOW}WARNING:{RESET} {TAQ_FILE} not found. Please create the file and start coding!"
        )
        return
    if os.path.getsize(TAQ_FILE) == 0:
        print(f"{YELLOW}NOTE:{RESET} {TAQ_FILE} is empty. Begin writing your program!")
        return

    # Test 1: Taco + Taco -> $3.00 then $6.00
    out = run_program(["Taco", "Taco"])
    assert_totals("Taco twice -> $3.00, $6.00", out, ["3.00", "6.00"])

    # Test 2: Baja Taco + Tortilla Salad -> $4.25 then $12.25
    out = run_program(["Baja Taco", "Tortilla Salad"])
    assert_totals("Baja Taco + Tortilla Salad -> $4.25, $12.25", out, ["4.25", "12.25"])

    # Test 3: Invalid item ignored (Burger), then valid Super Quesadilla
    out = run_program(["Burger", "Super Quesadilla"])
    assert_totals("Invalid then Super Quesadilla -> $9.50", out, ["9.50"])

    # Test 4: Case-insensitive + extra spaces + multiple items
    out = run_program(["  nAcHos  ", "taco", "TACO", " Taco  ", ""])
    assert_totals(
        "Mixed casing + spaces + repeats", out, ["11.00", "14.00", "17.00", "20.00"]
    )

    # Test 5: Single item then EOF -> one total
    out = run_program(["Burrito"])
    assert_totals("EOF after one item -> $7.50", out, ["7.50"])


if __name__ == "__main__":
    main()
