import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    string= input().strip()
    print(string[0] + string[-1])