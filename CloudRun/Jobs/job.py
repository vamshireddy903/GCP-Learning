import os

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"

def main():
    if not os.path.exists(INPUT_FILE):
        print("Input file not found!")
        return

    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()

    count = len(lines)

    with open(OUTPUT_FILE, "w") as f:
        f.write(f"Total lines: {count}")

    print(f"Processed file. Total lines: {count}")

if __name__ == "__main__":
    main()
