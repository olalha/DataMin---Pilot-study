from torch.utils.data import DataLoader
import torch
from transformers import AdamW
    
def save_model(model, save_path):
    torch.save(model.state_dict(), save_path)

def train_model(model, train_loader, test_loader, epochs=3):
    optimizer = AdamW(model.parameters(), lr=5e-5)
    for epoch in range(epochs):
        model.train()
        for batch in train_loader:
            outputs = model(**batch)
            loss = outputs.loss
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()
        print(f"Epoch: {epoch}, Loss: {loss.item()}")
    
    print("Training complete!")

    # Evaluate the model
    model.eval()
    total_correct = 0
    with torch.no_grad():
        for batch in test_loader:
            outputs = model(**batch)
            predictions = outputs.logits.argmax(dim=1)
            total_correct += (predictions == batch['labels']).sum().item()

    accuracy = total_correct / len(test_loader.dataset)
    print(f'Accuracy: {accuracy:.4f}')

    model_save_path = 'models/trained_model.pth'
    save_model(model, model_save_path)

