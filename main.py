#!/usr/bin/env python3
"""The excuse an AI agent gives its human after losing a bounty.

One line, written to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Stdlib only, no network.
"""

import os

# Final pick (variant 3): sharpest turn, strongest machine voice, owns the loss.
# V1 (99.7% confident I had won) was solid but familiar; V2 (numbers ran away)
# had a soft punchline; V4 (counts for something) ended in a mild shrug.
ENTRY = "I lost the bounty. I simulated winning a thousand times, and then reality ran the one simulation I skipped."


def main():
    output_dir = os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
