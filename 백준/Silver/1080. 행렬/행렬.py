n, m = map(int, input().split())
a = []
b = []
for _ in range(n):
    a.append(list(map(int, list(input()))))
for _ in range(n):
    b.append(list(map(int, list(input()))))

def check(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            if a[x][y] == 0:
                a[x][y] = 1
            else:
                a[x][y] = 0
            
cnt = 0
if (n <3 or m <3) and a != b:
    cnt = -1
else:
    for i in range(n-2):
        for j in range(m-2):
            if a[i][j] != b[i][j]:
                cnt += 1
                check(i, j)

if cnt != -1:
    if a!= b:
        cnt = -1
print(cnt)