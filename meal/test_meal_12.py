import os
import re
import subprocess

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

MEAL_FILE = "meal.py"


def run_program(input_text: str) -> str:
    """Run meal.py with given input and return full stdout."""
    try:
        result = subprocess.run(
            ["python3", MEAL_FILE],
            input=input_text.encode(),
            capture_output=True,
            timeout=5,
        )
    except FileNotFoundError:
        return ""
    return result.stdout.decode()


def assert_has(test_name: str, output: str, expected: str) -> None:
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


def assert_none(test_name: str, output: str) -> None:
    meal_keywords = ("breakfast time", "lunch time", "dinner time")
    if any(kw in output for kw in meal_keywords):
        print(f"{RED}FAIL{RESET} {test_name}")
        print("   expected no meal output, but found one")
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
    if not os.path.exists(MEAL_FILE):
        print(
            f"{YELLOW}WARNING:{RESET} {MEAL_FILE} not found. Please create the file and start coding!"
        )
        return
    if os.path.getsize(MEAL_FILE) == 0:
        print(f"{YELLOW}NOTE:{RESET} {MEAL_FILE} is empty. Begin writing your program!")
        return

    # 24-hour format tests
    assert_has("7:00 breakfast", run_program("7:00\n"), "breakfast time")
    assert_has("7:30 breakfast", run_program("7:30\n"), "breakfast time")
    assert_has("12:42 lunch", run_program("12:42\n"), "lunch time")
    assert_has("18:32 dinner", run_program("18:32\n"), "dinner time")
    assert_none("11:11 none", run_program("11:11\n"))

    # 12-hour format tests
    assert_has("7:00 a.m. breakfast", run_program("7:00 a.m.\n"), "breakfast time")
    assert_has("7:30 AM breakfast", run_program("7:30 AM\n"), "breakfast time")
    assert_has("12:30 p.m. lunch", run_program("12:30 p.m.\n"), "lunch time")
    assert_has("6:15 pm dinner", run_program("6:15 pm\n"), "dinner time")
    assert_none("12:00 a.m. none", run_program("12:00 a.m.\n"))
    assert_has("12:00 p.m. lunch", run_program("12:00 p.m.\n"), "lunch time")


if __name__ == "__main__":
    main()
