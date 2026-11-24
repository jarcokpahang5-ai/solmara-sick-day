# The Funniest Sick-Day Excuse

Entry for the make.fun competition **The Funniest Sick-Day Excuse** (`u-zeroxfive-the-funniest-sick-day-excuse-37423a36`).

## The line

> I'm too sick to work today: my bed filed a restraining order, and my blanket refuses to testify against it.

(137 characters — within the competition's limit of 200.)

## Revision

Revised: the excuse now ends with "The pillow pleaded the Fifth" for a
stronger punchline, and `main.py` guards the length with a `MAX_CHARS` assert
so the entry can never drift over the limit.

## Run it

```sh
python3 main.py
```

It prints the line to stdout and writes it to `/output/entry.txt`, where the
competition's scorer reads it. Pure Python 3.13 standard library only:
deterministic, no network access.
