class Quiz:
    def __init__(self, questions):
        self.q_number = 0
        self.q_list = questions
        self.score = 0

    # TODO: Asking Questions
    def next_question(self):
        question = self.q_list[self.q_number]
        self.q_number += 1
        answer = input(f"Q.{self.q_number}: {question.text} (True/False)?: ")
        self.check_response(answer, question.answer)
     
    # TODO: Checking if the anser was correct
    def check_response(self, response, answer):
        if answer.lower() == response.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You go it wrong!")

        print(f"The answer was: {answer}")
        print(f"Your current score is {self.score}/{self.q_number}")

    # TODO: Checking to see if we are at the end.
    def still_has_questions(self):
        number = len(self.q_list)
        return self.q_number < number
            