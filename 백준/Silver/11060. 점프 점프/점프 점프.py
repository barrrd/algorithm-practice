from collections import deque

def bfs():
    global visited
    q = deque([(0,0)])
    visited[0] = True
    locate = 0
    while q:
        locate, move_cnt = q.popleft()
        # print(f"locate: {locate} move_cnt:{move_cnt}")
        if locate == N-1:
            return move_cnt
        
        max_jump_number = datas[locate]
        # print(f" max_jump_number: { max_jump_number}")

        if max_jump_number != 0:
            # print(f" max_jump_number: { max_jump_number}")
            for i in range(1,max_jump_number+1):
  
                # print(visited[locate+i])
                if locate + i < N and not visited[locate+i]:
                    # print(locate+i)
                    visited[locate+i] = True
                    q.append((locate+i,move_cnt+1))

    if locate != N-1:
        return -1

# 1. 입력
N = int(input())
datas = list(map(int,input().split()))
# print(N,datas)

# 2. visited = []
visited = [False]*N

print(bfs())