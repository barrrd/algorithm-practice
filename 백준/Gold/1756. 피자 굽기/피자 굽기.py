import sys
input = sys.stdin.readline

D, N = map(int, input().split())
depth = list(map(int, input().split()))
pizzas = list(map(int, input().split()))

# 1) 유효 지름으로 전처리: 위에서 아래로 non-increasing
for i in range(1, D):
    if depth[i] > depth[i-1]:
        depth[i] = depth[i-1]

# 2) 아래에서부터 피자를 하나씩 배치
pos = D - 1         # 현재 탐색 위치(0-index, 맨 아래)
last = -1           # 마지막 피자가 놓인 깊이(0-index 저장)

for s in pizzas:
    while pos >= 0 and depth[pos] < s:
        pos -= 1            # 이 위치엔 못 들어가니 위로 한 칸
    if pos < 0:
        print(0)            # 자리가 없음
        sys.exit(0)
    last = pos              # s 피자를 이 위치에 둠
    pos -= 1                # 다음 피자는 그 위부터 탐색

# 마지막 피자의 위치를 1-index로 출력
print(last + 1)
