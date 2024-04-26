from transformers import DistilBertForSequenceClassification

def get_model(num_labels=2):
    model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=num_labels)
    return model
