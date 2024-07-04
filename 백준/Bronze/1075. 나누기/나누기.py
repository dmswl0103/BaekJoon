import sys
input = sys.stdin.readline

N = input().strip()
F = int(input().strip())
two = int(N[:-2]+"00")

for i in range(100):
    out = two + i
    if out % F == 0:
        # i를 출력할 때 한 자리이면 0을 추가해야 함 
        # 두 자리로 형식화된 숫자를 출력하는 방법 
        # 자리가 남을 때 넣을 수, 출력하고 싶은 자릿수 
        print(f"{i:02}")
        break