import sys
# 빠른 입출력을 위해 sys.stdin.readline을 사용할 수 있습니다.
# input = sys.stdin.readline 

# 1. N과 X를 입력받습니다.
try:
    # 한 줄에 N과 X가 공백으로 구분되어 주어지므로, split() 후 map(int, ...)로 정수 변환합니다.
    # N은 사용하지 않을 수도 있지만, 문제 조건에 맞추어 입력받습니다.
    N, X = map(int, input().split())
except EOFError:
    # 입력이 없는 경우 처리
    sys.exit()
except ValueError:
    # 잘못된 형식의 입력 처리
    sys.exit()

# 2. 수열 A를 입력받습니다.
try:
    # 수열 A의 N개의 정수가 공백으로 구분되어 주어지므로, 리스트로 저장합니다.
    A = list(map(int, input().split()))
except EOFError:
    sys.exit()
except ValueError:
    sys.exit()

# 결과를 저장할 리스트를 초기화합니다.
result = []

# 3. 수열 A의 각 원소를 순서대로 확인합니다.
for number in A:
    # 4. 각 원소가 X보다 작은지 비교합니다.
    if number < X:
        # 5. 조건을 만족하면 결과 리스트에 추가합니다.
        result.append(str(number)) # 출력 시 공백 구분을 위해 문자열로 변환하여 저장

# 결과 리스트의 모든 요소를 공백으로 구분하여 출력합니다.
# join() 메소드는 리스트의 요소들을 지정된 구분자(여기서는 공백 ' ')로 연결하여 하나의 문자열로 만듭니다.
print(' '.join(result))