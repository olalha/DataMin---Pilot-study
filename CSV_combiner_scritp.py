import csv
import random

# File paths and deletion counts
file_path1 = 'csv_files/data_labelled_terms.csv'
file_path2 = 'csv_files/data_unfair_terms.csv'
output_file = 'csv_files/combined_training_data.csv'

delete_count_1 = 113  # Number of '1' labeled rows to delete
delete_count_0 = 198  # Number of '0' labeled rows to delete

# Initialize an empty 2D array to store the data
data = []

# Read data line by line from both files
for file_path in [file_path1, file_path2]:
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            # Remove leading/trailing commas (adjust based on actual comma positions)
            row = [item.strip(',') for item in row]  

            # Remove full stop from the end of the second column if present 
            if row[1].endswith('.'):
                row[1] = row[1][:-1] 

            data.append(row)

# Separate data by label
data_1 = [row for row in data if row[0] == '1']
data_0 = [row for row in data if row[0] == '0']

# Randomly delete rows
random.shuffle(data_1)
random.shuffle(data_0)
data_1 = data_1[:-delete_count_1]
data_0 = data_0[:-delete_count_0]

# Combine and shuffle data
final_data = data_1 + data_0
random.shuffle(final_data)

# Write to the new CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(final_data)

# Count rows for each label
count_1 = sum(row[0] == '1' for row in final_data)
count_0 = sum(row[0] == '0' for row in final_data)

print(f"Merged and processed data saved to: {output_file}")
print(f"Number of rows with label '1': {count_1}")
print(f"Number of rows with label '0': {count_0}")
