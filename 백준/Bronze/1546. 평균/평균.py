import sys
input = sys.stdin.readline 
n = int(input())
arr = sorted(list(map(int,input().split())))
M = arr[-1]
ave = 0
for i in range(n):
    ave += arr[i]/M*100 
result = ave/n
print(result)