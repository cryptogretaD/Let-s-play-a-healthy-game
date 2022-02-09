question_prompts = [
     "I’m red, round and salads is where I can be found?\n(a) Tomato\n(b) Apple\n(c) Strawberry\n",
     "I'm popular fruit, usually red or green and you can eat or drink my juice?\n(a) Apple\n(b) Cherry\n(c) Banana\n",
     "I am a common type of red fruit, small but not a cherry?\n(a) Pomegranate \n(b) Apple\n(c) Strawberry\n",
     "I come out of the earth who cuts off my tail, takes off my suit of silk, and weeps beside me when I am dead?" +
     "\n(a) Carrot\n(b) Onion\n(c) Potato\n"
]


class Question:
     def __init__(self, content, answer):
          self.content = content
          self.answer = answer


questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "a"),
     Question(question_prompts[2], "c"),
     Question(question_prompts[3], "c"),
]


class MiniGame1:
    def __init__(self, list_question=[]):
        self.list_question = list_question

    def add_question(self):
        self.list_question += questions


def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))


run_quiz(questions)