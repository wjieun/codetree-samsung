from collections import deque

N, M, K = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(N)
]

attack_arr = [
    [-1 for _ in range(M)]
    for _ in range(N)
]

turret_num = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            turret_num += 1

# 우하좌상 우선순위
dxs = [0, 1, 0, -1, 1, 1, -1, -1]
dys = [1, 0, -1, 0, 1, -1, 1, -1]

def get_weak_turret():
    min_power = float('inf')
    turrets = []
    for i in range(N):
        for j in range(M):
            if 0 < arr[i][j] < min_power:
                min_power = arr[i][j]
                turrets = [[(attack_arr[i][j], i + j, j), (i, j)]]
            elif 0 < arr[i][j] == min_power:
                turrets.append([(attack_arr[i][j], i + j, j), (i, j)])
    turrets.sort(key=lambda t: t[0], reverse=True)
    return turrets[0][1]

def get_strong_turret(w_x, w_y):
    max_power = 0
    turrets = []
    for i in range(N):
        for j in range(M):
            if (i, j) != (w_x, w_y):
                if 0 < arr[i][j] > max_power:
                    max_power = arr[i][j]
                    turrets = [[(attack_arr[i][j], i + j, j), (i, j)]]
                elif 0 < arr[i][j] == max_power:
                    turrets.append([(attack_arr[i][j], i + j, j), (i, j)])
    turrets.sort(key=lambda t: t[0])
    return turrets[0][1]

def bfs(s_x, s_y, e_x, e_y):
    q = deque(); q.append((s_x, s_y, []))
    v = set(); v.add((s_x, s_y))

    while q:
        now_x, now_y, path = q.popleft()
        for dx, dy in zip(dxs[:4], dys[:4]):
            new_x, new_y = (now_x + dx) % N, (now_y + dy) % M
            if (new_x, new_y) not in v:
                if (new_x, new_y) == (e_x, e_y):
                    return path + [(new_x, new_y)]
                elif arr[new_x][new_y] > 0:
                    q.append((new_x, new_y, path + [(new_x, new_y)]))
                    v.add((new_x, new_y))

    return []

for turn in range(K):
    # 1
    weak_x, weak_y = get_weak_turret()
    attack_arr[weak_x][weak_y] = turn
    arr[weak_x][weak_y] += N + M

    # 2
    strong_x, strong_y = get_strong_turret(weak_x, weak_y)

    # (1)
    path = bfs(weak_x, weak_y, strong_x, strong_y)
    if not len(path):  # (2)
        for dx, dy in zip(dxs, dys):
            new_x, new_y = (strong_x + dx) % N, (strong_y + dy) % M
            if arr[new_x][new_y] > 0 and (new_x, new_y) != (weak_x, weak_y):
                path.append((new_x, new_y))
    else:
        path.pop()

    arr[strong_x][strong_y] -= arr[weak_x][weak_y]
    if arr[strong_x][strong_y] <= 0: turret_num -= 1
    if turret_num == 1: break
    for x, y in path:
        arr[x][y] -= arr[weak_x][weak_y] // 2
        if arr[x][y] <= 0: turret_num -= 1
        if turret_num == 1: break
    if turret_num == 1: break

    # 4
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 and (i, j) not in path + [(weak_x, weak_y), (strong_x, strong_y)]:
                arr[i][j] += 1

max_p = max([max(a) for a in arr])
print(max_p)