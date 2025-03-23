import sys
input = sys.stdin.readline
n = int(input())
tree = [64] 

while sum(tree) > n:
    short = tree[-1]//2 
    last = tree.pop()
    if short + sum(tree) >= n: 
        tree.append(short)  
    else:
        tree.append(short)
        tree.append(short)
print(len(tree))

        
