def combination(arr,m):
    result = []

    def backtrack(start, path):
        if len(path) == m:
            result.append(path[:])
            return
        for i in range(start,len(arr)):
            path.append(arr[i])
            backtrack(i+1,path)
            path.pop()
    backtrack(0,[])
    return result

# 1. 입력
N, M = list(map(int,input().split()))
data = [i for i in range(1,N+1)]
# print(data)

# 2. combination
result  = combination(data,M)
# print(result)

for x in result:
    print(*x)