import sys
input = sys.stdin.readline

maximum = 0
row = col = 0
for i in range(9):
    arr = list(map(int,input().split()))
    for j in range(9):
        if arr[j] > maximum:
            maximum = arr[j]
            col = i
            row = j

print(maximum)
print(col+1, row+1)