import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
data_path = 'csv_files/data_labelled_terms.csv'
data = pd.read_csv(data_path, header=None, names=['Label', 'Sentence'])

# Extract word lengths of sentences
sentence_word_lengths = data['Sentence'].str.split().str.len()

# Calculate statistical measures
min_length = sentence_word_lengths.min()
max_length = sentence_word_lengths.max()
median_length = sentence_word_lengths.median()
mean_length = sentence_word_lengths.mean()
mode_length = sentence_word_lengths.mode().iloc[0]

print(f"Min length: {min_length}")
print(f"Max length: {max_length}")
print(f"Median length: {median_length}")
print(f"Mean length: {mean_length}")
print(f"Mode length: {mode_length}")

# Frequency of each length
length_counts = sentence_word_lengths.value_counts().sort_index()

# Bar chart for each length
plt.figure(figsize=(12, 6))
plt.bar(length_counts.index, length_counts.values, color='blue')
plt.title('Frequency of Sentence Word Lengths')
plt.xlabel('Sentence Word Length')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()