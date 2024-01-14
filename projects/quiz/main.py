from question_model import  Question
from data import  question_data
from quiz_brain import QuizBrain


question_bank = []
for questions in question_data:
    question_text = questions["question"]
    question_answer = questions["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
print(f"You've completed the quizz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")