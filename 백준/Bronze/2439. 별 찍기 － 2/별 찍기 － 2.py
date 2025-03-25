import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    for s in range(n-i-1):
        print(" ",end='')
    for k in range(i+1):
        print("*",end='')
    print("")
