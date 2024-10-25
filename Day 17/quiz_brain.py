from question_model import Question
class Quiz:
    def __init__(self,questions):
        self.score = 0
        self.question_number = 0
        self.questions_list = questions
    
    def check_if_correct(self, question: Question, answer: str):
        if answer.lower() == question.answer.lower():
            return True
        return False
    
    def check_end(self):
        return self.question_number > len(self.questions_list)-1
    
    def next_question(self):
        # if question number is at the end of the list stop
        user_choice = str(input(f"Q.{self.question_number+1}: {self.questions_list[self.question_number].text} (True/False?)"))
        if self.check_if_correct(self.questions_list[self.question_number],user_choice):
            self.score += 1
            print(f"You got it right!")
        else:
            print("That was the wrong answer!")
        print(f"Your score is {self.score}/{(self.question_number+1)}")
        self.question_number += 1
        return True

 

    

