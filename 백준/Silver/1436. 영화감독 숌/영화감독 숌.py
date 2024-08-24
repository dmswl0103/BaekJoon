import sys
input = sys.stdin.readline
n = int(input())
num = 666 
cnt = 0
# 어떤 숫자 안에 꼭 들어가야 하는 종말의 수 
# 안에 들어가는 게 목표니까 문자열로 따짐 
while True:
    if '666' in str(num):
        cnt += 1 

    if cnt == n:
        break 

    num +=1 # 숫자 1씩 증가시키면서 따짐 
    # 브루트포스 

print(num)