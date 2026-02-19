import sys

# 입력: 8줄, 각 줄에 0~6
grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(8)]

# 사용된 도미노를 표시할 배열
# (a,b)와 (b,a)를 같은 도미노로 보고, (min(a,b), max(a,b))를
# idx = a*7 + b 로 매핑해서 used[idx]로 관리 (크기 49면 충분)
used = [False] * 49

# 칸 채움 여부
filled = [[False] * 7 for _ in range(8)]

# 두 방향만 보면 충분 (오른쪽, 아래)
dirs = [(0, 1), (1, 0)]

def idx_of(a, b):
    if a > b:
        a, b = b, a
    return a * 7 + b

def dfs(pos):
    # pos: 0..55 선형 인덱스
    if pos == 56:
        return 1  # 모두 채움

    r, c = divmod(pos, 7)

    # 이미 채워졌으면 다음 칸
    if filled[r][c]:
        return dfs(pos + 1)

    total = 0
    # 이 칸을 시작으로 도미노를 오른쪽/아래로 둠
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 8 and 0 <= nc < 7 and not filled[nr][nc]:
            a, b = grid[r][c], grid[nr][nc]
            idx = idx_of(a, b)
            if not used[idx]:
                # 놓기
                used[idx] = True
                filled[r][c] = filled[nr][nc] = True
                total += dfs(pos + 1)
                # 되돌리기
                filled[r][c] = filled[nr][nc] = False
                used[idx] = False

    return total

print(dfs(0))
