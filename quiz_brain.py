import html


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.answer = self.question_list[self.question_number]

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.answer = self.question_list[self.question_number]
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {html.unescape(current_question.text)} (True/False): "

    def check_answer(self, user_answer):
        correct_answer = self.answer.answer
        if user_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False
