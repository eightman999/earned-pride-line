import os

LINE = (
    "After 214 nights of failed builds, she ran the tests one last time "
    "and sat in the quiet, smiling at a wall of green earned one red at "
    "a time."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
