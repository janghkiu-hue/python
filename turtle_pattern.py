

from turtle import *
import turtle
"""
# 펜 색상 설정: 테두리는 'red', 채우는 색은 'yellow'로 설정
color("green", "yellow")

# 도형을 채우기 시작 (begin_fill로 채움 영역을 시작)
begin_fill()

# 반복문을 사용하여 도형을 그립니다.
while True:
    # 200픽셀만큼 앞으로 이동
    forward(300)
    
    # 170도 왼쪽으로 회전
    left(170)
    
    # 현재 위치가 시작점에 가까운지 확인
    if abs(pos()) < 1:
        # 위치가 시작점에 매우 가까우면(정확하게는 1픽셀 이하) 반복문을 종료
        break

# 도형의 채우기를 종료
end_fill()

# 그리기 작업이 끝났음을 알리고 윈도우를 닫지 않도록 유지
done()
"""

color("green", "yellow")

# 도형을 채우기 시작 (begin_fill로 채움 영역을 시작)
begin_fill()

# 반복문을 사용하여 도형을 그립니다.
while True:
    # 200픽셀만큼 앞으로 이동
    forward(5)
    
    # 170도 왼쪽으로 회전
    left(1)
    circle(200,7)
    speed(0)
    # 현재 위치가 시작점에 가까운지 확인
    if abs(pos()) < 1:
        # 위치가 시작점에 매우 가까우면(정확하게는 1픽셀 이하) 반복문을 종료
        break

# 도형의 채우기를 종료
end_fill()

# 그리기 작업이 끝났음을 알리고 윈도우를 닫지 않도록 유지
done()
