#Jonathan M Lucius
#The purpose of this code is to act as a the class module for the Trivia game.

class trivia:
    def __init__(self):
        self.__question = ''
        self.__ans1 = ''
        self.__ans2 = ''
        self.__ans3 = ''
        self.__ans4 = ''
        self.__real_ans = 0
    
    def set_qna(self, new_question, new_ans1, new_ans2, new_ans3, new_ans4, right_ans):
        self.__question = new_question
        self.__ans1 = new_ans1
        self.__ans2 = new_ans2
        self.__ans3 = new_ans3
        self.__ans4 = new_ans4
        self.__real_ans = right_ans

    def get_ans(self):
        return self.__real_ans
    
    def __str__(self):
        return f'Question: {self.__question} \nAnswer 1: {self.__ans1} \nAnswer 2: {self.__ans2} \
        \nAnswer 3: {self.__ans3} \nAnswer 4: {self.__ans4}'
    