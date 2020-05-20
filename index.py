

"""

1. 입력 > a,b, 


2. 출력 a+b
"""

import sys

a, b = map(int, input().split())  # 입력 1 2

"""
a, b = map(int, "1 2".split()) 
a, b = map(int, ["1","2"]) 
a, b = [1,2]
"""
print(a+b)
