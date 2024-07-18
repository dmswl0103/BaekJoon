import sys
input = sys.stdin.readline 
n = int(input())
for i in range(0, n):
    while i >= 0:
        print("*", end= "")
        i-=1
    print(" ")

# 파이썬에서 print문으로 줄바꿈 없이 출력되게 하려면 end 사용 

