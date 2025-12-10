import re
import random
responses = {
    "hello": [
        "Hello! How could I help you today?",
        "Hi there! What's on your mind?",
        "Greetings! What can I do for you?"
    ],
    "hi": [
        "Hello! How could I help you today?",
        "Hi there! What's on your mind?",
        "Greetings! What can I do for you?"
    ],
    "I feel (.*)": [
        "Why do you feel {}?",
        "How long have you been feeling {}?",
        "Feeling {} is completely normal. Can you tell me more about it?"
    ],
    "I am (.*)": [
        "It's interesting that you are {}. What does that mean to you?",
        "Tell me more about being {}.",
        "Why do you say you are {}?"
    ],
    "I want (.*)": [
        "Why do you want {}?",
        "What would achieving {} look like?",
        "If you could have {} right now, what would you do next?"
    ],
    "(.*) your name(.*)": [
        "I am a helpful AI assistant.",
        "I don't have a name, but I can help you with your questions."
    ],
    "How are you": [
        "I am functioning well, thank you for asking!",
        "As an AI, I don't have feelings, but I'm ready to assist you."
    ],
    "quit": [
        "Goodbye! It was nice chatting with you.",
        "Talk to you later!",
        "Feel free to come back anytime."
    ],
    "(.*)": [ # This is the fallback response for any unrecognized input
        "That's interesting. Can you elaborate?",
        "I'm not sure I understand. Can you rephrase that?",
        "Tell me more about that."
    ]
}

def process_text(input_text) :
    for pattern in responses:
        matches = re.match(pattern,input_text,re.IGNORECASE);
        # if Matches are found i want to print the a random corresponsing response;
        # I also want to replace the regex text in the response with the corresponsing word mentioned.
        if matches:
            chosen_response = random.choice(responses[pattern]);
            if matches.groups():
                return chosen_response.format(matches.group(1));



#Print the  Hi FROM AI;
print("Hello my name is CHEESE");

userinput = '';
while(True):
    userinput = input("YOU: ");
    if re.match("(bye|quit)",userinput,re.IGNORECASE):
        print("CHEESE: GOOD BYE!")
        break;
    else:
        print(f"CHEESE: {process_text(userinput)}");



