w, h = map(int,input().split())
num = int(input()) # 상점 수
tloc = [list(map(int,input().split())) for _ in range(num+1)]
# print(tloc)

P = 2 * (w + h)

cloc = []  # [cw]
for _, (t, c) in enumerate(tloc, 1):
    # 시계방향 누적 거리 (NW=0 기준)
    if t == 1:      # 북
        cw = c
    elif t == 4:    # 동
        cw = w + c
    elif t == 2:    # 남
        cw = w + h + (w - c)
    elif t == 3:    # 서
        cw = 2*w + 2*h - c

    cloc.append(cw)

start = cloc.pop()
start # [cw,ccw]


sum = 0
sc = start
for c in cloc:
    best_min = float('inf')
    best_min = min(abs(c-sc), 2*(h+w) - abs(c- sc))
    sum +=best_min
print(sum)
