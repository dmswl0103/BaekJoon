import sys
input = sys.stdin.readline 

test = int(input()) 
for i in range(test):
    cnt = 0
    k = int(input())
    n = int(input())
    f0 = [x for x in range(1, n+1)] # 0층 리스트 

    for x in range(k):
        new = []
        for j in range(n):
            new.append(sum(f0[:j+1])) # sum을 이용하여 다음 층수를 구할 수 있는 거 
        f0 = new.copy() # 테스트 케이스에 들어온 층수에 맞춰 그 층수 이전까지 
        # 이전 층수를 계속 업데이트함 
    print(f0[-1])
 

    