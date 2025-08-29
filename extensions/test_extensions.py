import os
import re
import subprocess

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

EXT_FILE = "extensions.py"

# All media types we expect from the assignment
MEDIA_RE = re.compile(
    r"(image/(gif|jpeg|png)|application/(pdf|zip|octet-stream)|text/plain)"
)


def run_program(input_text: str) -> str:
    """Run extensions.py with given input and return full stdout (unstripped)."""
    try:
        result = subprocess.run(
            ["python3", EXT_FILE],
            input=input_text.encode(),
            capture_output=True,
            timeout=5,
        )
    except FileNotFoundError:
        return ""
    return result.stdout.decode()


def assert_type(test_name: str, output: str, expected_type: str) -> None:
    """
    Find the last media type in output (handles cases like 'File name: image/jpeg')
    and compare with expected_type.
    """
    matches = MEDIA_RE.findall(output)
    if not matches:
        print(f"{RED}FAIL{RESET} {test_name}")
        print("   expected to find a media type but none was found")
        lines = output.splitlines()
        if lines:
            print("   last few lines:")
            for l in lines[-5:]:
                print("   ", l)
        else:
            print("   <no output>")
        return

    # Each match is a tuple; the full match is at index 0
    actual = [m[0] for m in matches][-1]
    if actual == expected_type:
        print(f"{GREEN}PASS{RESET} {test_name}")
    else:
        print(f"{RED}FAIL{RESET} {test_name}")
        print(f"   expected: {expected_type}")
        print(f"   got:      {actual}")


def main():
    # Friendly handling if extensions.py doesn't exist or is empty
    if not os.path.exists(EXT_FILE):
        print(
            f"{YELLOW}WARNING:{RESET} {EXT_FILE} not found. Please create the file and start coding!"
        )
        return
    if os.path.getsize(EXT_FILE) == 0:
        print(f"{YELLOW}NOTE:{RESET} {EXT_FILE} is empty. Begin writing your program!")
        return

    # Core tests from the spec
    assert_type("jpg -> image/jpeg", run_program("happy.jpg\n"), "image/jpeg")
    assert_type("jpeg -> image/jpeg", run_program("photo.JPEG\n"), "image/jpeg")
    assert_type("gif -> image/gif", run_program("cat.Gif\n"), "image/gif")
    assert_type("png -> image/png", run_program("logo.PNG\n"), "image/png")
    assert_type(
        "pdf -> application/pdf", run_program("document.pdf\n"), "application/pdf"
    )
    assert_type("txt -> text/plain", run_program("notes.TXT\n"), "text/plain")
    assert_type(
        "zip -> application/zip", run_program("archive.ZIP\n"), "application/zip"
    )

    # No/unknown extension -> default
    assert_type(
        "no extension -> octet-stream",
        run_program("picture\n"),
        "application/octet-stream",
    )
    assert_type(
        "unknown ext -> octet-stream",
        run_program("file.weird\n"),
        "application/octet-stream",
    )

    # Whitespace & casing robustness
    assert_type("spaces & casing", run_program("   ReSuMe.PdF   \n"), "application/pdf")


if __name__ == "__main__":
    main()
