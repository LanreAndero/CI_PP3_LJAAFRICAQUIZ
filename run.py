from termcolor import colored
import os
import time
import random

# Define the questions and answers as a list of dictionaries.
quiz_data = [
    {
        "question": "Which river is the longest in Africa?",
        "options": [
            "Congo River", "Nile River", "Niger River", "Zambezi River"
        ],
        "correct_answer": "Nile River",
    },
    {
        "question": "Which African country is known as the 'Rainbow Nation'?",
        "options": [
            "Nigeria", "Kenya", "South Africa", "Egypt"
        ],
        "correct_answer": "South Africa",
    },
    {
        "question": "Which African nation was never colonized by European",
        "question_contd": "powers?",
        "options": ["Ghana", "Ethiopia", "Nigeria", "South Africa"],
        "correct_answer": "Ethiopia",
    },
    {
        "question": "Which African country is famous for its wildlife and",
        "question_contd": "safaris?",
        "options": ["Ghana", "Tanzania", "Ethiopia", "Mali"],
        "correct_answer": "Tanzania",
    },
    {
        "question": "What is the largest lake in Africa?",
        "options": [
            "Lake Chad", "Lake Malawi", "Lake Tanganyika", "Lake Victoria"
        ],
        "correct_answer": "Lake Victoria",
    },
    {
        "question": "Which African country is 'Land of a Thousand Hills'?",
        "options": [
            "Rwanda", "Uganda", "Burundi", "Togo"
        ],
        "correct_answer": "Rwanda",
    },
    {
        "question": "What is the largest river in West Africa?",
        "options": [
            "Congo River", "Niger River", "Zambezi River", "Limpopo River"
        ],
        "correct_answer": "Niger River",
    },
    {
        "question": "Which African country is famous for its pyramids?",
        "options": ["Nigeria", "Kenya", "Egypt", "Morocco"],
        "correct_answer": "Egypt",
    },
    {
        "question": "What is the highest mountain in Africa?",
        "options": [
            "Mount Kenya", "Mount Kilimanjaro", "Mount Elgon",
            "Simien Mountains"],
        "correct_answer": "Mount Kilimanjaro",
    },
    {
        "question": "Which African country is known as the 'Giant of Africa'?",
        "options": [
            "Nigeria", "South Africa", "Ghana", "Kenya"
        ],
        "correct_answer": "Nigeria",
    },
    {
        "question": "Which African country is famous for the Victoria Falls?",
        "options": [
            "Zambia", "Zimbabwe", "Botswana", "Mozambique"
        ],
        "correct_answer": "Zambia",
    },
    {
        "question": "What is the largest city in Africa by population?",
        "options": [
            "Lagos", "Cairo", "Kinshasa", "Johannesburg"
        ],
        "correct_answer": "Lagos",
    },
    {
        "question": "Which African country is known as the 'Pearl of Africa'?",
        "options": [
            "Uganda", "Ethiopia", "Nigeria", "Tunisia"
        ],
        "correct_answer": "Uganda",
    },
    {
        "question": "What is the largest island country in Africa?",
        "options": [
            "Madagascar", "Seychelles", "Comoros", "Mauritius"
        ],
        "correct_answer": "Madagascar",
    },
    {
        "question": "What is the largest country by land area in Africa?",
        "options": [
            "Nigeria", "South Africa", "Algeria", "Sudan"
        ],
        "correct_answer": "Algeria",
    },
    {
        "question": "What is the largest national park in Africa?",
        "options": [
            "Kruger National Park", "Serengeti National Park",
            "Murchison Falls National Park", "Etosha National Park"
        ],
        "correct_answer": "Serengeti National Park",
    },
    {
        "question": "Which African country is famous for its",
        "question_contd": "cocoa production?",
        "options": ["Côte d'Ivoire", "Ghana", "Nigeria", "Cameroon"],
        "correct_answer": "Côte d'Ivoire",
    },
    {
        "question": "Which African country is known as the",
        "question_contd": "'Pearl of the Indian Ocean'?",
        "options": ["Madagascar", "Comoros", "Seychelles", "Mauritius"],
        "correct_answer": "Mauritius",
    },
    {
        "question": "Which African nation, despite its proximity to European",
        "question_contd": "colonies, maintained its sovereignty?",
        "options": ["Kenya", "Uganda", "Somalia", "Morocco"],
        "correct_answer": "Morocco"
    },
    {
        "question": "Which African country successfully resisted colonization",
        "question_contd": "by the French, despite several attempts?",
        "options": ["Madagascar", "Senegal", "Algeria", "Tunisia"],
        "correct_answer": "Algeria",
    },
]

# Define the logo as a string


logo = """
    ___    _      _   ___  __   ___   _    _      _        ___  __
 )    (   /_)    /_)  )_   )_)   )   / `  /_)    / )  / /   )   /
(__  __) / /    / /  (    /    _(_  (_.  / /    (_X  (_/  _(_  /

"""

print(colored("Welcome to the Africa Quiz!\n", "yellow"))

# Function to ask a question and get user input for an answer.


def ask_question(question_data):
    print(question_data["question"])

    # Check if there's a continuation
    if "question_contd" in question_data:
        print(question_data["question_contd"])

    for i, option in enumerate(question_data["options"], start=1):
        colored_option = colored(f"{i}. {option}", "blue")
        print(colored_option)

    while True:
        user_input = input("Enter the number of your answer: \n")

        try:
            user_input = int(user_input)
            if 1 <= user_input <= len(question_data["options"]):
                user_answer = question_data["options"][user_input - 1]
                return user_answer
            else:
                raise ValueError
        except ValueError:
            message = "Invalid input. Please enter a valid option number."
            colored_message = colored(message, "red")
            print(colored_message)

# Function to display the logo


def display_logo():
    print(colored(logo, "cyan"))

# Function to clear the terminal screen.


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" * 100)  # Print 100 empty lines to "clear" the screen

# Function to run the quiz game.


def run_quiz(quiz_data):
    score = 0
    start_time = time.time()

    for question_data in quiz_data:
        user_answer = ask_question(question_data)
        if user_answer is None:
            print(colored("Invalid input. Skipping this question.\n", "red"))
            continue
        if user_answer == question_data["correct_answer"]:
            print(colored("Correct!\n", "green"))
            score += 1
        else:
            correct_answer = question_data['correct_answer']
            message = f"Wrong! The correct answer is: {correct_answer}\n"
            print(colored(message, "red"))

    end_time = time.time()
    time_spent = end_time - start_time
    score_message = f"You scored {score} out of {len(quiz_data)} "
    score_percentage = f"({(score/len(quiz_data)) * 100:.2f}%)."
    final_score = colored(score_message + score_percentage, "yellow")
    time_message = colored(f"Time spent: {time_spent:.2f} seconds", "blue")

    print(final_score)
    print(time_message)

# Add a congratulatory message based on the user's score

    if score == len(quiz_data):
        print(colored("Congratulations! You got a perfect score!", "green"))
    elif score >= len(quiz_data) // 2:
        print(colored("Good job! You did well.", "green"))
    else:
        print(colored("You can do better next time.", "red"))

# Function to play the quiz game again.


def restart_quiz():
    while True:
        clear_screen()  # Clears the terminal screen
        display_logo()
        print("Welcome to the Africa Quiz!\n")
        random.shuffle(quiz_data)  # Shuffle the questions
        run_quiz(quiz_data)  # Start a fresh game

        promt = "\033[91mDo you want to play again? (yes/no): \033[0m\n"
        play_again = input(prompt)
        play_again = play_again.strip().lower()
        if play_again != "yes":
            clear_screen()
            display_logo()
            break


if __name__ == "__main__":
    display_logo()
    prompt = "\033[91mWould you like to start the quiz? (yes/no): \033[0m\n"
    user_input = input(prompt)
    user_input = user_input.strip().lower()
    if user_input == "yes":
        restart_quiz()
    else:
        clear_screen()
        print("\033[91mOkay, maybe next time!\033[0m")
        display_logo()
