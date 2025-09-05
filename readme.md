# 🤖 End-to-End Chatbot Project

This project implements a simple yet powerful chatbot using Python, Streamlit, and machine learning techniques. The chatbot understands natural language inputs and provides appropriate responses based on predefined intents.

# Table of Contents
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Customizing the Chatbot](#customizing-the-chatbot)
- [Future Improvements](#future-improvements)

# Project Structure

```
End-2-End_chatbot/
│
├── data/
│   └── intents.json        # Contains all conversation patterns and responses
│
├── models/
│   ├── train_model.py      # Handles model training
│   └── predict.py         # Handles response prediction
│
├── utils/
│   └── nltk_data/         # NLTK data files
│
├── app.py                 # Main Streamlit application
└── README.md              # This documentation file
```

# How It Works

# Step 1: Intent Definition
- All possible conversation patterns and responses are defined in `intents.json`
- Each intent has:
  - A `tag` (category name)
  - Multiple `patterns` (example user inputs)
  - Multiple `responses` (possible bot replies)

# Step 2: Model Training
1. The training script (`train_model.py`):
   - Loads the intents from JSON
   - Creates a TF-IDF vectorizer to convert text to numerical features
   - Uses Logistic Regression to learn patterns
   - Saves the trained model components

# Step 3: Prediction
1. When a user sends a message:
   - The input is transformed using the same TF-IDF vectorizer
   - The model predicts the most likely intent tag
   - A random response from that intent's responses is selected

# Step 4: Streamlit Interface
- Provides a clean chat interface
- Maintains conversation history
- Handles user input and displays bot responses

# Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/7skaliahmed07/End-2-End_chatbot.git
   cd End-2-End_chatbot
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually if you don't have a requirements file:
   ```bash
   pip install streamlit nltk scikit-learn
   ```

4. Download NLTK data:
   ```bash
   python -m nltk.downloader punkt
   ```

# Running the Project

1. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Interact with the chatbot:
   - The app will open in your default browser
   - Type messages in the input box and press Enter
   - The chatbot will respond based on the trained intents

3. To exit:
   - Type "goodbye" or close the browser window
   - Press Ctrl+C in the terminal to stop the server

# Customizing the Chatbot

1. Add new intents:
   - Edit `data/intents.json`
   - Add new objects following the same format:
     ```json
     {
       "tag": "new_category",
       "patterns": ["sample question 1", "sample question 2"],
       "responses": ["answer 1", "answer 2"]
     }
     ```

2. Improve responses:
   - Add more patterns for each intent to improve recognition
   - Add more varied responses to make conversations more natural

3. Retrain the model:
   - The model automatically retrains when you modify intents.json
   - No manual retraining needed (thanks to Streamlit caching)

# Future Improvements

1. Add more advanced NLP:
   - Implement entity recognition
   - Add sentiment analysis

2. Enhance the interface:
   - Add typing indicators
   - Include multimedia responses

3. Add persistence:
   - Save conversation history
   - Implement user authentication

4. Deploy the chatbot:
   - Host on Streamlit Sharing
   - Create a Docker container for easy deployment

