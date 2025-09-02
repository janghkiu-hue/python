import keyword
import calendar
import datetime


#print(keyword.kwlist)
#print(calendar.month(2009,9,12))
today = datetime.date.today()
print(today.year)
print(today.month)
print(today.day)
now = datetime.datetime.now()
print(now.year,now.month,now.day,now.hour,now.minute,now.second) 
#입출력 복습


"""
# 비만도(bmi)구하기 몸무게/(키의제곱) *10000

height=int(input("키를 적어주세요:"))
weight=int(input("몸무게를 적어주세요 :"))
bmi = weight/(height**2)*10000
print(f"당신의bmi는 {round(bmi, 2)} 입니다")


#반올림 round()
pi = 3.6451
print(round(pi, 1))
print(round(pi, 2))            
'''

#사칙연산 계산기 만들기
num1= int(input("첫번째 값 입력 : "))
num2=int(input("두번째 값 입력 : "))
add_result = num1 + num2         
mul_result = num1 * num2
sub_result = num1 - num2
div_result = num1 / num2
#계산된 결과 출력하기
print(f"덧셈 결과는 {add_result} 입니다")
print(f"곱셈 결과는 {mul_result} 입니다")
print(f"뺄셈 결과는 {sub_result} 입니다")
print(f"나눗셈 결과는 {div_result} 입니다")
"""
#변수


