from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
still_has_questions = True

while still_has_questions:
    quiz.next_question()
    still_has_questions = quiz.still_has_questions()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}.")
