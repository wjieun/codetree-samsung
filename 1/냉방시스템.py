import copy
from collections import deque

n, m, k = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

office_list = []
aircon_list = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            office_list.append((i, j))
        elif arr[i][j] > 1:
            aircon_list.append((i, j, arr[i][j] - 2))

# 왼위오아
dxs = [0, -1, 0, 1]
dys = [-1, 0, 1, 0]

wall_arr = [
    # 위 벽, 왼쪽 벽
    [[False, False] for _ in range(n)]
    for _ in range(n)
]

cold_arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for _ in range(m):
    x, y, s = list(map(int, input().split()))
    wall_arr[x - 1][y - 1][s] = True

def make_cold():
    for x, y, d in aircon_list:
        dx, dy = dxs[d], dys[d]
        q = deque(); q.append((x + dx, y + dy, 5))
        v = set(); v.add((x + dx, y + dx))

        while q:
            now_x, now_y, now_c = q.popleft()
            cold_arr[now_x][now_y] += now_c

            if now_c > 1:
                if dy == 1:
                    if in_range(now_x - 1, now_y + 1):
                        if not wall_arr[now_x][now_y][0] and not wall_arr[now_x - 1][now_y + 1][1]:
                            if (now_x - 1, now_y + 1) not in v:
                                q.append((now_x - 1, now_y + 1, now_c - 1))
                                v.add((now_x - 1, now_y + 1))
                    if in_range(now_x, now_y + 1):
                        if not wall_arr[now_x][now_y + 1][1]:
                            if (now_x, now_y + 1) not in v:
                                q.append((now_x, now_y + 1, now_c - 1))
                                v.add((now_x, now_y + 1))
                    if in_range(now_x + 1, now_y + 1):
                        if not wall_arr[now_x + 1][now_y][0] and not wall_arr[now_x + 1][now_y + 1][1]:
                            if (now_x + 1, now_y + 1) not in v:
                                q.append((now_x + 1, now_y + 1, now_c - 1))
                                v.add((now_x + 1, now_y + 1))

                elif dy == -1:
                    if in_range(now_x - 1, now_y - 1):
                        if not wall_arr[now_x][now_y][0] and not wall_arr[now_x - 1][now_y][1]:
                            if (now_x - 1, now_y - 1) not in v:
                                q.append((now_x - 1, now_y - 1, now_c - 1))
                                v.add((now_x - 1, now_y - 1))
                    if in_range(now_x, now_y - 1):
                        if not wall_arr[now_x][now_y][1]:
                            if (now_x, now_y - 1) not in v:
                                q.append((now_x, now_y - 1, now_c - 1))
                                v.add((now_x, now_y - 1))
                    if in_range(now_x + 1, now_y - 1):
                        if not wall_arr[now_x + 1][now_y][0] and not wall_arr[now_x + 1][now_y][1]:
                            if (now_x + 1, now_y - 1) not in v:
                                q.append((now_x + 1, now_y - 1, now_c - 1))
                                v.add((now_x + 1, now_y - 1))

                elif dx == 1:
                    if in_range(now_x + 1, now_y - 1):
                        if not wall_arr[now_x][now_y][1] and not wall_arr[now_x + 1][now_y - 1][0]:
                            if (now_x + 1, now_y - 1) not in v:
                                q.append((now_x + 1, now_y - 1, now_c - 1))
                                v.add((now_x + 1, now_y - 1))
                    if in_range(now_x + 1, now_y):
                        if not wall_arr[now_x + 1][now_y][0]:
                            if (now_x + 1, now_y) not in v:
                                q.append((now_x + 1, now_y, now_c - 1))
                                v.add((now_x + 1, now_y))
                    if in_range(now_x + 1, now_y + 1):
                        if not wall_arr[now_x][now_y + 1][1] and not wall_arr[now_x + 1][now_y + 1][0]:
                            if (now_x + 1, now_y + 1) not in v:
                                q.append((now_x + 1, now_y + 1, now_c - 1))
                                v.add((now_x + 1, now_y + 1))

                elif dx == -1:
                    if in_range(now_x - 1, now_y - 1):
                        if not wall_arr[now_x][now_y][1] and not wall_arr[now_x][now_y - 1][0]:
                            if (now_x - 1, now_y - 1) not in v:
                                q.append((now_x - 1, now_y - 1, now_c - 1))
                                v.add((now_x - 1, now_y - 1))
                    if in_range(now_x - 1, now_y):
                        if not wall_arr[now_x][now_y][0]:
                            if (now_x - 1, now_y) not in v:
                                q.append((now_x - 1, now_y, now_c - 1))
                                v.add((now_x - 1, now_y))
                    if in_range(now_x - 1, now_y + 1):
                        if not wall_arr[now_x][now_y + 1][1] and not wall_arr[now_x][now_y + 1][0]:
                            if (now_x - 1, now_y + 1) not in v:
                                q.append((now_x - 1, now_y + 1, now_c - 1))
                                v.add((now_x - 1, now_y + 1))

def mix_air():
    global cold_arr
    new_cold_arr = copy.deepcopy(cold_arr)

    for i in range(n):
        for j in range(n):
            if i != n - 1:
                if not wall_arr[i + 1][j][0]:
                    move_cold = abs(cold_arr[i + 1][j] - cold_arr[i][j]) // 4
                    if cold_arr[i + 1][j] > cold_arr[i][j]:
                        new_cold_arr[i + 1][j] -= move_cold
                        new_cold_arr[i][j] += move_cold
                    elif cold_arr[i + 1][j] < cold_arr[i][j]:
                        new_cold_arr[i + 1][j] += move_cold
                        new_cold_arr[i][j] -= move_cold

            if j != n - 1:
                if not wall_arr[i][j + 1][1]:
                    move_cold = abs(cold_arr[i][j + 1] - cold_arr[i][j]) // 4
                    if cold_arr[i][j + 1] > cold_arr[i][j]:
                        new_cold_arr[i][j + 1] -= move_cold
                        new_cold_arr[i][j] += move_cold
                    elif cold_arr[i][j + 1] < cold_arr[i][j]:
                        new_cold_arr[i][j + 1] += move_cold
                        new_cold_arr[i][j] -= move_cold

    cold_arr = new_cold_arr

def reduce_wall_cold():
    for i in [0, n - 1]:
        for j in range(1, n - 1):
            if cold_arr[i][j]:
                cold_arr[i][j] -= 1

    for j in [0, n - 1]:
        for i in range(1, n - 1):
            if cold_arr[i][j]:
                cold_arr[i][j] -= 1

    cold_arr[0][0] -= 1
    cold_arr[0][n - 1] -= 1
    cold_arr[n - 1][0] -= 1
    cold_arr[n - 1][n - 1] -=1

def check_office():
    office_cold = [cold_arr[x][y] for x, y in office_list]
    return True if min(office_cold) >= k else False

time = 0
for time in range(1, 102):
    make_cold()
    mix_air()
    reduce_wall_cold()
    if check_office():
        break

if time > 100:
    print(-1)
else:
    print(time)