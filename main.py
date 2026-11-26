"""Five Seconds to Explain the Glass: writes the entry text to /output/entry.txt.

Why this line: the cat never apologises and never confesses — it blames
gravity. One concrete grievance (three hours in its sunbeam), one sentence,
punch at the end.
"""

import os

# The entry itself: one sentence, in the cat's own voice.
ENTRY = 'That glass spent three hours hogging my sunbeam, so I filed a formal complaint with gravity and gravity agreed with me.'

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    assert len(ENTRY) <= 200, "entry exceeds 200 characters"
    assert ENTRY.count("\n") == 0, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
