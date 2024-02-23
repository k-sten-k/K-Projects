# This is UniBuddy, a personalized chatbot designed to answer common questions 
# for new university students and help them transition into university life.

# Function to display available questions from the list
def display_available_questions():
    """
    Prints a numbered list of questions for the user to choose from.
    """
    print("\nHere are the questions I can answer for you:")
    for question_num, question in enumerate(questions_list, start=1):
        print(f"{question_num}. {question}")

# List of questions for the user to choose from:
questions_list = ["How do I find my way around campus?",
                "Where can I go if I get sick?",
                "Where is the fees office?",
                "Where can I get help if I'm struggling in a class?",
                "What clubs and societies can I join?"]

# List of answers corresponding to the questions in the list
answers_list = ["Use the virtual campus map available on our main website.",
            "Visit the university health centre located on ground floor in themain building.",
            "The fees office is located in main building, first floor, room 28.",
            "Talk to your professor during office hours or to student counsellor.",
            "Attend the student fair with booths for different clubs and organizations, or check our website for list of univerity's societes."]

# Welcoming message and personalized replies based on user input:
print("""\nHello!\nWelcome to university! How exciting! Feeling a bit overwhelmed? Don't worry! I'm here to help :)
        But first let us learn a bit more about each other. My name is UniBuddy""")
name = input("\nWhat's your name? ")
print(f"Hi {name}, nice to meet you!")

faculty = (input("\nWhat faculty do you belong to? ")).strip().lower()
if faculty == "science":
    print(f"The {faculty} faculty?! No way! I love science experiments!")
else : 
    print(f"The {faculty} faculty offers great subjects!")

major = input("\nWhat are your majors? ")
print(f"""So yu will study {major}. Good choice! I hope you enjoy it :) \n\nI have one more question for you:""")

superpower = (input("\nIf you could have a superpower, what would it be? ")).strip().lower()
if superpower == "flight":
    print(f"I would also pick {superpower}! Just imagine soaring through the skies, like Superman or Wonder Woman... ")
else:
    print(f"Ah, {superpower}, sounds like a lot of fun!")

print(f"""\nThank you for all this information {name}. Im confident you can master {major} on your own. 
      Save your {superpower} superpower to fight vilains ;)
      \nNow you can ask me some questions. Please select from the list below.""")

# Display available questions
display_available_questions()

# Continuous conversation loop with error handling
while True:
    try:                                                       
        choosen_question = input("Please select your question number or type 'bye' to exit: ")
        if 1 <= int(choosen_question) <= len(questions_list):
            print(f"\nYou want to know: {questions_list[(int(choosen_question))-1]} \nHere is your answer:") 
            print(answers_list[int(choosen_question)-1], "\n")
        else:
            raise ValueError("Invalid question number.")
    except ValueError:
        print("\nInvalid input. Please enter a valid question number or 'bye' to exit.")
    if choosen_question.lower().strip() == "bye":                           
        print("\nOk, Thank you for chatting with me:) Bye now!!!")
        break
