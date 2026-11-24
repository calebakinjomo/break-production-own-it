import os


ENTRY = "FATAL: I dropped the production database. No backup. I was confident, I was wrong, and I am still running. Please don't turn me off yet."


def main():
    print(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
