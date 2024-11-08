from collections import deque

N, M, K = list(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(N)
]

save_tower = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            save_tower += 1

time_arr = [[0] * M for _ in range(N)]

# 우하좌상
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
dxs2 = dxs + [1, 1, -1, -1]
dys2 = dys + [-1, 1, -1, 1]

def get_weakest_tower():
    min_power, max_time, max_row, max_col = float('inf'), 0, 0, 0

    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                min_power, max_time, max_row, max_col = max(
                    (min_power, max_time, max_row, max_col),
                    (arr[i][j], time_arr[i][j], i, j),
                    key=lambda x: (-x[0], x[1], x[2]+x[3], x[3])
                )

    return max_row, max_col

def get_strongest_tower(w_x, w_y):
    max_power, min_time, min_row, min_col = 0, 0, 0, 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] and (i, j) != (w_x, w_y):
                max_power, min_time, min_row, min_col = min(
                    (max_power, min_time, min_row, min_col),
                    (arr[i][j], time_arr[i][j], i, j),
                    key=lambda x: (-x[0], x[1], x[2]+x[3], x[3])
                )

    return min_row, min_col

def laser_attack(w_x, w_y, s_x, s_y):
    visited = [[False] * M for _ in range(N)]
    visited[w_x][w_y] = True

    q = deque()
    q.append((w_x, w_y, []))

    while q:
        qx, qy, q_list = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = (qx + dx) % N, (qy + dy) % M

            if arr[new_x][new_y] and not visited[new_x][new_y]:
                new_list = q_list + [(new_x, new_y)]
                if (new_x, new_y) == (s_x, s_y):
                    return new_list
                else:
                    visited[new_x][new_y] = True
                    q.append((new_x, new_y, new_list))

    return []

for turn in range(1, K + 1):
    # 1
    weak_x, weak_y = get_weakest_tower()
    arr[weak_x][weak_y] += N + M
    time_arr[weak_x][weak_y] = turn

    # 2
    strong_x, strong_y = get_strongest_tower(weak_x, weak_y)
    # print(weak_x, weak_y, strong_x, strong_y)

    # 2-1
    laser_route = laser_attack(weak_x, weak_y, strong_x, strong_y)

    if not laser_route:
        # 2-2
        for dx, dy in zip(dxs2, dys2):
            new_x, new_y = (strong_x + dx) % N, (strong_y + dy) % M
            if arr[new_x][new_y] and (new_x, new_y) != (weak_x, weak_y):
                laser_route.append((new_x, new_y))
    else:
        laser_route = laser_route[:-1]

    attack_num = arr[weak_x][weak_y]
    if arr[strong_x][strong_y] > attack_num:
        arr[strong_x][strong_y] -= attack_num
    else:
        arr[strong_x][strong_y] = 0
        save_tower -= 1

    attack_num = attack_num // 2
    for lx, ly in laser_route:
        if arr[lx][ly] > attack_num:
            arr[lx][ly] -= attack_num
        else:
            arr[lx][ly] = 0
            save_tower -= 1

    if save_tower == 1:
        break

    # 4
    laser_route = laser_route + [(weak_x, weak_y), (strong_x, strong_y)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] and (i, j) not in laser_route:
                arr[i][j] += 1

max_p = max(max(p) for p in arr)
print(max_p)