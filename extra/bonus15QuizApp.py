import json

with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, item in enumerate(question["options"]):
        row = f"{index + 1}. {item}"
        print(row)
    answer = int(input("Your response here (enter a number): "))
    question["user_selection"] = answer


print("The results are in!")
score = 0
for index, question in enumerate(data):
    if question["user_selection"] == question["correct_answer"]:
        score = score + 1
        result = "CORRECT"
    else:
        result = "WRONG"
    message = f"Question {index + 1} {result} : you responded {question['user_selection']}, " \
              f"correct answer is {question['correct_answer']}"
    print(message)

print(score, "/", len(data))
