from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


class SentimentAnalysis:

    def __init__(self, MODEL_NAME):
        self.model_name = MODEL_NAME
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)

    def sentiment_score(self, text):
        tokens = self.tokenizer.encode(text, return_tensors='pt')
        result = self.model(tokens)
        return int(torch.argmax(result.logits))+1
