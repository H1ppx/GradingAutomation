import random

class MCQ():

    def __init__(self, prompt, correctAnswer, *incorrectAnswers):
        self.prompt = prompt
        self.correctAnswer = correctAnswer
        self.answers = incorrectAnswers.append(correctAnswer)
        random.shuffle(self.answers)
