import sys
input = sys.stdin.readline 
burger = []
ju = []
for i in range(3):
    burger.append(int(input()))
for j in range(2):
    ju.append(int(input()))
burger.sort()
ju.sort()
print(burger[0]+ju[0]-50)