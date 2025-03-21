import sys
input = sys.stdin.readline
while True:
    n, m = map(int, input().split())
    if n == 0 & m == 0:
        break
    else: 
        if n > m:
            print("Yes")
        else:
            print("No")