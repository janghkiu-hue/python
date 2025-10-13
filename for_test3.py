#for_test3.py
#제어문 반복문 for 문자열 리스트변수 range
"""
print("구구단 2단 출력")
for i in range(1,10):# i1~9
    print(f"2*{i}={2*i}")


print("구구단 8단 출력")
for i in range(1,10):# i1~9
    print(f"8*{i}={8*i}")

#구구단 4단 홀수만 찍기 4*1 4*3 4*5..4*9
print("구구단8단 출력")
for i in range(1,10,2):
    print(f"8*{i} = {8*i}")


print("구구단 2단 출력")
for i in range(1,10):# i1~9
    print(f"2*{i}={2*i}", end=' ')

#중복 for
count =0
for i in range(1,6): #i 1 2 3 4 5
    print("i값은",i)
    for j  in range(1,6): #j 1 2 3 4 5
        count +=1
        print(count,"hello")

# 구구단 2~9단 찍기
for i in range(1,10): # 단 2 3 4 5 6 7 8 9
    #print(i,"단") #8번
    for j in range(2,10):
         print(f"{j} * {i} = {i*j:>2}", end=' ')
    print() #다음줄로 내려주는 효과

#print 포매팅 정렬
name = "장경효"

print(f"name:<10}") #왼쪽정렬
print(f"name:^10}") #오른쪽정렬
print(f"name:>10}") #가운데정렬

#반복 별찍기
for i in range(1,6):
    print("*"i)
print()
for i in range(5,0,-1):
    print("*"*i)

for i in range(1,6):#0 1 2 3 4
    for j in range(0,i):
        print("*",end='')
    print()
"""
for i in range(0,10):
    print(f"{"*"*i:>40}"f"{"*"*i:<40}")























































