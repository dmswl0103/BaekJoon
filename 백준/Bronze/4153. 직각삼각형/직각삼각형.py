import sys
input = sys.stdin.readline 
while True:
    trian = sorted(list(map(int, input().split())))
    if trian[0] == 0:
        break 
    if trian[2]**2 == trian[0]**2 + trian[1]**2:
        print("right")
    else:
        print("wrong")
    
