import os
import json

input_dir = "onprintshop_docs"
output_file = "onprintshop_knowledge.jsonl"

with open(output_file, "w") as out_f:
    for filename in os.listdir(input_dir):
        filepath = os.path.join(input_dir, filename)
        if filename.endswith(".txt"):
            with open(filepath, "r") as f:
                lines = f.readlines()
                for line in lines:
                    clean_line = line.strip()
                    if clean_line:
                        out_f.write(json.dumps({"text": clean_line}) + "\n")

print(f"✅ JSONL file created: {output_file}")