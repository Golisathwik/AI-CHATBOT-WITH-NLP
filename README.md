# AI-CHATBOT-WITH-NLP

COMPANY: CODTECH IT SOLUTIONS

NAME: GOLI SATHWIK

INTERN ID: CT04DM1450

DOMAIN: PYTHON PROGRAMMING

DURATION: 4 WEEEKS

MENTOR: NEELA SANTOSH

---

## Project Description: AI Chatbot with Natural Language Processing

### Project Title
**AI Chatbot with Natural Language Processing (NLP)**

### Overview
This project involves building a **simple AI chatbot** capable of engaging in basic conversational interactions and answering user queries. The core functionality is powered by **Natural Language Processing (NLP)** libraries, specifically **NLTK (Natural Language Toolkit)** in Python, to enable the chatbot to understand and respond to human language.

### Key Features and Functionality

1.  **Conversational Interface:** The chatbot provides a command-line interface where users can type in their questions or statements, and the chatbot will respond accordingly.
2.  **Basic Understanding of User Input:**
    * **Greeting/Farewell Recognition:** The chatbot can identify common greetings (like "hello," "hi") and farewells ("bye," "goodbye") and respond appropriately.
    * **Keyword and Pattern Matching:** It uses pre-defined patterns and keywords to recognize specific questions or topics.
    * **Thanks Recognition:** It acknowledges expressions of gratitude.
3.  **Knowledge Base:** The chatbot comes with a built-in "knowledge base" (a dictionary of pre-programmed questions and answers) that allows it to provide direct responses to common inquiries, such as:
    * "What is your name?"
    * "Who created you?"
    * "What is NLP?"
    * "Tell me a joke."
4.  **Natural Language Processing (NLP) with NLTK:**
    * **Text Preprocessing:** User input is cleaned by converting it to lowercase and removing punctuation, ensuring consistent matching.
    * **Tokenization:** NLTK's `punkt` tokenizer is used to break down sentences into individual words (tokens), which is a fundamental step for analysis.
    * **Lemmatization:** The `WordNetLemmatizer` is employed to reduce words to their base or root form (e.g., "running" becomes "run," "better" becomes "good"). This helps the chatbot recognize words regardless of their grammatical variations, improving accuracy in matching queries.
5.  **Fallback Responses:** When the chatbot doesn't understand a query (i.e., it doesn't find a matching pattern in its knowledge base), it provides a polite fallback response, indicating that it's still learning or needs more clarification.
6.  **Extensibility:** The modular design allows for easy expansion of the chatbot's knowledge base by adding more question-and-answer pairs or developing more sophisticated response logic.

### Technical Stack

* **Programming Language:** Python
* **Primary NLP Library:** NLTK (Natural Language Toolkit)
    * `nltk.word_tokenize` (for tokenization)
    * `nltk.stem.WordNetLemmatizer` (for lemmatization)
    * NLTK data packages (`wordnet`, `punkt`)

### How It Works (Simplified Flow)

1.  **User Input:** The user types a message.
2.  **Preprocessing:** The message is converted to lowercase and punctuation is removed.
3.  **Tokenization:** The cleaned message is broken down into individual words.
4.  **Lemmatization:** Each word is reduced to its base form.
5.  **Pattern Matching:** The chatbot checks the lemmatized words/phrases against its pre-defined rules for:
    * Greetings
    * Goodbyes
    * Expressions of thanks
    * Specific questions in its `knowledge_base` (using a percentage overlap or exact phrase match logic).
6.  **Response Generation:** Based on the match, the chatbot provides a relevant pre-written response. If no match is found, a general fallback response is given.
7.  **Loop:** The process repeats, allowing for continuous conversation until the user decides to exit.

### Future Enhancements (Potential Next Steps)
While this project provides a solid foundation, future enhancements could include:

* **Advanced NLP Models:** Incorporating machine learning models (e.g., using scikit-learn, TensorFlow, or PyTorch) for more sophisticated intent recognition and entity extraction.
* **Context Management:** Implementing a system to remember previous turns in the conversation to allow for more natural, multi-turn dialogues.
* **Integration with APIs:** Connecting to external APIs to retrieve real-time information (e.g., weather, news, specific product data).
* **Sentiment Analysis:** Giving the chatbot the ability to detect the user's emotional tone.
* **Voice Interface:** Adding speech-to-text and text-to-speech capabilities for a voice-enabled chatbot experience.

---

