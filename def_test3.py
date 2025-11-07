#def_test2.py
#함수
#1. 내장함수print() input() len()
#2. 사용자 정의 함수 내가 def만든
#3. 라이브러리 함수  import를 이용해 사용 turtle random
"""
import time

print("안녕")
time.sleep(1)
print("반가워")
"""

#카운트다운

import time
a = 1
for i in range(10,0,-1):
    print(i)
    i += 1
    time.sleep(1)
print("1살 더 먹었다")
