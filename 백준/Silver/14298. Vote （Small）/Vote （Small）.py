# 1.factorical
def factorical(n:int):
    if n < 2:
        return 1
    else:
        return n * (factorical(n-1))
    
# 2.combination
def combination(n,r):
    N = factorical(n)
    R = factorical(r)
    N_R = factorical(n-r)
    return N//(R * N_R)

# 3. dfs
def dfs (num_a,num_b):
    global total_case, count
    plus_list = [[1,0],[0,1]]
     
    if num_a == datas[0] and num_b == datas[1]:
        count +=1
        return
    
    if num_a > datas[0] or num_b > datas[1]:
        return 

    for i in range(2):
        a_val, b_val = plus_list[i]
        na, nb = num_a + a_val, num_b + b_val

        if na <= nb:
            continue
        
        elif na > datas[0] or nb > datas[0]:
            continue

        elif na > nb:
            dfs(na, nb)       
            
# 0. 입력
T = int(input())
for k in range(T):
    datas = list(map(int,input().split()))
    # datas = [list(map(int, input().split())) for _ in range(T)]
    # print(datas)

    # 1. 경우의 수
    total_case = combination(datas[0] + datas[1], datas[1])
    # print(total_case)

    # 2. visited_num
    visited_num = [0,0]

    # 3. graph
    # graph = [[0] * (total_case + 1) for _ in range(2)]
    # graph[0][1] = 1
    # graph_a = graph[0]
    # graph_b = graph[1]
    # # print(graph)

    count = 0
    # 4. dfs
    if datas[0] == 0:
        print(f'Case #{k+1}: {count/total_case:.8f}')
    else:
        dfs(1,0)
        p = count/total_case
        print(f'Case #{k+1}: {p:.8f}')
