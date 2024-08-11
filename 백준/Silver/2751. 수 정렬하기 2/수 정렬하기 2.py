import sys
input = sys.stdin.readline 
n = int(input())
num = [] 

for i in range(n):
    k = int(input())
    num.append(k)
result = list(set(num))
result.sort()

for i in result:
    print(i)
