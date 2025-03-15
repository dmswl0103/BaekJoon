num = list(map(int, input().split()))
s = 0
for n in num:
    s += n**2
verification = s % 10
print(verification)
