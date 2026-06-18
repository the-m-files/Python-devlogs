import os
from google import genai

def interactive_essay_helper():
    client = genai.Client()
    
    # Initialize a multi-turn chat session with a system instruction
    chat = client.chats.create(
        model="gemini-2.5-flash",
        config={"system_instruction": "You are an essay drafting assistant. Always format essays with a clear Introduction, Body Paragraphs, and Conclusion."}
    )
    
    print("AI Essay Assistant Initialized. (Type 'quit' to exit)")
    topic = input("What topic do you want to write about? ")
    
    # First turn: Generate the initial essay
    response = chat.send_message(f"Write a templated essay on: {topic}")
    print("\n--- Initial Draft ---\n", response.text, "\n---------------------\n")
    
    # Continuous loop for edits
    while True:
        feedback = input("What changes would you like to make? (or type 'quit'): ")
        if feedback.lower() == 'quit':
            break
            
        response = chat.send_message(feedback)
        print("\n--- Updated Draft ---\n", response.text, "\n---------------------\n")

if __name__ == "__main__":
    interactive_essay_helper()