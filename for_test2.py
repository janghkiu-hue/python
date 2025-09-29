
"""
k = int(input('구분: 1. 주간 2. 야간?'))
m = int(input('대상: 1. 대인 2. 소인?'))

if k ==1: #주간
    if  m==1:
        pay = 50000
    else:
        pay = 40000
else: # 야간
    if m==1:
        pay = 30000
    else:
        pay =20000

print(f"당신의 입장료는 {pay}원입니다")


#for 반복문
#2. 리스트 변수를 이용한 반복문
fruit = ('mango' , 'apple' , 'orange' , 'kiwi' , 'banana')
#print(fruit[2])
count = 0 
for i in fruit:
    count +=1  #count = count + 1
    print(count, " . ",i)


n = [0,1,2,3,4,]
for i in n:
    print(i+1," . 안녕하세요")


food = ("물냉면" , "비빔냉면" , " 함흥냉면" , "평양냉면" , "70년전통 할머니 냉면")

print(type(food))

for f  in food:
        print(f)



number = [273,103,5,32,65,9,72,880,99,58]

for n in number:
    if  n  %2 ==0:
         print(f"{n}은 짝수입니다")   #print(n, "은 짝수입니다")
    else:
        print(f"{n}은 홀수입니다")

number = [273,103,5,32,65,9,72,880,99,58]

#273은 3자리수입니다 #len   str

for n in number:
    print(f"{n}은 {len(str(n))}자리수 입니다")
"""

score_list = [98,58,65,78,44]
count = 0
total = 0
i = 0
for score in score_list:
    count += 1
    if score >=60:
        total  += score
        i+= 1
        print(f"{count}번 학생은{score}점으로 합격입니다")
    else:
      print(f"{count}번 학생은 {score}점으로 불합격입니다")

print(f"합격한 친구들의 총점은 {total}점 입니다")
print(f"합격한 친구들의 총점은 {round(total/i,2)}점 입니다")



















