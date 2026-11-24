#!/usr/bin/env python3
"""Variant A — SELF-DEFENSE. The dog ate the homework because the homework
attacked first. Dog as innocent victim, zero guilt.

Iteration log — ONE concept (self-defense vs the maths worksheet), v1-v8.
The final line is ENTRY below.

v1 (110 chars): "The maths worksheet growled at me first, so I defended myself.
    What was I supposed to do, just let it bite me?"
    Lost: ends on a rhetorical question — the dog sounds like it's pleading
    its case to a human, not a dog who believes it did nothing wrong. No
    concrete evidence, no defiant closer.

v2 (108 chars): "The maths worksheet lunged at me first, corners up, teeth
    out. I defended myself. Any dog would do the same."
    Lost: "corners up, teeth out" is a good image, but the closer "any dog
    would do the same" is generic committee-speak, not dog logic. The dog
    defers to other dogs instead of owning it.

v3 (104 chars): "It wasn't eating, it was self-defense — the maths worksheet
    growled, bared its corners and bit me first."
    Lost: opens meta ("It wasn't eating...") — a legal defence, not a dog
    talking. No scene, no punchline, reads like a lawyer's note.

v4 (105 chars): "The maths worksheet bit me first. I only ate it back because
    it started it. Ask the worksheet — it knows."
    Lost: "ask the worksheet" is cute but the worksheet can't talk, so the
    joke dead-ends on an impossibility instead of landing. "I only ate it
    back" is also mealy-mouthed — the dog is apologising.

v5 (125 chars): "The maths worksheet attacked me first — it growled, it
    snapped, it drew blood. I ate it in self-defense, and I'd do it again."
    Lost: "drew blood" is too graphic for a one-line dog joke and "attacked"
    is vaguer than "bit". Strong closer ("I'd do it again") but the middle
    over-sells the violence and loses the laugh.

v6 (122 chars): "Look at the bite marks on my nose: the maths worksheet
    attacked ME first. Eating it was self-defense, and I'd do it again."
    Lost: "Look at..." lectures the reader; "attacked ME" shouts instead of
    showing. The bite-marks-on-the-nose evidence is the right idea, but the
    delivery scolds rather than charms.

v7 (121 chars): "The maths worksheet bit me first, right on the nose. I ate
    it in self-defense. Any dog in my paws would've done the same."
    Lost: "any dog in my paws" is a pun that tries too hard and lands as a
    human joke, not dog logic. Closer defers to other dogs again (see v2).

v8 (113 chars, CHOSEN): "The maths worksheet bit me first — see the teeth
    marks on my nose? I ate it in self-defense, and I'd do it again."
    Wins: one concrete scene (a named artifact, the maths worksheet, with
    teeth) + one surprising turn (the homework bit the DOG). The evidence
    is visual and dog-logical — teeth marks on the nose prove the worksheet
    started it. "I'd do it again" is the defiant, zero-guilt closer the
    judge brief asks for: a dog who believes it has done nothing wrong.
    No stock lines (no cat, no taste of paper, no good boy), no setup
    needed, 113 chars in the joke sweet spot.
"""

import os

ENTRY = (
    "The maths worksheet bit me first \u2014 see the teeth marks on my nose? "
    "I ate it in self-defense, and I'd do it again."
)


def main() -> None:
    text = ENTRY
    # Gate validation (mirrors the sealed scorer): 1-200 chars, single line,
    # not whitespace-only, no leading/trailing whitespace, no double spaces.
    assert isinstance(text, str) and 1 <= len(text) <= 200, "length out of range"
    assert "\n" not in text and "\r" not in text, "must be a single line"
    assert text == text.strip(), "leading/trailing whitespace"
    assert "  " not in text, "double space"
    assert text.strip(), "whitespace-only"

    # Write ONLY to /output — never to the repo root (the grader sandbox
    # mounts the repo read-only; a repo-root write crashes with exit code 1).
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
