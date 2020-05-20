# pracitce


# 입력 > 연산자, a ,b
# 출력 > 계산 결과

def useInput():
    y = input()
    return y


def cal():
    # 1. 입력처리
    op = useInput()
    a = int(useInput())
    b = int(useInput())
    y = None
    # 2. 계산 과정
    if op == "**":
        y = a**b
    elif op == "%":
        y = a % b
    elif op == "//":
        y = a//b
    else:
        print("not support")
        y = None

    return y


result = cal()
print(result)
