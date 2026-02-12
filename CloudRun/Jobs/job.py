import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

INPUT_FILE = "input.txt"

def main():
    logging.info("Job started")

    # Check if file exists
    if not os.path.exists(INPUT_FILE):
        logging.error("Input file not found!")
        return

    # Read file
    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()

    count = len(lines)

    logging.info(f"Total lines in file: {count}")
    logging.info("Job completed successfully")

if __name__ == "__main__":
    main()
