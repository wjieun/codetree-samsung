from collections import deque

n, m, k = list(map(int, input().split()))

arr = [
    [0] * n
    for _ in range(n)
]

office = []
aircon = []

for i in range(n):
    now_list = list(map(int, input().split()))
    for j in range(n):
        if now_list[j] == 1:
            office.append((i, j))
        elif 2 <= now_list[j] <= 5:
            aircon.append((i, j, now_list[j] - 2))

# 좌상우하
dxs = [0, -1, 0, 1]
dys = [-1, 0, 1, 0]

up = [
    [False] * n
    for _ in range(n)
]

left = [
    [False] * n
    for _ in range(n)
]

for _ in range(m):
    x, y, s = list(map(int, input().split()))
    x, y = x - 1, y - 1
    if s == 0:
        up[x][y] = True
    elif s == 1:
        left[x][y] = True

def get_finish():
    return all(arr[x][y] >= k for x, y in office)

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

def outer_wall():
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                if arr[i][j]:
                    arr[i][j] -= 1

def get_cool():
    for x, y, d in aircon:
        if d % 2 == 0:  # 좌우
            if d == 0: move_d, check_d = -1, 0
            else: move_d, check_d = 1, 1

            if in_range(x, y + move_d) and not left[x][y + check_d]:
                q = deque()
                q.append((x, y + move_d, 5))

                visited = [[0] * n for _ in range(n)]
                visited[x][y + move_d] = 5
                arr[x][y + move_d] += 5

                while q:
                    qx, qy, qn = q.popleft()

                    if in_range(qx - 1, qy + move_d) and not up[qx][qy] and \
                            not left[qx - 1][qy + check_d] and not visited[qx - 1][qy + move_d]:
                        arr[qx - 1][qy + move_d] += qn - 1
                        visited[qx - 1][qy + move_d] = qn - 1
                        if qn > 2: q.append((qx - 1, qy + move_d, qn - 1))

                    if in_range(qx, qy + move_d) and \
                            not left[qx][qy + check_d] and not visited[qx][qy + move_d]:
                        arr[qx][qy + move_d] += qn - 1
                        visited[qx][qy + move_d] = qn - 1
                        if qn > 2: q.append((qx, qy + move_d, qn - 1))

                    if in_range(qx + 1, qy + move_d) and not up[qx + 1][qy] and \
                            not left[qx + 1][qy + check_d] and not visited[qx + 1][qy + move_d]:
                        arr[qx + 1][qy + move_d] += qn - 1
                        visited[qx + 1][qy + move_d] = qn - 1
                        if qn > 2: q.append((qx + 1, qy + move_d, qn - 1))

        else:  # 상하
            if d == 1: move_d, check_d = -1, 0
            else: move_d, check_d = 1, 1

            if in_range(x + move_d, y) and not up[x + check_d][y]:
                q = deque()
                q.append((x + move_d, y, 5))

                visited = [[0] * n for _ in range(n)]
                visited[x + move_d][y] = 5
                arr[x + move_d][y] += 5

                while q:
                    qx, qy, qn = q.popleft()

                    if in_range(qx + move_d, qy - 1) and not left[qx][qy] and \
                            not up[qx + check_d][qy - 1] and not visited[qx + move_d][qy - 1]:
                        arr[qx + move_d][qy - 1] += qn - 1
                        visited[qx + move_d][qy - 1] = qn - 1
                        if qn > 2: q.append((qx + move_d, qy - 1, qn - 1))

                    if in_range(qx + move_d, qy) and \
                            not up[qx + check_d][qy] and not visited[qx + move_d][qy]:
                        arr[qx + move_d][qy] += qn - 1
                        visited[qx + move_d][qy] = qn - 1
                        if qn > 2: q.append((qx + move_d, qy, qn - 1))

                    if in_range(qx + move_d, qy + 1) and not left[qx][qy + 1] and \
                            not up[qx + check_d][qy + 1] and not visited[qx + move_d][qy + 1]:
                        arr[qx + move_d][qy + 1] += qn - 1
                        visited[qx + move_d][qy + 1] = qn - 1
                        if qn > 2: q.append((qx + move_d, qy + 1, qn - 1))

def mix_air():
    plus_arr = [
        [0] * n
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n-1):
            if not left[i][j + 1]:
                plus_num = abs(arr[i][j] - arr[i][j + 1]) // 4
                if arr[i][j] < arr[i][j + 1]:
                    plus_arr[i][j] += plus_num
                    plus_arr[i][j + 1] -= plus_num
                elif arr[i][j] > arr[i][j + 1]:
                    plus_arr[i][j] -= plus_num
                    plus_arr[i][j + 1] += plus_num

    for i in range(n-1):
        for j in range(n):
            if not up[i + 1][j]:
                plus_num = abs(arr[i][j] - arr[i + 1][j]) // 4
                if arr[i][j] < arr[i + 1][j]:
                    plus_arr[i][j] += plus_num
                    plus_arr[i + 1][j] -= plus_num
                elif arr[i][j] > arr[i + 1][j]:
                    plus_arr[i][j] -= plus_num
                    plus_arr[i + 1][j] += plus_num

    for i in range(n):
        for j in range(n):
            arr[i][j] += plus_arr[i][j]

minute = 0
for minute in range(1, 102):
    get_cool()  # 1
    mix_air()  # 2
    outer_wall()  # 3
    if get_finish():
        break

if minute == 101:
    print(-1)
else:
    print(minute)