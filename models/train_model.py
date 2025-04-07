import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import os

def load_intents(filepath=None):
    # If no filepath is provided, look in the data directory relative to this file
    if filepath is None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(current_dir, '..', 'data', 'intents.json')
    
    with open(filepath, 'r', encoding='utf-8') as file:
        intents = json.load(file)
    return intents

def train_model():
    intents = load_intents()
    
    # Create the vectorizer and classifier
    vectorizer = TfidfVectorizer()
    clf = LogisticRegression(random_state=0, max_iter=10000)

    # Preprocess the data
    tags = []
    patterns = []
    for intent in intents:
        for pattern in intent['patterns']:
            tags.append(intent['tag'])
            patterns.append(pattern)

    # Train the model
    x = vectorizer.fit_transform(patterns)
    y = tags
    clf.fit(x, y)
    
    return vectorizer, clf, intents

if __name__ == '__main__':
    vectorizer, clf, intents = train_model()
    print("Model trained successfully!")