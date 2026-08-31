def solution(arr):
    """
    1. dp 상태
       max_dp[i][j]:
       i번째 숫자 ~ j번째 숫자까지 계산했을 때의 최댓값

       min_dp[i][j]:
       i번째 숫자 ~ j번째 숫자까지 계산했을 때의 최솟값

    2. 초기값
       숫자 하나만 있는 경우
       max_dp[i][i] = min_dp[i][i] = nums[i]

    3. 이전 상태
       [i ~ k] 연산자 [k+1 ~ j]

    4. 점화식
       '+' :
           max = 왼쪽 max + 오른쪽 max
           min = 왼쪽 min + 오른쪽 min

       '-' :
           max = 왼쪽 max - 오른쪽 min
           min = 왼쪽 min - 오른쪽 max
    """
    # 0. init
    nums = []
    ops = []
    for i in range(len(arr)):
        if i % 2 == 0:
            nums.append(int(arr[i]))
        else:
            ops.append(arr[i])
    
    n = len(nums)
    
    # 1~2: dp 상태 + 초기값
    max_dp = [[-float("inf")]*n for _ in range(n)]
    min_dp = [[float("inf")]*n for _ in range(n)]
    
    for i in range(n):
        max_dp[i][i] = nums[i]
        min_dp[i][i] = nums[i]
    
    for length in range(2, n + 1):
        
        for i in range(n - length + 1):
            j = i + length - 1
            
            for k in range(i, j):
                
                if ops[k] == "+":
                    cand_max = max_dp[i][k] + max_dp[k + 1][j]
                    cand_min = min_dp[i][k] + min_dp[k + 1][j]
                else:                    
                    cand_max = max_dp[i][k] - min_dp[k + 1][j]
                    cand_min = min_dp[i][k] - max_dp[k + 1][j]
                
                max_dp[i][j] = max(max_dp[i][j], cand_max)
                min_dp[i][j] = min(min_dp[i][j], cand_min)
                    
    
    answer = -1
    answer = max_dp[0][n-1]
    return answer