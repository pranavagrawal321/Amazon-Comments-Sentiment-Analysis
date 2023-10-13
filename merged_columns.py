import os
import csv

input_directory = 'amazon_reviews'
output_directory = 'merged_columns'

os.makedirs(output_directory, exist_ok=True)

file_data = {}
csv_files = [file for file in os.listdir(input_directory) if file.endswith('.csv')]

for csv_file in csv_files:
    file_name = os.path.splitext(csv_file)[0]

    if file_name not in file_data:
        file_data[file_name] = []

    input_file_path = os.path.join(input_directory, csv_file)

    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        input_csv = csv.reader(input_file)

        for row in input_csv:
            merged_row = row[:3] + [''.join(row[3:])]
            file_data[file_name].append(merged_row)

for file_name, data in file_data.items():
    output_file_path = os.path.join(output_directory, f"{file_name}.csv")

    with open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:
        output_csv = csv.writer(output_file)
        output_csv.writerows(data)

print("CSV files merged and saved in the 'merged_columns' folder.")
