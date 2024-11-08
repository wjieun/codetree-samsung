from queue import Queue

# 격자의 크기를 나타내는 n, 빨간색 이외의 서로 다른 폭탄의 종류를 나타내는 m
n, m = list(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
] # -1 검은색 돌, 0 빨간색 폭탄, 1이상 m이하의 숫자는 빨간색과는 다른 서로 다른 색의 폭탄

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

def initialize_visited():
    global visited
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def find_group(x, y):
    global arr, visited
    num = arr[x][y]

    q = Queue()
    q.put((x, y))
    group = [[], [(x, y)]]
    combined_group = [(x, y)]
    visited[x][y] = True

    while not q.empty():
        now_x, now_y = q.get()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = now_x + dx, now_y + dy
            if in_range(new_x, new_y):
                if arr[new_x][new_y] in [0, num] \
                        and (new_x, new_y) not in combined_group:
                    q.put((new_x, new_y))
                    combined_group.append((new_x, new_y))
                    if arr[new_x][new_y] == 0:
                        group[0].append((new_x, new_y))
                    else:
                        group[1].append((new_x, new_y))
                        visited[new_x][new_y] = True

    return group, len(combined_group)


def find_maxlen_groups():
    global arr, visited, n
    maxlen_groups = []
    max_len = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0 and not visited[i][j]:
                new_group, group_len = find_group(i, j)
                if group_len >= 2:
                    if group_len > max_len:
                        maxlen_groups = [new_group]
                        max_len = group_len
                    elif group_len == max_len:
                        maxlen_groups.append(new_group)

    initialize_visited()

    return maxlen_groups

def get_point(g):
    sort_c = sorted(g[1], key=lambda p:p[1])
    sort_r = sorted(sort_c, key=lambda p:p[0], reverse=True)
    return sort_r[0]

def gravity():
    global n, arr
    for j in range(n):
        i = n - 1; i2 = 0
        while i > 0:
            if arr[i][j] == -2:
                all_blank = True
                for i2 in range(i - 1, -2, -1):
                    if i2 == -1 or arr[i2][j] == -1:
                        arr[i2 + 1][j] = -2
                        break
                    if arr[i2][j] != -2:
                        all_blank = False
                    arr[i2 + 1][j] = arr[i2][j]
                if all_blank:
                    i = i2
                    continue
                i += 1
            i -= 1

def rotate():
    global n, arr
    new_arr = [
        [-3 for _ in range(n)]
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(n):
            new_arr[n - 1 - j][i] = arr[i][j]
    arr = new_arr

score_sum = 0
while True:
    groups = find_maxlen_groups()
    groups = sorted(groups, key=lambda g:len(g[0]))

    if not len(groups):
        break

    less_red_groups = []
    for group in groups:
        if len(group[0]) == len(groups[0][0]):
            less_red_groups.append(group)

    selected_group = None
    max_x, min_y = -1, float('inf')
    for group in less_red_groups:
        point_x, point_y = get_point(group)
        if (point_x > max_x) or (point_x == max_x and point_y < min_y):
            max_x, min_y = point_x, point_y
            selected_group = group

    score = 0
    for group in selected_group:
        for x, y in group:
            arr[x][y] = -2
            score += 1
    score_sum += score * score

    gravity()
    rotate()
    gravity()

print(score_sum)