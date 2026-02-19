import sys
# 입력 N을 문자열로 받습니다.
N = sys.stdin.readline().strip()

def solve():
    L = len(N)
    
    # 1. 예외 처리: N이 모두 '9'로만 이루어진 경우
    if all(c == '9' for c in N):
        print('1' + '0' * (L - 1) + '1')
        return

    # 2. 왼쪽 절반(가운데 포함)을 구합니다.
    mid = (L + 1) // 2
    left_half = N[:mid]
    
    # 짝수 길이일 때: left_half + left_half의 역순
    # 홀수 길이일 때: left_half + left_half의 역순 (단, 가운데 숫자는 중복되므로 제외)
    candidate_P = left_half + left_half[:L - mid][::-1]

    # 3. N과 P 비교
    if candidate_P > N:
        # 3-A. P가 N보다 이미 큰 경우: P가 정답
        print(candidate_P)
    else:
        # 3-B. P가 N보다 작거나 같은 경우: 왼쪽 절반을 1 증가시킨 후 대칭
        
        # 왼쪽 절반을 정수로 변환하여 1 증가
        new_left_int = int(left_half) + 1
        new_left_half = str(new_left_int)
               
        # 짝수/홀수에 따라 대칭 기준을 다르게 적용
        if L % 2 == 0:
            # 짝수: 그대로 역순을 붙임
            result_P = new_left_half + new_left_half[::-1]
        else:
            # 홀수: 마지막 글자를 제외하고 역순을 붙임 (가운데 글자는 new_left_half의 마지막)
            result_P = new_left_half + new_left_half[:-1][::-1]
        
        print(result_P)

solve()


