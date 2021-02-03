#-*- -coding:utf-8 -*-

SECURE = {'A':'4', 'a':'@', 'b':'6', 'B':'8', 's':'&', 'k':'|<', 'O':'0', 'D':'|)', 'h':'7'}

def passwordsecure(input):

    for key, value in SECURE.items():
        input = input.replace(key, value)

    return input

password = input("비밀번호는 알파벳 대소문자+숫자만 가능합니다. \n당신의 비밀번호를 입력해주세요: ")

print(f"당신의 새로운 비밀번호는 {passwordsecure(password)}")
