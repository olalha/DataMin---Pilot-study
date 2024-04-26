import pandas as pd
import numpy as np

# Specify the number of rows to delete for each label
delete_count_1 = 111  # Number of '1' labeled rows to delete
delete_count_0 = 198  # Number of '0' labeled rows to delete

# Paths to the CSV files
file_path1 = 'csv_files/data_labelled_terms.csv'
file_path2 = 'csv_files/data_unfair_terms.csv'

# Load the CSV files
df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)

# Combine the dataframes
combined_df = pd.concat([df1, df2], ignore_index=True)

# Shuffle the combined dataframe
shuffled_df = combined_df.sample(frac=1).reset_index(drop=True)

# Drop specified number of rows for each label
if delete_count_1 > 0 and delete_count_0 > 0:
    filtered_df_1 = shuffled_df[shuffled_df.iloc[:, 0] == 1].drop(shuffled_df[shuffled_df.iloc[:, 0] == 1].sample(n=delete_count_1, random_state=1).index)
    filtered_df_0 = shuffled_df[shuffled_df.iloc[:, 0] == 0].drop(shuffled_df[shuffled_df.iloc[:, 0] == 0].sample(n=delete_count_0, random_state=1).index)

    # Combine the remaining data
    final_df = pd.concat([filtered_df_1, filtered_df_0]).sample(frac=1).reset_index(drop=True)
else:
    final_df = shuffled_df

# Save the final dataframe to a new CSV file
output_file = 'csv_files/combined_training_data.csv'
final_df.to_csv(output_file, index=False)

# Print the final counts of each type of row
final_count_1 = final_df[final_df.iloc[:, 0] == 1].shape[0]
final_count_0 = final_df[final_df.iloc[:, 0] == 0].shape[0]
print(f"Data has been processed and saved to {output_file}.")
print(f"Final counts - 1's: {final_count_1}, 0's: {final_count_0}")
