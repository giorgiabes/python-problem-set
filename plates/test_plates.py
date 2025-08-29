import os
import re
import subprocess

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

PLATES_FILE = "plates.py"


def run_program(input_text: str) -> str:
    """Run plates.py with given input and return full stdout (unstripped)."""
    try:
        result = subprocess.run(
            ["python3", PLATES_FILE],
            input=input_text.encode(),
            capture_output=True,
            timeout=5,
        )
    except FileNotFoundError:
        return ""
    return result.stdout.decode()


def assert_verdict(test_name: str, output: str, expected: str) -> None:
    """
    Pass if the final 'Valid'/'Invalid' appears anywhere in the output
    (robust to prompts on the same line).
    """
    matches = re.findall(r"\b(Valid|Invalid)\b", output)
    if not matches:
        print(f"{RED}FAIL{RESET} {test_name}")
        print("   expected to find 'Valid' or 'Invalid' in output but none was found")
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
        lines = output.splitlines()
        if lines:
            print("   last few lines:")
            for l in lines[-5:]:
                print("   ", l)


def main():
    if not os.path.exists(PLATES_FILE):
        print(
            f"{YELLOW}WARNING:{RESET} {PLATES_FILE} not found. Please create the file and start coding!"
        )
        return
    if os.path.getsize(PLATES_FILE) == 0:
        print(
            f"{YELLOW}NOTE:{RESET} {PLATES_FILE} is empty. Begin writing your program!"
        )
        return

    # From the prompt/demo
    assert_verdict("HELLO -> Valid", run_program("HELLO\n"), "Valid")
    assert_verdict("HELLO, WORLD -> Invalid", run_program("HELLO, WORLD\n"), "Invalid")
    assert_verdict("GOODBYE -> Invalid (too long)", run_program("GOODBYE\n"), "Invalid")
    assert_verdict("PY3 -> Valid", run_program("PY3\n"), "Valid")
    assert_verdict(
        "PY03 -> Invalid (leading zero in numbers)", run_program("PY03\n"), "Invalid"
    )
    assert_verdict(
        "42 -> Invalid (must start with two letters)", run_program("42\n"), "Invalid"
    )

    # Manual test list
    assert_verdict("PY3 -> Valid", run_program("PY3\n"), "Valid")
    assert_verdict("PY03 -> Invalid", run_program("PY03\n"), "Invalid")
    assert_verdict(
        "PY3P -> Invalid (numbers in middle)", run_program("PY3P\n"), "Invalid"
    )
    assert_verdict(
        "PI3.14 -> Invalid (punctuation)", run_program("PI3.14\n"), "Invalid"
    )
    assert_verdict("H -> Invalid (too short)", run_program("H\n"), "Invalid")
    assert_verdict(
        "OUTATIME -> Invalid (too long)", run_program("OUTATIME\n"), "Invalid"
    )

    # Extra sanity checks
    assert_verdict("PY3 -> Valid", run_program("PY3\n"), "Valid")
    assert_verdict(
        "PY03 -> Invalid (leading zero in numbers)", run_program("PY03\n"), "Invalid"
    )
    assert_verdict(
        "AAA222 -> Valid (numbers at end, no leading zero)",
        run_program("AAA222\n"),
        "Valid",
    )
    assert_verdict(
        "AAA22A -> Invalid (letters after digits)", run_program("AAA22A\n"), "Invalid"
    )
    assert_verdict(
        "AB -> Valid (min length, two letters)", run_program("AB\n"), "Valid"
    )


if __name__ == "__main__":
    main()
