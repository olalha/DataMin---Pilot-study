import csv
import requests
import json
import re

# OLD KEY - OPENROUTER_API_KEY = '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'
OPENROUTER_API_KEY = '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'
MODEL = "google/gemini-pro-1.5"

BATCH_SIZE = 1
MAX_BATCHES = 1

READ_FILE = 'csv_files/unfair_terms_topics.csv'
WRITE_FILE = 'csv_files/data_unfair_terms.csv'
MESSAGE_FILE = 'Task_message_unfair_terms.md'

# Reads the initial message from a file
def read_initial_message(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()

# Sends a combined message of initial_message and batch_terms to the chatbot API
def send_message(initial_message, batch_terms):
    full_message = initial_message + '\n' + '\n'.join(batch_terms)
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}"},
        data=json.dumps({
            "model": MODEL,
            "messages": [{"role": "user", "content": full_message}]
        })
    )
    return response.json() if response.status_code == 200 else {'choices': []}

# Processes batches of terms, sending them through the send_message function
def process_batches(terms, initial_message):
    batch_count = 0
    total_terms = len(terms)
    
    # Iterate through the list of terms in chunks defined by BATCH_SIZE
    for start in range(0, total_terms, BATCH_SIZE):
        if batch_count >= MAX_BATCHES:
            break
        end = min(start + BATCH_SIZE, total_terms)
        batch_terms = [terms[i][0] for i in range(start, end)]
        response = send_message(initial_message, batch_terms)
        choices = response.get('choices', [])
        labelled_data = []
        
        # Iterate through each choice to extract and process the returned messages
        for choice in choices:
            content = choice.get('message', {}).get('content', '').split('\n')
            
            # Parse each line of the returned message content for processing
            for line in content:
                if line and line[0] in '01':
                    if len(re.findall(r'\w+', line)) <= 40 and len(re.findall(r'\w+', line)) >= 5:
                        label, text = line[0], line[1:].strip().replace(',', '')
                        labelled_data.append([label, text])
                else:
                    if line != "":
                        print(f"Error: {line}")
        save_results(labelled_data)
        print(f"Batch {batch_count + 1} complete")
        batch_count += 1

# Saves the processed and labelled data into a CSV file
def save_results(labelled_data):
    with open(WRITE_FILE, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONE, escapechar='\\')
        writer.writerows(labelled_data)

# Main function to read initial message, process batches, and handle file operations
def main():
    initial_message = read_initial_message(MESSAGE_FILE)
    with open(READ_FILE, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        terms = list(reader)

    process_batches(terms, initial_message)
    print("Classification completed and results saved.")

if __name__ == "__main__":
    main()
