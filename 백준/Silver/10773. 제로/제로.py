k = int(input())
stack = []

for i in range(k):
    user_input = int(input())
    if user_input != 0:
        stack.append(user_input)
    else:
        if stack:
            stack.pop()  
stack_sum = sum(stack)

print(stack_sum)