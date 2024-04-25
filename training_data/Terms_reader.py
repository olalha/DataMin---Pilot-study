import csv
import os
import re

# Replace newlines within paragraphs with a space, retaining newlines for bullet points and numbers
def preprocess_text(text):
    pattern = r'\n(?!\s*(\(\w+\)|\d+\.|[\u2022\u2023\u25E6\u2043•\-]))'
    return re.sub(pattern, ' ', text)

# Remove quotes, various unwanted characters, and leading bullet points or numbers
def clean_term(term):
    
    # Remove quotation marks
    term = re.sub(r'[“”"]', '', term)
    # Remove specific punctuation
    term = re.sub(r'[:;,!?(){}[\]–—]', '', term)
    # Remove leading bullet points
    term = re.sub(r'^\s*[\u2022\u2023\u25E6\u2043•\-]+', '', term)
    # Remove leading numbering and lettering
    term = re.sub(r'^\s*([a-z]|\d|(?=i+v*|v+|i*x)(i{1,3}|i?x|vi{0,3}|iv))\b\.?\s*', '', term, flags=re.IGNORECASE)
    # Remove whitespaces
    term = re.sub(r'\s+', ' ', term).strip()
    return term

# Split text into sentences considering punctuation and capital letters that follow
def split_sentences(text):
    return re.split(r'(?<=[.!?]) +(?=[A-Z])', text)

# Extract and filter terms from processed text
def extract_terms(text):
    terms = []
    sentences = split_sentences(text)
    for sentence in sentences:
        if sentence:
            points = sentence.split('\n')
            for point in points:
                if len(point.split()) >= 3:
                    clean_point = clean_term(point)
                    if clean_point:
                        terms.append(clean_point)
    return terms

# Write processed terms to a CSV file in append mode
def write_terms_to_csv(terms, filename):
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONE)
        for term in terms:
            writer.writerow([term])

# Process all text files within the specified directory and append all terms to a CSV file
def process_files(directory, output_file):
    all_terms = []
    if not os.path.exists(directory):
        print(f"Directory does not exist: {directory}")
        return

    files_processed = 0
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            files_processed += 1
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                text = file.read()
                processed_text = preprocess_text(text)
                terms = extract_terms(processed_text)
                all_terms.extend(terms)
    write_terms_to_csv(all_terms, output_file)
    print(f"Processed {files_processed} files.")

def main():
    folder_path = './raw_contract_data'
    output_csv = './csv_files/data_formatted_terms.csv'
    if os.path.exists(output_csv):
        os.remove(output_csv)
    process_files(folder_path, output_csv)
    print("Terms extraction completed and stored in", output_csv)

if __name__ == '__main__':
    main()
