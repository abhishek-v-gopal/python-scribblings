# build by Open AI
def ask_question(question, correct_answer, max_attempts=3):
    attempts = 0
    while attempts < max_attempts:
        user_answer = input(question + " ").strip().lower()
        if user_answer == correct_answer:
            print("Correct!\n")
            return True
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            if remaining_attempts > 0:
                print(f"Incorrect. You have {remaining_attempts} {'attempts' if remaining_attempts > 1 else 'attempt'} remaining.")
            else:
                print("Sorry, you've run out of attempts. Moving to the next question.\n")
                return False

def main():
    print("Welcome to the Quiz!\n")

    # Question 1
    question_1 = "What is the capital of France?"
    answer_1 = "paris"
    if not ask_question(question_1, answer_1):
        return

    # Question 2
    question_2 = "What is the largest mammal in the world?"
    answer_2 = "blue whale"
    if not ask_question(question_2, answer_2):
        return

    # Question 3
    question_3 = "Which planet is known as the Red Planet?"
    answer_3 = "mars"
    if not ask_question(question_3, answer_3):
        return

    print("Congratulations! You've completed the quiz.")
    
if __name__ == "__main__":
    main()
