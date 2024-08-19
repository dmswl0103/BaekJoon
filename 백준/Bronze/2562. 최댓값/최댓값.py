import sys
input = sys.stdin.readline
num = []
for _ in range(9):
    num.append(int(input().rstrip()))
# rstrip은 문자열에만 쓸 수 있으니까 int로 변환은 rstrip 쓴 이후에 
max = 0 
for i in range(1, 9):
    if num[i] > num[max]:
        max = i
print(num[max])
print(max+1)
