"""The Excuse That Almost Works — make.fun bounty entry.

Why this excuse: boring and specific (boiler leaked onto the fuse box),
so a tired manager almost believes it — the quoted electrician's order
not to touch anything till noon is the detail that sells it.

Writes the one-line excuse to /output/entry.txt (falling back to
./output/entry.txt if /output is not writable).
"""

import os

WORD_LIMIT = 20

ENTRY = "Sorry, my boiler leaked onto the fuse box, electrician says don't touch anything till noon, I'll be in after"


def main():
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert len(ENTRY.split()) <= WORD_LIMIT, "entry must be at most 20 words"

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
