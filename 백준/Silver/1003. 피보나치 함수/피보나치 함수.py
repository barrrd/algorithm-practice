import sys
input = sys.stdin.readline

# fib(n)의 (0호출수, 1호출수) 캐시
memo = {0: (1, 0), 1: (0, 1)}   # ← 핵심: 메모이제이션

def fibonacci(n):
    global result
    if n in memo:
        z, o = memo[n]
        result[0] += z
        result[1] += o
        return
    # 아직 캐시에 없으면 하위 문제를 먼저 채운 뒤 현재 n을 캐시에 저장
    fibonacci(n - 1)
    fibonacci(n - 2)
    z = memo[n - 1][0] + memo[n - 2][0]
    o = memo[n - 1][1] + memo[n - 2][1]
    memo[n] = (z, o)  # 다음부터는 바로 더해주기만 하면 됨

T = int(input())
for _ in range(T):
    n = int(input())
    result = [0, 0]
    fibonacci(n)
    print(result[0], result[1])
