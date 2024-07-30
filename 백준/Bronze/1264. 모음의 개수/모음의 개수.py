import sys
input = sys.stdin.readline 


while True:
    n = 0
    eng = input().rstrip().lower()
    if eng == '#':
        break
    for i in eng:
        if i in "aeiou":
            n+=1
    print(n)

