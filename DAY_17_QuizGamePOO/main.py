from question_model import Question
from data import question_data
from quiz_brain import  QuizBrain

question_bank = []
for question in question_data:
    temp_question = Question(question["question"], question["correct_answer"])
    question_bank.append(temp_question)

quiz = QuizBrain(question_bank)
# quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is {quiz.score}/{len(quiz.question_list)}")
