
"""
계산기
"""
import sys


def userInput(mesg):
    res = input(mesg)
    return res


def calBasic():
    print("enter : [a] [op] [b] >>> ", end="")
    a, op, b = userInput("").split()
    a = int(a)
    b = int(b)

    if op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/":
        print(a/b)
    else:
        print("Wrong input form")


def calBasicPlus():
    print("enter : [a] [op] [b] >>> ", end="")
    a, op, b = userInput("").split()
    a = int(a)
    b = int(b)

    if op == "**":
        print(a**b)
    elif op == "%":
        print(a % b)
    elif op == "//":
        print(a//b)
    else:
        print("Wrong input form")


while True:
    choice = int(userInput("PRACTICE ::  1:basic 2:Plus (0:Exit)#"))
    if choice == 0:
        break
    elif choice == 1:
        calBasic()
    elif choice == 2:
        calBasicPlus()
    else:
        print("Select again :)")
