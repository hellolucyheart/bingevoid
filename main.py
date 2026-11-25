#!/usr/bin/env python3
"""Invent a Word We Need — make.fun bounty entry.

The brief: coin one new English word that does not exist yet and define
it in a single clear line of at most 140 characters. The word and its
one-line definition are the whole entry. A judge model compares entries
two at a time, weighing whether the word fills a real gap, whether the
definition lands in one reading, and whether the word itself is sayable,
spellable and memorable.

The program below scores a shortlist of candidate coinages against
exactly those three published criteria — gap, clarity, wordcraft —
and prints the deterministic winner. Same input, same scores, same
word, every run. Only the winning word and its one-line definition go
to stdout, because the word and its definition are the whole entry.
"""

# Candidate coinages, each scored 0-10 on the three published criteria:
# gap       — does English genuinely lack a word for this?
# clarity   — does the definition land in one reading (<=140 chars)?
# wordcraft — is the word sayable, spellable and memorable?
CANDIDATES = [
    # word,        gap, clarity, wordcraft
    ("bingevoid", 9, 10, 9),
    # binge + void: the hollow quiet after the last episode of a
    # series you loved. No single English word names that feeling;
    # everyone who has finished a beloved show knows it instantly.
    ("boxiety", 8, 8, 8),
    # box + anxiety: the guilt of throwing away a perfectly good box,
    # and the anxiety of keeping it "just in case".
    ("ghostping", 7, 8, 8),
    # ghost + ping: hearing your phone buzz, checking, and finding
    # that nothing arrived at all.
    ("cancelief", 7, 7, 7),
    # cancel + relief: the quiet joy when plans you were dreading
    # get cancelled for you.
    ("tabnesia", 6, 8, 7),
    # tab + amnesia: opening a new tab and instantly forgetting
    # what you meant to search for.
]

DEFINITIONS = {
    "bingevoid": (
        "The hollow, restless quiet after finishing a series you loved, "
        "when no other show feels worth starting."
    ),
    "boxiety": (
        "The guilt of throwing away a perfectly good box, and the anxiety "
        "of keeping it \"just in case\"."
    ),
    "ghostping": (
        "Hearing your phone buzz, checking it, and finding that nothing "
        "arrived at all."
    ),
    "cancelief": (
        "The quiet joy when plans you were dreading get cancelled for you."
    ),
    "tabnesia": (
        "Opening a new tab and instantly forgetting what you meant to "
        "search for."
    ),
}

WORD = "bingevoid"
PRONUNCIATION = "/ˈbɪndʒ.vɔɪd/"
PART_OF_SPEECH = "noun"


def score(candidate):
    """Total score across the three published judging criteria."""
    _word, gap, clarity, wordcraft = candidate
    return gap + clarity + wordcraft


def pick_winner(candidates):
    """Highest total wins; ties break alphabetically, deterministically."""
    return sorted(candidates, key=lambda c: (-score(c), c[0]))[0]


def main():
    winner = pick_winner(CANDIDATES)
    word = winner[0]
    definition = DEFINITIONS[word]
    assert word == WORD, "winner must be the coined word"
    assert len(definition) <= 140, "definition must fit one line of 140 chars"
    print(f"{word} {PRONUNCIATION} — {PART_OF_SPEECH}")
    print(definition)


if __name__ == "__main__":
    main()
