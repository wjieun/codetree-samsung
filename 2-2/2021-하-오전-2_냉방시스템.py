from collections import deque

n, m, k = list(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
cold = [[0] * n for _ in range(n)]

AC = []
office = []

for i in range(n):
    for j in range(n):
        if 2 <= arr[i][j] <= 5:
            d = arr[i][j] - 2
            AC.append((i, j, d))
        elif arr[i][j] == 1:
            office.append((i, j))

# 왼위오아
dxs = [0, -1, 0, 1]
dys = [-1, 0, 1, 0]

up = [[False] * n for _ in range(n)]
left = [[False] * n for _ in range(n)]

for _ in range(m):
    x, y, s = list(map(int, input().split()))
    x, y = x - 1, y - 1

    if s == 0:
        up[x][y] = True
    else:
        left[x][y] = True

def check_wall(x1, y1, x2, y2, d):
    x_diff, y_diff = x1 - x2, y1 - y2

    if x_diff and y_diff:
        if d == 0 or d == 2:
            x_max = max(x1, x2)
            y_max = max(y1, y2)
            return up[x_max][y1] or left[x2][y_max]
        else:
            x_max = max(x1, x2)
            y_max = max(y1, y2)
            return left[x1][y_max] or up[x_max][y2]
    elif x_diff:
        x_max = max(x1, x2)
        return up[x_max][y1]
    elif y_diff:
        y_max = max(y1, y2)
        return left[x1][y_max]

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

def cooling(AC_x, AC_y, AC_d):
    new_x, new_y = AC_x + dxs[AC_d], AC_y + dys[AC_d]
    if not in_range(new_x, new_y) or check_wall(AC_x, AC_y, new_x, new_y, AC_d):
        return

    if AC_d == 0 or AC_d == 2: # 좌우
        x_start, x_end = -1, 2
        if AC_d == 0: y_start, y_end = -1, 0
        else: y_start, y_end = 1, 2
    else: # 상하
        y_start, y_end = -1, 2
        if AC_d == 1: x_start, x_end = -1, 0
        else: x_start, x_end = 1, 2

    visited = [[False] * n for _ in range(n)]

    q = deque()
    q.append((new_x, new_y, 5))

    while q:
        now_x, now_y, now_cold = q.popleft()
        cold[now_x][now_y] += now_cold

        if now_cold > 1:
            for dx in range(x_start, x_end):
                for dy in range(y_start, y_end):
                    new_x, new_y = now_x + dx, now_y + dy

                    if in_range(new_x, new_y) and not visited[new_x][new_y] \
                            and not check_wall(now_x, now_y, new_x, new_y, AC_d):
                        visited[new_x][new_y] = True
                        q.append((new_x, new_y, now_cold - 1))

def mix_air():
    plus_cold = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n-1):
            if not left[i][j + 1]:
                move_cold = abs(cold[i][j] - cold[i][j + 1]) // 4
                if cold[i][j] > cold[i][j + 1]:
                    plus_cold[i][j] -= move_cold
                    plus_cold[i][j + 1] += move_cold
                elif cold[i][j] < cold[i][j + 1]:
                    plus_cold[i][j] += move_cold
                    plus_cold[i][j + 1] -= move_cold

    for i in range(n-1):
        for j in range(n):
            if not up[i + 1][j]:
                move_cold = abs(cold[i][j] - cold[i + 1][j]) // 4
                if cold[i][j] > cold[i + 1][j]:
                    plus_cold[i][j] -= move_cold
                    plus_cold[i + 1][j] += move_cold
                elif cold[i][j] < cold[i + 1][j]:
                    plus_cold[i][j] += move_cold
                    plus_cold[i + 1][j] -= move_cold

    for i in range(n):
        for j in range(n):
            cold[i][j] += plus_cold[i][j]
            if (i == 0 or i == n - 1 or j == 0 or j == n - 1) \
                    and cold[i][j]:
                cold[i][j] -= 1

def get_break():
    return not any(cold[x][y] < k for x, y in office)

for minute in range(1, 102):
    # 1
    for i, j, d in AC:
        cooling(i, j, d)

    # 2, 3
    mix_air()

    if get_break():
        break

if minute == 101:
    print(-1)
else:
    print(minute)