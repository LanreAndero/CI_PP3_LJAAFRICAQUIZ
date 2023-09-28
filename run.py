from termcolor import colored
import time
import os
import random

# Define the questions and answers as a list of dictionaries.
quiz_data = [
    {
        "question": "Which river is the longest in Africa?",
        "options": ["Congo River", "Nile River", "Niger River", "Zambezi"],
        "correct_answer": "Nile River",
    },
    {
        "question": "Which African country is known as the 'Rainbow Nation'?",
        "options": ["Nigeria", "Kenya", "South Africa", "Egypt"],
        "correct_answer": "South Africa",
    },
    {
        "question": "Which African nation was never colonized by European?",
        "options": ["Ghana", "Ethiopia", "Nigeria", "South Africa"],
        "correct_answer": "Ethiopia",
    },
    {
        "question": "Which African country is famous for its safaris?",
        "options": ["Ghana", "Tanzania", "Ethiopia", "Mali"],
        "correct_answer": "Tanzania",
    },
    {
        "question": "What is the largest lake in Africa?",
        "options": ["Lake Chad", "Lake Malawi", "Tanganyika", "Lake Victoria"],
        "correct_answer": "Lake Victoria",
    },
    {
        "question": "Which African country is 'Land of a Thousand Hills'?",
        "options": ["Rwanda", "Uganda", "Burundi", "Togo"],
        "correct_answer": "Rwanda",
    },
    {
        "question": "What is the largest river in West Africa?",
        "options": ["Congo River", "Niger River", "Zambezi River", "Limpopo"],
        "correct_answer": "Niger River",
    },
    {
        "question": "Which African country is famous for its pyramids?",
        "options": ["Nigeria", "Kenya", "Egypt", "Morocco"],
        "correct_answer": "Egypt",
    },
    {
        "question": "What is the highest mountain in Africa?",
        "options": ["Mount Kenya", "Mount Kilimanjaro", "Elgon", "Simien"],
        "correct_answer": "Mount Kilimanjaro",
    },
    {
        "question": "Which African country is known as the 'Giant of Africa'?",
        "options": ["Nigeria", "South Africa", "Ghana", "Kenya"],
        "correct_answer": "Nigeria",
    },
    {
        "question": "Which African country is famous for the Victoria Falls?",
        "options": ["Zambia", "Zimbabwe", "Botswana", "Mozambique"],
        "correct_answer": "Zambia",
    },
    {
        "question": "What is the largest city in Africa by population?",
        "options": ["Lagos", "Cairo", "Kinshasa", "Johannesburg"],
        "correct_answer": "Lagos",
    },
    {
        "question": "Which African country is known as the 'Pearl of Africa'?",
        "options": ["Uganda", "Ethiopia", "Nigeria", "Tunisia"],
        "correct_answer": "Uganda",
    },
    {
        "question": "What is the largest island country in Africa?",
        "options": ["Madagascar", "Seychelles", "Comoros", "Mauritius"],
        "correct_answer": "Madagascar",
    },
    {
        "question": "What is the largest country by land area in Africa?",
        "options": ["Nigeria", "South Africa", "Algeria", "Sudan"],
        "correct_answer": "Algeria",
    },
]

# Function to present the question and get user input for an answer.


def ask_question(question_data):
    print(question_data["question"])
    for i, option in enumerate(question_data["options"], start=1):
        colored_option = colored(f"{i}. {option}", "blue")
        print(colored_option)
    user_input = input("Enter the number of your answer: ")
    try:
        user_answer = question_data["options"][int(user_input) - 1]
        return user_answer
    except (ValueError, IndexError):
        return None


# Function to clear the terminal screen.


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


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

# Function to play the quiz game again.


def play_quiz_again():
    clear_screen()
    print("Welcome to the Africa Quiz!\n")
    while True:
        random.shuffle(quiz_data)  # Shuffle the questions for a new game
        run_quiz(quiz_data)  # Start a fresh game
        play_again = input("Do you want to play the quiz again? (yes/no): ")
        if play_again.lower() != "yes":
            break


# Function to shuffle the quiz questions and reset the score.


def restart_quiz():
    clear_screen()
    print("Welcome to the Africa Quiz!\n")
    random.shuffle(quiz_data)  # Shuffle the questions
    run_quiz(quiz_data)  # Start a fresh game

# Run the quiz game.


restart_quiz()
play_quiz_again()
