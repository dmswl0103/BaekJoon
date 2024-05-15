from collections import deque

# 입력받기
n, k = map(int, input().split())

# deque 초기화
queue = deque(range(1, n+1))

# 결과 저장용 리스트
result = []

# k-1번 회전하고 k번째 요소를 제거하는 작업 반복
while queue:
    queue.rotate(-(k-1))
    result.append(queue.popleft())

# 결과 출력
print('<' + ', '.join(map(str, result)) + '>')
