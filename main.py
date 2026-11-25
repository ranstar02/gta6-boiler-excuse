"""The Excuse That Almost Works — make.fun bounty entry.

Writes the one-line excuse to /output/entry.txt (falling back to
./output/entry.txt if /output is not writable).
"""

import os

ENTRY = "Sorry, my boiler leaked onto the fuse box, electrician says don't touch anything till noon, I'll be in after"


def main():
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"

    out_path = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        with open(out_path, "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
    except OSError:
        out_path = "./output/entry.txt"
        os.makedirs("./output", exist_ok=True)
        with open(out_path, "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)

    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "round-trip mismatch"

    print(ENTRY)
    print("characters: %d" % len(ENTRY))
    print("words: %d" % len(ENTRY.split()))


if __name__ == "__main__":
    main()
