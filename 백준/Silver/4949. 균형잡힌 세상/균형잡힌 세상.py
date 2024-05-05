import sys
input = sys.stdin.readline
while True:
    string=input().rstrip('\n') 
    stack=[]
    if string=='.':
        break
    else:
        
        for i in string:
            if i=='(' or i=='[':
                stack.append(i)
            elif i==')':
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(i)
                    break # 균형 잡힌 괄호 안에서 () 열리고 닫히고가 끝나는 경우도 있는데 
        
            elif i==']':
                if stack and stack[-1]=='[':
                    stack.pop()
                else:
                    stack.append(i)
                    break
        if breakpoint==1:
            breakpoint=0
            continue
        if len(stack)==0:
            print("yes")
        else:
            print("no")