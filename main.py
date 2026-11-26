import os
from pathlib import Path

LINE = "Sorry, I heard 'set a timer' as 'set a tiger.' Please do not open the pantry."
OUTPUT_NAME = "entry.txt"


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / OUTPUT_NAME).write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
