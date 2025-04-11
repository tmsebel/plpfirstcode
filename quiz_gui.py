import random

def ask_question(question, options, correct_option):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    try:
        answer = int(input("Choose the correct option (1/2/3/4): "))
        if answer < 1 or answer > 4:
            raise ValueError
        if answer == correct_option:
            return True
        else:
            print(f"Wrong! The correct answer is: {options[correct_option - 1]}\n")
            return False
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 4.")
        return False

def quiz():
    questions = [
        # Your full question list here
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
            "correct_option": 3
        },
        # Add the rest
    ]
    random.shuffle(questions)
    score = 0
    for q in questions:
        if ask_question(q["question"], q["options"], q["correct_option"]):
            score += 1
            print("Correct!\n")
    print(f"Your final score is {score} out of {len(questions)}")

def main():
    while True:
        quiz()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()