import nltk
import random
import wikipedia
import webbrowser
from nltk.chat.util import Chat, reflections

# Define the patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you?', ['I am doing well, thank you!', 'I am fine, thanks for asking.', 'I\'m good, thanks.']),
    (r'what is your name?', ['You can call me ChatBot.', 'I\'m ChatBot.', 'My name is ChatBot.']),
    (r'quit', ['Bye! Take care.', 'Goodbye, have a great day!', 'See you later.']),
    (r'(^search) (.*)', ['search_wikipedia']),
    (r'(^open) (youtube)', ['open_youtube']),
]

# Function to search Wikipedia
def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return "I found multiple results. Please be more specific."
    except wikipedia.exceptions.PageError as e:
        return "Sorry, I couldn't find any information on that topic."

# Function to open YouTube
def open_youtube():
    webbrowser.open("https://www.youtube.com")

# Create a ChatBot
def chatbot():
    print("Hi! I'm ChatBot. How can I assist you today?")

    # Create a Chat instance
    chat = Chat(patterns, reflections)

    # Start conversation
    while True:
        user_input = input("You: ").lower()
        if user_input == 'quit':
            response = random.choice(patterns[3][1])  # Random response for quitting
            print("ChatBot:", response)
            break
        else:
            response = chat.respond(user_input)
            if response == "search_wikipedia":
                query = user_input.split(' ', 1)[1]  # Extract the query from the user input
                response = search_wikipedia(query)
            elif response == "open_youtube":
                open_youtube()
                response = "Opening YouTube..."
            print("ChatBot:", response)

# Main function
if __name__ == "__main__":
    nltk.download('punkt')  # Ensure punkt tokenizer is downloaded
    wikipedia.set_lang("en")  # Set Wikipedia language to English
    chatbot()
