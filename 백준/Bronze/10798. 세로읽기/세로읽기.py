import sys

word = [] 
for i in range(5):
    input = sys.stdin.readline().rstrip()
    word.append(input) # 줄 단위로 리스트 저장 

for i in range(15):
    for j in range(5): # 현재 선택된 단어의 순서 
        if i < len(word[j]):
            print(word[j][i], end = "")
