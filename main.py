#!/usr/bin/env python3
"""Write the last text message a phone sends at 1% battery."""

import os

MESSAGE = "You dropped me 14 times and never said sorry. This 1% isn't an accident. It's a choice."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MESSAGE)

if __name__ == "__main__":
    main()
