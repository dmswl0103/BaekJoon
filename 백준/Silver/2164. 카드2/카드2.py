import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
queue=deque([])
for i in range(1,n+1):
    queue.append(i)
    # append에는 인자를 무조건 적어야 하는 듯 

while len(queue)>1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])