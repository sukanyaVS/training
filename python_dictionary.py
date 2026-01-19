quiz_questions = {
    1: {
        "q": "Which keyword is used to define a function in Python?",
        "opt": {
            "A": "func",
            "B": "define",
            "C": "def",
            "D": "function"
        },
        "ans": "C"
    },
    2: {
        "q": "What is the output of 2 * 3?",
        "opt": {
            "A": "5",
            "B": "6",
            "C": "8",
            "D": "9"
        },
        "ans": "B"
    },
    3: {
        "q": "What is 5 + 3?",
          "opt": {
            "A": "5",
            "B": "6",
            "C": "8",
            "D": "9"
        },
        "ans": "C"
    }
}

def start_quiz(questions):
 score = 0
 for data in questions.values():
    print("Question:",data["q"])
    for options in data['opt']:
       print(options)
    user_data = input("Enter option A/B/C/D or S to skip the question or Q to quit the quiz : ")
    user_input = user_data.upper()
    print(user_input)

    if user_input == 'Q':
      print('You quit the quiz')
      break
    if user_input == 'S':
      print('This question is skipped')
      continue
    if user_input == data['ans']:
      print("Correct answer")
      score += 1
    else:
      print("Wrong answer")
      score -= 1

 print("Your score is :",score)    




start_quiz(quiz_questions)
 