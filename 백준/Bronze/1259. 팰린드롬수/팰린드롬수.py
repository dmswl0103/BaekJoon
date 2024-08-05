import sys
input = sys.stdin.readline
while True:
    pal = input().rstrip()
    rev = "".join(reversed(pal))
    if pal == '0':
        break
    elif pal == rev:
        print("yes")
    else:
        print("no")

# reversed 함수는 이터레이터를 반환하기 때문에 ''.join()안에 넣어서 문자열로 반환