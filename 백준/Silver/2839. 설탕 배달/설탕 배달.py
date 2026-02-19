n = int(input())

"""
dp[n] = min(dp[n -3], dp[n - 5]) + 1
"""

dp = [10000] *(n + 1)
dp[3] = 1
if n > 4:
    dp[5] = 1

for x in range(6,n + 1):
    dp[x] = min(dp[x - 3], dp[x -5]) + 1

if dp[n] < 10000:
    print(dp[n])
else:
    print(-1)
