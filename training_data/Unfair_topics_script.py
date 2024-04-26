import csv

# Define the list of topics directly in the code
topics = [
    "Hidden Fees",
    "Sudden Changes to the Terms",
    "Interest Rate Changes",
    "Unfair loan conditions",
    "Credit terms"
    "Data Privacy",
    "Mandatory Arbitration",
    "Overdraft Policies",
    "Termination of Account and early termination",
    "Automatic Renewals",
    "Cross-Collateralization",
    "Waivers of Rights",
    "Rollover Clauses",
    "Non-Competitive Clauses",
    "Limitation of Liability",
    "Unilateral Changes to Benefits",
    "Opaque Handling of Disputes"
]

output_file = 'csv_files/unfair_terms_topics.csv'

# Define the string length ranges
length_ranges = ['5-15', '15-20', '20-40']

with open(output_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    # Generate three rows for each topic, with different string lengths
    for topic in topics:
        for length in length_ranges:
            new_row = [f"# Generate 10 strings {length} words in length for the topic: {topic}"]
            writer.writerow(new_row)

print("CSV file has been modified and saved as", output_file)
