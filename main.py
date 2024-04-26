import pandas as pd
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader
from transformers import DistilBertTokenizer

from src.dataset import ContractDataset
from src.models import get_model
from src.train import train_model

def tokenize_data(texts, tokenizer):
    return tokenizer(
        text=texts,
        add_special_tokens=True,
        max_length=64,
        truncation=True,
        padding='max_length',
        return_tensors='pt',
        return_attention_mask=True
    )

def main():
    # Load data
    df = pd.read_csv('csv_files/combined_training_data.csv', header=None)
    df.columns = ['label', 'text']

    # Split the dataset
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

    # Initialize the tokenizer
    tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')

    # Tokenize the data
    train_encodings = tokenize_data(train_df['text'].tolist(), tokenizer)
    test_encodings = tokenize_data(test_df['text'].tolist(), tokenizer)

    # Create datasets
    train_dataset = ContractDataset(train_encodings, train_df['label'].tolist())
    test_dataset = ContractDataset(test_encodings, test_df['label'].tolist())

    # Create data loaders
    train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=16, shuffle=False)

    # Load model
    model = get_model()

    # Train the model
    train_model(model, train_loader, test_loader)

if __name__ == '__main__':
    main()
