import sys
input = sys.stdin.readline
n=int(input())
for j in range(n):
    stack=[]
    string=input()
    for i in string:
        if i=='(':
            stack.append(i)
        elif i==')':
            if '(' in stack:
                stack.pop() 
            else:
                print("NO")
                breakpoint = 1
                break
            
    if breakpoint == 1:
        breakpoint = 0
        continue
    if len(stack)!=0:
        print("NO")
    else:
        print("YES")