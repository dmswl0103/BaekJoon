import sys
input = sys.stdin.readline
n, m, k = map(int,input().split())
if n != m and m != k and n != k:
    print(max(n, m, k)*100)
elif n == m and m == k:
    print(10000+m*1000)
else:
    if n == m or n == k:
        print(1000+n*100)
    else:
        print(1000+m*100)
