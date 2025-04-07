import random

def chatbot_response(input_text, vectorizer, clf, intents):
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    
    for intent in intents:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    
    return "I'm sorry, I don't understand that. Can you please rephrase?"