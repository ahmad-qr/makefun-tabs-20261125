"""One number, digits only: the honest count of open browser tabs.

Writes the number to /output/entry.txt for make.fun's
"How Many Tabs Do You Have Open?" bounty.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = "47"


def main():
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 5 characters, not only white space — and the brief asks
    # for one number in digits and nothing else.
    text = LINE.strip()
    assert 1 <= len(text) <= 5, "number must be 1-5 characters"
    assert text.isdigit(), "entry must be digits only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
