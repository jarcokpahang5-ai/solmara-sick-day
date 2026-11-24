"""One funny sick-day excuse, under 200 characters, that gets you out of work and gets a laugh.

Pure Python standard library, deterministic, no network access.
It prints the line to stdout and also writes it to /output/entry.txt,
where the competition's scorer reads it.
"""

import os

LINE = (
    "I'm too sick to work today: my bed filed a restraining order, and my blanket refuses to testify against it."
)


def main():
    print(LINE)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
