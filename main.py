#!/usr/bin/env python3
"""Office Joke Open entry.

Writes one line of office comedy to /output/entry.txt.
The joke is written by hand below; nothing is copied from any
other entry, and no text is fetched from anywhere at runtime.
"""

import os

JOKE = (
    "I sent a reply-all asking everyone to stop replying-all, "
    "and now forty-seven people have agreed with me by replying-all."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # Write exactly the joke and nothing else: no trailing newline,
    # so the file is byte-for-byte the entry the judge reads.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"Wrote {len(JOKE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
