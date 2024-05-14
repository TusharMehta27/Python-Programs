import random

# List of questions and answers
quiz_questions = {
    "What is the capital of France?": "Paris",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "Which planet is known as the Red Planet?": "Mars",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
    "What is the chemical symbol for water?": "H2O"
}

# Function to display a random quiz
def display_quiz(questions):
    print("Welcome to the GK Quiz!")
    print("Answer the following questions:")

    # Shuffle the questions to display them randomly
    shuffled_questions = list(questions.keys())
    random.shuffle(shuffled_questions)

    for question in shuffled_questions:
        print(question)
        answer = input("Your answer: ")
        check_answer(question, answer)

# Function to check the answer
def check_answer(question, answer):
    correct_answer = quiz_questions[question]
    if answer.lower() == correct_answer.lower():
        print("Correct!")
        return 1
    else:
        print("Incorrect. The correct answer is:", correct_answer)
        return 0

# Function to calculate the score
def score():
    score = 0
    for question in quiz_questions:
        answer = input(f"{question}\nYour answer: ")
        if check_answer(question, answer):
            score += 1
    return score

# Function to provide remarks based on the score
def remark(score_value):
    if score_value == 5:
        return "Outstanding"
    elif score_value == 4:
        return "Excellent"
    elif score_value == 3:
        return "Good"
    elif score_value == 2:
        return "Read more to score more"
    elif score_value == 1:
        return "Needs to take interest"
    else:
        return "General knowledge will always help you. Take it seriously."

# Main code
display_quiz(quiz_questions)
final_score = score()
print("Your final score is:", final_score)
print("Remarks:", remark(final_score))
