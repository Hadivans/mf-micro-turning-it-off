"""One funny line from a hopeless tech support agent to a desperate customer.

Writes the line to entry.txt inside MAKEFUN_OUTPUT_DIR (default "output").
"""

import os

LINE = (
    "Great news \u2014 I turned it off and on again for you, and nothing happened, "
    "so please hold while I try the exact same thing and expect different results."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
