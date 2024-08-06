import sys
input = sys.stdin.readline 
n = int(input())
num = list(map(int, input().split()))
prime = 0 
for i in num:
    cnt = 0
    for j in range(1, i): 
        if i % j == 0:
            cnt += 1
            continue
    if cnt == 1:
        prime +=1 
print(prime)
        

