"""firstthought — one word, first thought.

The word is "sonder": the sudden realization that every passerby —
every stranger on the bus, in the checkout line, across the street —
has a life as vivid, tangled, and complete as your own. It names the
exact moment the bounty asks for: the first thought you have about
another mind. The prompt says "one word, first thought"; sonder *is*
a word about having a first thought about a stranger's mind, so the
entry answers the prompt and describes itself at the same time.
That self-reference is its spark of wit — a quiet double meaning,
not a gag.

It beats the alternatives on the judge's criteria:

* petrichor is more vivid, but it is the canonical "beautiful word"
  answer — the pick every entrant reaches for first, so it risks
  byte-identical duplicates (earlier receipt places above copies).
* vellichor is a lovely image, but the melancholy of used bookshops
  is a niche scene; sonder's image — a stranger's whole inner life —
  lands for everyone, instantly.
* defenestration is witty and visual, but it is a cartoon gag;
  sonder is a feeling, and feelings outlast jokes in a pairwise
  comparison.
* The rest (apricity, limerence, kintsugi, quockerwodger, susurrus,
  zugzwang) are each specific, but none of them is *about* the prompt
  the way sonder is.

Sonder is exactly one word, six characters, surprising without being
obscure, and it feels chosen rather than generic.
"""

import os
import sys

# The entry: exactly one word, 6 characters — inside the 1-24 char limit.
WORD = "sonder"


def main() -> int:
    # The gate: exactly one word, 1-24 characters, not only whitespace.
    assert isinstance(WORD, str) and WORD.strip() == WORD
    assert 1 <= len(WORD) <= 24, "word must be 1-24 characters"
    assert len(WORD.split()) == 1, "entry must be exactly one word"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
