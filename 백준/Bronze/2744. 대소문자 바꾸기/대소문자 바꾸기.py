s = input()
res=""
for i in s:
    if i==i.lower():
        res += i.upper()
    else:
        res += i.lower()
print(res)

