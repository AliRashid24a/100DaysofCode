from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []
for question in question_data:
    temp_question = Question(question['text'],question['answer'])
    question_bank.append(temp_question)

quiz = Quiz(question_bank)

while quiz.check_end() == False:
    quiz.next_question()

print(f"You've completed the quiz.\nYour final score is {quiz.score}/{quiz.question_number}")