from copy import deepcopy
from collections import deque

n, q = list(map(int, input().split()))
N = 2**n

arr = [
    list(map(int, input().split()))
    for _ in range(N)
]

rotate_level = list(map(int, input().split()))

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(a, b):
    return 0 <= a < N and 0 <= b < N

def get_max_group():
    visited = [
        [False] * N
        for _ in range(N)
    ]

    max_group = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and arr[i][j] > 0:
                group = 0
                visited[i][j] = True
                q = deque()
                q.append((i, j))

                while q:
                    qx, qy = q.popleft()
                    group += 1

                    for dx, dy in zip(dxs, dys):
                        new_x, new_y = qx + dx, qy + dy
                        if in_range(new_x, new_y) and arr[new_x][new_y] > 0\
                                and not visited[new_x][new_y]:
                            visited[new_x][new_y] = True
                            q.append((new_x, new_y))

                max_group = max(group, max_group)

    return max_group

for L in rotate_level:
    # 1
    new_arr = [
        [0] * N
        for _ in range(N)
    ]

    if L > 0:
        size, s_size = 2**L, 2**(L-1)
        for x in range(0, N, size):
            for y in range(0, N, size):

                for i in range(0, size, s_size):
                    for j in range(0, size, s_size):

                        for k in range(s_size):
                            for l in range(s_size):
                                new_arr[x + j + k][y + s_size - i + l] = arr[x + i + k][y + j + l]

        arr = new_arr

    # 2
    new_arr = deepcopy(arr)
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                count = 0
                for dx, dy in zip(dxs, dys):
                    new_x, new_y = i + dx, j + dy
                    if in_range(new_x, new_y) and arr[new_x][new_y] > 0:
                        count += 1

                if count < 3:
                    new_arr[i][j] -= 1

    arr = new_arr

a_sum = [sum(ar) for ar in arr]
print(sum(a_sum))

print(get_max_group())