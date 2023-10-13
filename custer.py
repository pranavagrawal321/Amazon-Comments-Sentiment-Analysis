import os

# Create a directory to store the files
if not os.path.exists("output_files"):
    os.makedirs("output_files")

# Read the asin.txt file
with open("asin.txt", "r") as asin_file:
    lines = asin_file.readlines()

# Split the lines into chunks of 150
chunk_size = 150
chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]

# Write each chunk to a separate file
for i, chunk in enumerate(chunks):
    with open(f"output_files/output_{i+1}.txt", "w") as output_file:
        output_file.writelines(chunk)
