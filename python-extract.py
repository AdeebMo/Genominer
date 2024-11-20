import os
import gzip
import shutil

# Paths to the input and output folders
input_folder = "./zipped_mt_datasets/"
output_folder = "./unzipped_mt_datasets/"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all .gz files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".gz"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename[:-3])  # Remove .gz extension

        # Extract the .gz file
        with gzip.open(input_path, 'rb') as f_in:
            with open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        print(f"Extracted: {filename} -> {output_path}")

print("Extraction complete.")
