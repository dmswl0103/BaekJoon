import sys 
from collections import deque
input=sys.stdin.readline
queue=deque([])
n=int(input())
for i in range(n):
    com=list(map(int,input().split()))
    if com[0]==1:
        queue.appendleft(com[1])
    elif com[0]==2:
        queue.append(com[1])
    elif com[0]==3:
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif com[0]==4:
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif com[0]==5:
        print(len(queue))
    elif com[0]==6:
        if queue:
            print(0)
        else:
            print(1)
    elif com[0]==7:
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif com[0]==8:
        if queue:
            print(queue[-1])
        else:
            print(-1)