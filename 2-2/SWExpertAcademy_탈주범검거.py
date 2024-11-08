from collections import deque

N, M, R, C, L = list(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(N)
]

# 상하좌우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

d_mapping = {
    1: [0, 1, 2, 3], 2: [0, 1], 3: [2, 3],
    4: [0, 3], 5: [1, 3], 6: [1, 2], 7: [0, 2]
}

dxy_mapping = {
    (-1, 0): 0, (1, 0): 1, (0, -1): 2, (0, 1): 3
}

def in_range(a, b):
    return 0 <= a < N and 0 <= b < M

visited = [[False] * M for _ in range(N)]
visited[R][C] = True

q = deque()
q.append((R, C, 1))

while q:
    qx, qy, qc = q.popleft()

    num = arr[qx][qy]
    if num and qc < L:
        for d in d_mapping[num]:
            new_x, new_y = qx + dxs[d], qy + dys[d]

            if in_range(new_x, new_y) and not visited[new_x][new_y] \
                    and arr[new_x][new_y]:
                new_num = arr[new_x][new_y]
                new_d_list = d_mapping[new_num]

                if dxy_mapping[(-dxs[d], -dys[d])] in new_d_list:
                    visited[new_x][new_y] = True
                    q.append((new_x, new_y, qc + 1))

v_sum = sum(sum(v) for v in visited)
print(v_sum)