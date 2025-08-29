# 출력 포매팅 표준 함수

name = "장경효"
profile= """
안녕하세요
저는 인평자동차고등학교
AI소프트웨어과
1학년 2반 장경효입니다. 
"""
'''
print(profile)

name= "장경효"
age = 17

print("장경효")
print("나의 소개: " ,profile)
print("나의 나이" , age)
print("내 이름은"+ name+"이고 내소개는\""+profile+"\"이야")
print("내 이름은", name+"이고 내소개는\""+profile+"\"이야")

# 문자열 포매팅
name= "장경효"
age = 17
print("이름: "+name+ " 나이:", age)
print("이름: ",name, "나이:", age)
print("이름:%s, 나이: %d"%(name, age))
print("이름:{}, 나이: {}".format(name, age))
print(f"이름: {name} 나이: {age}")

a = 11
print("%d는 16진수로 %x"%(a,a))
'''
name = "장 경 효!!"
print(len(name))
print(len(profile))
number = [1,5,-2,0,6]
print("최대값은 ",max(number)) #max() 최대값 구하기
print("최소값은 ",min(number)) #min() 최소값 구하기
print("합계는  ",sum(number)) #sum() 최대값 구하기
print("평균은  ",sum(number)/len(number)) #평균 구하기
#pow()
print(pow(5,9)) #5**9
print(5**9)

a = "I Love Python"
print(a.lower()) # 소문자로 변환 
print(a.upper()) # 대문자로 변환

