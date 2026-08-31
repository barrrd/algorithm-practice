def solution(money):
    answer = 0
    """
    1. dp 상태 + 초기화
    
    arr[0], arr[-1] 은 같이 못함,,,
    
    case1: dp[0] = money[0]
    
    case2. dp[0] = 0
    
    dp[x]: 0 ~ x 번째 집을 고려했을떄, 최대 money
    - max(x번째 o == x - 2 번째 + x 번째, x번쨰 x == x - 1번째 o)
    
    2. 이전상태 + 점화식
    dp[x] = max(dp[x-2] + money[x], dp[x-1])
    
    """
    
    # 1.init
    dp0 = [0]*len(money) # dp[0] = money[0]
    dp0[0] = money[0]
    dp0[1] = max(money[0], money[1])
    
    dp1 = [0]*len(money) # dp[0] = 0
    dp1[1] = money[1]
    
    
    for x in range(2, len(money)):
        if x != len(money) - 1 :
            dp0[x] = max(dp0[x-2] + money[x], dp0[x - 1])
        dp1[x] = max(dp1[x-2] + money[x], dp1[x - 1])
    
    
    answer = max(dp0[-2], dp1[-1])
    return answer