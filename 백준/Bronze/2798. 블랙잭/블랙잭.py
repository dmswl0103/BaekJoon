import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num = list(map(int, input().rstrip().split()))
# 리스트 정렬할 필요 없음, 하나씩 다 조합해야 함 
total = 0 
for i in range(n): # 리스트 수들 전체 봐야 함 
    for j in range(i+1, n):
        for k in range(j+1, n):
            if num[i] + num[j] + num[k] > m:
                continue
            else:
                # total 변수를 이전 total과 비교해서 더 가까운 값 저장
                total = max(total,num[i] + num[j] + num[k])
print(total)


