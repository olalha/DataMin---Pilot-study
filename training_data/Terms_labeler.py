import csv
import requests
import json

# Constants
OPENROUTER_API_KEY = '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'
BATCH_SIZE = 30
MAX_BATCHES = 1

def read_initial_message(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()

def send_message(initial_message, batch_terms):
    """
    Send a combined message of initial_message and batch_terms as a single string to the chatbot API.
    """
    # Combine initial_message with batch_terms separated by new lines
    full_message = initial_message + '\n' + '\n'.join(batch_terms)
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}"},
        data=json.dumps({
            "model": "openai/gpt-4-turbo",
            "messages": [{"role": "user", "content": full_message}]
        })
    )
    return response.json() if response.status_code == 200 else {'choices': []}

def process_batches(terms, initial_message):
    labelled_data = []
    batch_count = 0
    total_terms = len(terms)
    for start in range(0, total_terms, BATCH_SIZE):
        if batch_count >= MAX_BATCHES:
            break
        end = min(start + BATCH_SIZE, total_terms)
        batch_terms = [terms[i][0] for i in range(start, end)]  # Access each term in the sublist of terms
        response = send_message(initial_message, batch_terms)
        choices = response.get('choices', [])
        for choice in choices:
            content = choice.get('message', {}).get('content', '')
            labelled_data.extend(content.split('\n'))  # Split content by new lines
        batch_count += 1
    return labelled_data

def save_results(labelled_data):
    with open('csv_files/data_labelled_terms.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONE, escapechar='\\')
        for line in labelled_data:
            writer.writerow([line])

def main():
    initial_message = read_initial_message('task_message.md')
    with open('csv_files/data_formatted_terms.csv', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        terms = list(reader)  # Convert CSV input to list of lists

    labelled_data = process_batches(terms, initial_message)
    save_results(labelled_data)
    print("Classification completed and results saved.")

if __name__ == "__main__":
    main()
