#while_test.py
#제어문 - 선택문 반복문
#반복문 for range 문자열 리스트변수
#while
"""
i = 1
while i <=5:
    print(i, "안녕하세요")
    i = i + 1
print("끝")


for i in range(1,6):
    print(i,"안녕하세요")
print("끝")

i = 1
sum = 0
while i <=10001:
    sum += i
    i += 1
print('1부터 10가지의 합 : ',sum)         
#3부터 15까지 출력하는 while 반복문
i = 3
sum = 0
while i <=15:
    print(i)
    sum +=i
    i+=1

#무한반복
while True:
    jumsu = int(input("희망 영어 점수를 입력하세요:"))
    if jumsu>=0 and jumsu<=100:
        break
print("너는 영어시험에서" ,jumsu,"점을 받을거야")

# 키보드로부터 숫자 하나를 입력 받고 무한반복되다가
# 입력된 값이 4이면 탈출하세요.

while True:
    i = int(input("수 하나 입력하면.(종료시 4입력):"))
    if i==4:
        break
    else:
        print("당신이 입력한 수는 ",i," 입니다")
"""
fruit = ["사과", "용과", "포도", "망고"]
for i in fruit:
    print(i)

i= 0
while i< len(fruit):
    print(fruit[i])
    i += 1
          




























