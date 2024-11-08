n, m, h, k = tuple(map(int, input().split()))
it_x, it_y = n // 2, n // 2

map_arr = [
    [[] for _ in range(n)]
    for _ in range(n)
]

tree_arr = [
    [False for _ in range(n)]
    for _ in range(n)
]

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]
change_d = {0: 1, 1: 0, 2: 3, 3: 2}

for _ in range(m):
    x, y, d = tuple(map(int, input().split()))
    if d == 1: map_arr[x - 1][y - 1].append(2)
    elif d == 2: map_arr[x - 1][y - 1].append(0)

for _ in range(h):
    x, y = tuple(map(int, input().split()))
    tree_arr[x - 1][y - 1] = True

def calc_dis(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move_people():
    global it_x, it_y, map_arr
    new_arr = [
        [[] for _ in range(n)]
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            for d in map_arr[i][j]:
                if calc_dis(it_x, it_y, i, j) <= 3:
                    new_i, new_j = i + dxs[d], j + dys[d]
                    if in_range(new_i, new_j):
                        if not (new_i, new_j) == (it_x, it_y):
                            new_arr[new_i][new_j].append(d)
                            continue
                    else:
                        d = change_d[d]
                        new_i, new_j = i + dxs[d], j + dys[d]
                        if not (new_i, new_j) == (it_x, it_y):
                            new_arr[new_i][new_j].append(d)
                            continue
                new_arr[i][j].append(d)

    map_arr = new_arr

it_d = 0
it_d_cnt = []
for i in range(1, n):
    it_d_cnt.extend([i, i])
it_d_cnt.append(n - 1)
it_cnt = [0 for _ in range(len(it_d_cnt))]

it_d_list = [
    [1, 2, 0, 3],
    [0, 2, 1, 3]
]
d_idx = 0
def move_it():
    global it_x, it_y, it_d, it_cnt, d_idx

    now_d = it_d % len(it_d_cnt)
    d = it_d_list[d_idx][now_d % 4]

    if d_idx == 0:
        it_cnt[now_d] += 1
        if it_cnt[now_d] == it_d_cnt[now_d]:
            it_d += 1
        if it_cnt == it_d_cnt:
            it_cnt = [0 for _ in range(len(it_d_cnt))]
            d_idx = 1
    else:
        it_cnt[len(it_d_cnt) - 1 - now_d] += 1
        if it_cnt[len(it_d_cnt) - 1 - now_d] == it_d_cnt[len(it_d_cnt) - 1 - now_d]:
            it_d += 1
        if it_cnt == it_d_cnt:
            it_cnt = [0 for _ in range(len(it_d_cnt))]
            d_idx = 0

    it_x, it_y = it_x + dxs[d], it_y + dys[d]

turn = 1
score = 0
def catch():
    global it_x, it_y, it_d, turn, score

    now_d = it_d % len(it_d_cnt)
    d = it_d_list[d_idx][now_d % 4]

    for i in range(3):
        catch_x, catch_y = it_x + dxs[d] * i, it_y + dys[d] * i
        if in_range(catch_x, catch_y):
            if not tree_arr[catch_x][catch_y]:
                score += turn * len(map_arr[catch_x][catch_y])
                map_arr[catch_x][catch_y] = []
        else:
            break

while turn <= k:
    move_people()
    move_it()
    catch()
    turn += 1
print(score)