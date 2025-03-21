import sys
input = sys.stdin.readline
n, m =map(int, input().split())
if n > m:
    print(abs(n-m))
else:
    print(abs(m-n))
