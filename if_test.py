#if_test2.py
#반올림 round() 포매팅
"""
print(round(5.5795,2))#5.58
print(round(5.5295,1))#5.5
print(round(5.5295,0))#6.0
print(round(5.5295,-1))#10
print(round(5.5295))#6
a = round(5.5295)
b = round(5.5295,0)
print(type(a)) #int
print(type(b)) #float

#포매팅
print("{:.1f}".format(3.5289))
print("{:.0f}".format(3.5289))
print("{:.3f}".format(3.5289)) #3.529

print("{0}과{0}".format(3.5555, 3.7777))# 인덱스
print("{0}과{1}".format(3.5555, 3.7777))
print("{0:.2f}과{1:.1f}".format(3.5555, 3.7777))
print("{1:.1f}과{0:.2f}".format(3.5555, 3.7777))


a = 5
b = 8
if a>=b:
    print(a+b)
else:
    print(a*b)

money = int(input("무슨 집을 살까? "))

if money >= 10000000000:
    print("시그니엘!")
elif money >= 5000000000:
    print("강남 한강뷰 !")
elif money >= 500000000:
    print("송도 아파트 !")
elif money >= 50000000:
    print("투룸 빌라!")
else:
    print("서울역 3번출구 그냥 죽어!.")
"""

scores = [85, 92, 78, 95, 88]

print("입력된 점수: ", scores)
print("전체학생수:", len (scores))
if len(scores)>0:
    max_score = max (scores)
    min_score = min(scores)
    tot_score = sum(scores)
    avg_score = sum(scores)/len(scores)
    print("최고 점수 : ", max_score,"점")
    print("최저 점수 : ", min_score,"점")
    print("총합 점수 : ", tot_score,"점")
    print("평균 점수 : ","{:.2f}".format(avg_score),"점")
else:
    print("입력된 점수가 없습니다.")
