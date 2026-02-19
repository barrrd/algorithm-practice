# 음의 아닌 정수 x의 5432 감소
# N 번쨰 감소하는 수
from collections import deque
N = int(input())

q= deque()
tlst = []

for i in range(10):
    q.append(i)
    tlst.append(i)

# print(q)
# print(tlst)

deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
while q:
    current = q.popleft()
    last = current % 10
    # print(current)
    # print(last)
    
    for c in range(last):
        next_num = current * 10 + c 
        # print(next_num)
        # print()
        tlst.append(next_num)
        q.append(next_num)

if N >= len(tlst):
    # N번째 감소하는 수가 없을 경우
    print(-1)
else:
    # 감소하는 수 리스트를 오름차순으로 정렬
    tlst.sort()
    
    # N번째 감소하는 수를 출력합니다.
    print(tlst[N])