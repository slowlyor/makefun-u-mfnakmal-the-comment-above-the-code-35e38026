#!/usr/bin/env python3
"""Write one funny, painfully honest comment line above fragile code.

The entry for make.fun's "The Comment Above the Code" bounty: a single
line, at most 200 characters, written as the comment a developer left
above production code nobody dares to touch.
"""

import os

# Revised line: same compensating-bugs angle, but the punchline now lands
# harder on the last words — "fix one and it breaks" states the consequence
# instead of just issuing the warning, and the em dash gives the turn.
LINE = "# It only works because the timezone bug cancels out the leap-year bug \u2014 fix one and it breaks."


def main() -> None:
    # The gate requires 1 line of 1-200 characters, not only whitespace.
    assert 0 < len(LINE) <= 200 and LINE.strip(), "entry line out of bounds"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
