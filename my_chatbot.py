import nltk
import random
from nltk.stem import WordNetLemmatizer
import string

# --- NLTK Data Downloads ---
# These 'try-except' blocks will attempt to download the necessary NLTK data
# if it's not already present on your system.
# The 'LookupError' is caught when nltk.data.find() cannot locate the resource.

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    print("Downloading 'wordnet' NLTK data. This may take a moment...")
    nltk.download('wordnet')
    print("'wordnet' download complete.")

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    print("Downloading 'punkt' NLTK data. This may take a moment...")
    nltk.download('punkt')
    print("'punkt' download complete.")

# Initialize the WordNet Lemmatizer
lemmatizer = WordNetLemmatizer()

# --- Define Chatbot's Knowledge Base ---
# This is a simple rule-based system. For a real NLP chatbot, you'd use
# machine learning models and much larger datasets.

greetings = ["hello", "hi", "hey", "greetings", "whats up", "howdy"]
greeting_responses = ["Hello!", "Hi there!", "Hey!", "Greetings!", "How can I help you today?", "Nice to see you!"]

goodbyes = ["bye", "goodbye", "see you", "farewell", "cya", "later"]
goodbye_responses = ["Goodbye!", "See you later!", "Have a great day!", "Farewell!", "Take care!"]

thanks = ["thank you", "thanks", "appreciate it", "cheers"]
thank_responses = ["You're welcome!", "No problem!", "Glad to help!", "Anytime!"]

# More specific Q&A
knowledge_base = {
    "what is your name": "I am a simple chatbot.",
    "who created you": "I was created by Goli Sathwik, the Programmer.",
    "how are you": "I'm just a program, so I don't have feelings, but I'm functioning perfectly and ready to assist you!",
    "what can you do": "I can answer some basic questions, have a simple conversation, and provide information stored in my knowledge base.",
    "where are you from": "I exist in the digital realm, so I don't have a physical origin.",
    "what is nlp": "NLP stands for Natural Language Processing. It's a branch of AI that focuses on enabling computers to understand, interpret, and generate human language.",
    "what is python": "Python is a popular high-level, general-purpose programming language, widely used for web development, data analysis, AI, and more.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "what is ai": "AI, or Artificial Intelligence, refers to the simulation of human intelligence in machines that are programmed to think and learn like humans.",
    "what is machine learning": "Machine Learning is a subset of AI that allows systems to learn from data, identify patterns, and make decisions with minimal human intervention.",
}

# Fallback responses for when the chatbot doesn't understand
fallback_responses = [
    "I'm not sure I understand that. Could you rephrase?",
    "That's an interesting question, but I don't have an answer for it yet.",
    "My apologies, I'm still learning. Could you try asking something else?",
    "I'm afraid I don't comprehend. Can you provide more context?",
    "Hmm, I don't seem to have information on that."
]

# --- Helper Functions for Text Processing ---
def preprocess_text(text):
    """Converts text to lowercase and removes punctuation."""
    text = text.lower()
    text = "".join([char for char in text if char not in string.punctuation])
    return text

def lemmatize_words(words):
    """Lemmatizes a list of words."""
    return [lemmatizer.lemmatize(word) for word in words]

def get_response(user_input):
    """
    Determines the chatbot's response based on user input.
    This uses a simplified approach of matching keywords and patterns.
    """
    processed_input = preprocess_text(user_input)
    # Use nltk.word_tokenize for more accurate word separation
    words = nltk.word_tokenize(processed_input)
    lemmas = lemmatize_words(words)

    # Check for greetings
    for word in lemmas:
        if word in greetings:
            return random.choice(greeting_responses)

    # Check for goodbyes
    for word in lemmas:
        if word in goodbyes:
            return random.choice(goodbye_responses)

    # Check for thanks
    for word in lemmas:
        if word in thanks:
            return random.choice(thank_responses)

    # Check knowledge base for direct or strong matches
    # This loop checks if a significant portion of the "question" words
    # are present in the user's input.
    for question, answer in knowledge_base.items():
        q_processed = preprocess_text(question)
        q_words = set(lemmatize_words(nltk.word_tokenize(q_processed)))
        
        # Calculate overlap percentage
        if q_words: # Avoid division by zero if question is empty
            overlap = len(q_words.intersection(set(lemmas))) / len(q_words)
            # You can adjust this threshold (e.g., 0.7 for 70% overlap)
            if overlap > 0.7:
                return answer
        
        # Also check for exact substring match of the processed question
        if q_processed in processed_input:
            return answer

    # If no specific match, provide a fallback response
    return random.choice(fallback_responses)

# --- Main Chatbot Loop ---
if __name__ == "__main__":
    print("--- Simple Chatbot ---")
    print("Hello! I'm a basic chatbot ready to chat.")
    print("Type 'quit', 'bye', or 'exit' to end our conversation.")
    print("----------------------")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "bye", "exit"]:
            print("Chatbot: Goodbye! It was nice chatting with you.")
            break
        else:
            response = get_response(user_input)
            print(f"Chatbot: {response}")