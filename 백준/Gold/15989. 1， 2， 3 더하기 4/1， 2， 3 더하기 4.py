import sys

# 테스트 케이스 T를 먼저 받고
T = int(sys.stdin.readline())

# DP 테이블을 미리 최댓값까지 계산해 놓습니다.
# n은 10,000보다 작거나 같으므로 10001 크기의 배열 생성
dp = [0] * 10001
dp[0] = 1 # 합계 0을 만드는 방법은 1가지

# 사용할 숫자는 1, 2, 3
for num in [1, 2, 3]:
    # i는 num부터 시작해야 dp[i-num]이 유효함
    for i in range(num, 10001):
        dp[i] += dp[i - num]

# 각 테스트 케이스에 대해 미리 계산된 값을 출력
for _ in range(T):
    wanted = int(sys.stdin.readline())
    print(dp[wanted])