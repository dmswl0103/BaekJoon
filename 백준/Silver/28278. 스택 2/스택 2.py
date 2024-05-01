import sys
input = sys.stdin.readline

stack=[]
n=int(input())
input_line = []
for _ in range(n):
    
    input_line=input().split()
    command=int(input_line[0])

    if command==1:
        x=int(input_line[1])
        stack.append(x)
    elif command==2:
        if len(stack)!=0:
            x = stack.pop()
            print(x)
        else:   
            print(-1)
    elif command==3:
        print(len(stack))
    elif command==4:
        if len(stack)==0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
