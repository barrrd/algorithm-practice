# [1] 입력
N = int(input()) # 기둥 수
data = [list(map(int,input().split())) for _ in range(N)]
data.sort(key= lambda x: x[0]) # x 길이 기준

# [2] 최대 높이 및 인덱스 찾기 (→ 오른쪽 끝 인덱스는 기존 max_hindex 유지)
max_height = -1
max_hindex = -1
for i in range(N):
    L, H = data[i]
    if H >= max_height:
        max_height = H
        max_hindex = i

# 추가: 최대 높이의 왼쪽/오른쪽 끝 인덱스
left_hindex = next(i for i, (_, h) in enumerate(data) if h == max_height)
right_hindex = max_hindex  # 기존 변수 재사용(오른쪽 끝)

# [3] 최대 높이 '왼쪽 끝' 전까지 left 스캔
sum = 0
best_max = -1
prev_x = data[0][0]

for i in range(left_hindex + 1):
    x, y = data[i]
    if y > best_max:
        if best_max > 0:
            sum += (x - prev_x) * best_max
        best_max = y
        prev_x = x

# [4] right 스캔: 오른쪽 끝에서 '오른쪽 최대 인덱스' 직전까지
best_max = 0
prev_x = data[N - 1][0]

for i in range(N - 1, right_hindex, -1):
    x, y = data[i]
    if y > best_max:
        sum += (prev_x - x) * best_max
        best_max = y
        prev_x = x

if best_max > 0:
    sum += (prev_x - data[right_hindex][0]) * best_max

# [5] 최대 높이 평평한 구간(첫 최대 L ~ 마지막 최대 L) 면적 추가
sum += (data[right_hindex][0] - data[left_hindex][0] + 1) * max_height

# 6. 최종 결과 출력
print(sum)