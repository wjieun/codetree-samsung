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

time = [[0] * M for _ in range(N)]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

dxs2 = dxs + [1, 1, -1, -1]
dys2 = dys + [1, -1, 1, -1]

def get_weak_tower():
    min_power, max_time, row, col = float('inf'), 0, 0, 0

    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                min_power, max_time, row, col = max(
                    (min_power, max_time, row, col),
                    (arr[i][j], time[i][j], i, j),
                    key=lambda x: (-x[0], x[1], x[2] + x[3], x[3])
                )

    return row, col

def get_strong_tower(wr, wc):
    max_power, min_time, row, col = 0, float('inf'), 0, 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] and (i, j) != (wr, wc):
                max_power, min_time, row, col = min(
                    (max_power, min_time, row, col),
                    (arr[i][j], time[i][j], i, j),
                    key=lambda x: (-x[0], x[1], x[2] + x[3], x[3])
                )

    return row, col

def laser(x1, y1, x2, y2):
    min_dis = float('inf')
    min_way = []

    visited = [[0] * M for _ in range(N)]
    visited[x1][y1] = True

    q = deque()
    q.append((x1, y1, [(x1, y1)]))

    while q:
        qx, qy, qw = q.popleft()
        if len(qw) >= min_dis - 1:
            continue

        for dx, dy in zip(dxs, dys):
            new_x, new_y = (qx + dx) % N, (qy + dy) % M

            if arr[new_x][new_y] and not visited[new_x][new_y] and (new_x, new_y) not in qw:
                visited[new_x][new_y] = True

                if (new_x, new_y) == (x2, y2):
                    min_way = qw + [(new_x, new_y)]
                    min_dis = len(min_way)
                    break

                q.append((new_x, new_y, qw + [(new_x, new_y)]))

    return min_way


for turn in range(1, K+1):
    # 1
    weak_r, weak_c = get_weak_tower()
    arr[weak_r][weak_c] += N + M
    time[weak_r][weak_c] = turn

    # 2
    strong_r, strong_c = get_strong_tower(weak_r, weak_c)

    # 2-1
    attack_way = laser(weak_r, weak_c, strong_r, strong_c)

    if attack_way:
        attack_way = attack_way[1:-1]
    else:
        # 2-2
        for dx, dy in zip(dxs2, dys2):
            new_x, new_y = (strong_r + dx) % N, (strong_c + dy) % M
            if arr[new_x][new_y] and (new_x, new_y) != (weak_r, weak_c):
                attack_way.append((new_x, new_y))

    attack_num = arr[weak_r][weak_c]
    if arr[strong_r][strong_c] <= attack_num:
        arr[strong_r][strong_c] = 0
        save_tower -= 1
    else:
        arr[strong_r][strong_c] -= attack_num

    if save_tower == 1: break

    attack_num = attack_num // 2
    for att_x, att_y in attack_way:
        if arr[att_x][att_y] <= attack_num:
            arr[att_x][att_y] = 0
            save_tower -= 1
        else:
            arr[att_x][att_y] -= attack_num

    if save_tower == 1: break

    attack_way = attack_way + [(weak_r, weak_c), (strong_r, strong_c)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] and (i, j) not in attack_way:
                arr[i][j] += 1

max_num = max(max(ar) for ar in arr)
print(max_num)