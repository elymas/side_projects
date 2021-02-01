#-*- coding:utf-8 -*-

'''
육하원칙에 해당하는 의문사로 시작하는 문장을 의문문 형식으로 바꾸어주는 코드
'''

def question_finder(sentence):
    parameters = ("언제", "어디서", "누가", "무엇을", "어떻게", "왜")
    if sentence.startswith(parameters):
        return f"{sentence}?"
    else:
        return f"{sentence}."


data = []

while True:
    yourdata = input("문장을 입력해 주세요 : ")
    if yourdata == "그만":
        break
    else:
        data.append(question_finder(yourdata))

print(" ".join(data))
