import os
import csv

input_directory = "merged_columns"
output_file = "amazon_dataset.csv"
all_merged_data = []

csv_files = [file for file in os.listdir(input_directory) if file.endswith(".csv")]

for csv_file in csv_files:
    input_file_path = os.path.join(input_directory, csv_file)

    with open(input_file_path, "r", encoding="utf-8") as input_file:
        input_csv = csv.reader(input_file)
        next(input_csv, None)
        all_merged_data.extend(list(input_csv))

with open(output_file, "w", newline="", encoding="utf-8") as output_file:
    output_csv = csv.writer(output_file)
    output_csv.writerows(all_merged_data)

print(f"All CSV files in '{input_directory}' merged into '{output_file}'.")
