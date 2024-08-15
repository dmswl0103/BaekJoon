import sys
input = sys.stdin.readline 
n = int(input())

for i in range(n):
    m = sum(list(map(int,list(str(i)))))
    if n == i + m:
        print(i)
        break
else:
    print(0) 



