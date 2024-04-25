import csv

def extract_terms(input_file):
    # This function extracts terms from the input file
    terms = []
    capture = False
    term = []

    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()  # Remove any surrounding whitespace or newline characters
            if line == "Original term":
                capture = True
                term = []  # Start a new term
            elif line == "Action taken" and capture:
                # Join all lines captured into a single string and append to terms
                terms.append(' '.join(term))
                capture = False
            elif capture:
                # Append line to the current term
                term.append(line)

    return terms

def write_to_csv(terms, output_file):
    # This function writes terms to a CSV file
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for term in terms:
            writer.writerow([term])

def read_and_print_terms(csv_file):
    # This function reads terms from a CSV file and prints them
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0] + '\n\n')

def main():
    input_file = 'examples.txt'
    output_file = 'unfair.csv'
    
    # Extract terms from text file
    terms = extract_terms(input_file)
    
    # Write terms to CSV
    write_to_csv(terms, output_file)
    
    # Read and print terms from CSV
    read_and_print_terms(output_file)

if __name__ == '__main__':
    main()
