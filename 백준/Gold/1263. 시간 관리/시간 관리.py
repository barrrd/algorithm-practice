# N : 할 일
# Ti: i 번째 일을 처리하는 시간
# Si: 해당 시간 내에 차리
import sys
input = sys.stdin.readline
N = int(input())
tasks = []
for _ in range(N):
    t, s = map(int, input().split())
    tasks.append((t, s))


temp = sorted(tasks, key=lambda x: -x[1])
# print(temp)
res = temp[0][1]
# print(res)

for dt, et in temp:
    deadline = min(res,et)
    res  = deadline - dt

if res < 0:
    print(-1)
else:
    print(res)