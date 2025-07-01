import os
import json

# Input and output paths
input_dir = "onprintshop_docs"
output_file = "onprintshop_knowledge.jsonl"

print(f"Starting to create {output_file} from {input_dir}...")

# Ensure the input directory exists and contains files
if not os.path.exists(input_dir) or not os.listdir(input_dir):
    print(f"Error: No documents found in '{input_dir}'. Please run scraper.py first.")
    exit() # Stop the script if no docs are found

with open(output_file, "w", encoding="utf-8") as out_f:
    for filename in os.listdir(input_dir):
        filepath = os.path.join(input_dir, filename)
        if filename.endswith(".txt"):
            print(f"Processing: {filename}")
            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    clean_line = line.strip()
                    if clean_line:
                        # Write each non-empty line as a separate JSON object
                        out_f.write(json.dumps({"text": clean_line}) + "\n")
print(f"✅ JSONL file created: {output_file}")
