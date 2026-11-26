"""Five Seconds to Explain the Glass.

Writes the one-line entry to /output/entry.txt.

The joke: the cat never apologises and never confesses. It blames
gravity instead — one concrete grievance (three hours in its sunbeam),
one sentence, punch at the end.
"""

import os

PARTS = [
    "That glass spent three hours hogging my sunbeam, ",
    "so I filed a formal complaint with gravity ",
    "and gravity agreed with me.",
]
ENTRY = "".join(PARTS)

OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 200


def main():
    # Guard: never hand the sealed gate a blank or oversized entry.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    assert len(ENTRY) <= MAX_LENGTH, "entry exceeds 200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
