# numpy  안 써도 되는 게 크기가 같으니까 걍 for 
import sys 
input = sys.stdin.readline
A, B = [], []
n, m = map(int, input().split())

for i in range(n*2):
    row = list(map(int,input().split()))
    if i<n:
        A.append(row)
    else:
        B.append(row)

for row in range(n):
    for col in range(m):
        print(A[row][col]+B[row][col], end=' ')
    print() 