import sys
input = sys.stdin.readline

def find(start, M, num):
    while start <= M:
        s_set = set()
        for s in str(start):
            s_set.add(s)
        if len(s_set) == len(str(start)):
            # 동일하게 없는 거 
            num += 1
        start += 1
    return num


while True:
    try:
        N, M = map(int, sys.stdin.readline().split())
        print(find(N, M, 0))
        
        
    except EOFError:
        break
    except Exception:
        break