import os
import nltk
import ssl
import streamlit as st
from models.train_model import train_model
from models.predict import chatbot_response

# SSL and NLTK setup
ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

# Initialize the model (this will be cached by Streamlit)
@st.cache_resource
def load_model():
    return train_model()

def main():
    st.title("End to End Chatbot")
    st.write("Welcome to the chatbot. Please type a message and press Enter to start the conversation...")

    # Initialize chat history in session state if it doesn't exist
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Load the model and intents
    vectorizer, clf, intents = load_model()
    
    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Get user input
    user_input = st.chat_input("Type your message here...")
    
    if user_input:
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Get chatbot response
        response = chatbot_response(user_input, vectorizer, clf, intents)
        
        # Add chatbot response to chat history
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        
        # Rerun to display the new messages
        st.rerun()

        # Check if it's a goodbye message
        if response.lower() in ['goodbye', 'bye']:
            st.success("Thank you for chatting with me. Have a great day!")
            st.stop()

if __name__ == '__main__':
    main()