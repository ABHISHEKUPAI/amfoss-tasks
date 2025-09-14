import requests
import html
import random
import threading
import time

def get_questions(amount, difficulty, q_type):
    url = "https://opentdb.com/api.php"
    params = {
        "amount": amount,
        "difficulty": difficulty,
        "type": q_type
    }

    response = requests.get(url, params=params)
    data = response.json()
    return data["results"]
def ask_question(question_data, time_limit=15):
    correct_answer = html.unescape(question_data["correct_answer"])
    if question_data["type"] == "multiple":
        options = [html.unescape(ans) for ans in question_data["incorrect_answers"]]
        options.append(correct_answer)
        random.shuffle(options)
    else:
        options = ["True", "False"]
    print("\n" + html.unescape(question_data["question"]))
    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")
    user_answer = [None]

    def get_input():
        user_answer[0] = input("\nYour choice: ")
    thread = threading.Thread(target=get_input)

    thread.daemon = True
    thread.start()
    start_time = time.time()
    
    while time.time() - start_time < time_limit:
        if user_answer[0] is not None:
            print()
            break
        remaining = int(time_limit - (time.time() - start_time))
        print("\r" + " " * 50, end="\r")  # clear 50 chars
        print(f"  Time left: {remaining:2d}s", end="\r", flush=True)
        time.sleep(1)
    if user_answer[0] is None:
        print("\nTime's up! :( Answer:", correct_answer)
        return 0
    try:
        chosen_option = options[int(user_answer[0]) - 1]
    except:
        chosen_option = None

    if chosen_option and chosen_option.lower() == correct_answer.lower():
        print("Correct :) ")
        return 1
    else:
        print("Wrong :( Answer:", correct_answer)
        return 0
def main():
    print("Welcome to TimeTickQuiz!")

    num_questions = int(input("Number of questions: "))
    difficulty = input("Difficulty (easy/medium/hard): ").lower()
    q_type = input("Type (multiple/boolean): ").lower()
      
    score = 0
    questions = get_questions(num_questions, difficulty, q_type)

    for q in questions:
        score += ask_question(q)

    print(f"\nGame Over! Score: {score}/{num_questions}")

if __name__ == "__main__":
    main()
