import sys
input = sys.stdin.readline
n = input().rstrip().split()
str = sorted(n) 
if n==str:
    print("ascending")
elif n==str[::-1]:
    print("descending")
else:
    print("mixed")