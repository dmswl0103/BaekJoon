import sys
input = sys.stdin.readline 
n = int(input())
arred= []
for i in range(n):
    arred.append(input().rstrip())
arr1 = set(arred)
arr = list(arr1)
arr.sort()
arr.sort(key = len) # sort 정렬이 문자까지, 기준 넣기 가능
for i in arr:
    print(i)
