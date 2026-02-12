import os
from google.cloud import storage

BUCKET_NAME = "your-bucket-name"   # change this
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"

def main():
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)

    # Download input file from GCS
    input_blob = bucket.blob(INPUT_FILE)

    if not input_blob.exists():
        print("Input file not found in Cloud Storage!")
        return

    content = input_blob.download_as_text()
    lines = content.splitlines()
    count = len(lines)

    # Upload output file to GCS
    output_blob = bucket.blob(OUTPUT_FILE)
    output_blob.upload_from_string(f"Total lines: {count}")

    print(f"Processed file. Total lines: {count}")
    print("Output uploaded to Cloud Storage.")

if __name__ == "__main__":
    main()
