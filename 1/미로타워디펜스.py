n, m = list(map(int, input().split()))
px, py = n // 2, n // 2

map_arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
map_list = []

dir_cnt = []
for i in range(1, n + 1):
    dir_cnt.extend([i, i])
dir_cnt.pop()

def arr_to_list():
    global map_arr, map_list, dir_cnt

    map_list = []

    d = 0
    cnt = [0 for _ in range(len(dir_cnt))]
    x, y = px, py

    for _ in range(n * n - 1):
        cd = change_d[d % 4]
        x, y = x + dxs[cd], y + dys[cd]
        map_list.append(map_arr[x][y])
        cnt[d] += 1
        if cnt[d] == dir_cnt[d]:
            d += 1

def list_to_arr():
    global map_arr, map_list, dir_cnt

    map_arr = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    d = 0
    cnt = [0 for _ in range(len(dir_cnt))]
    x, y = px, py

    for i in range(n * n - 1):
        cd = change_d[d % 4]
        x, y = x + dxs[cd], y + dys[cd]
        map_arr[x][y] = map_list[i]

        cnt[d] += 1
        if cnt[d] == dir_cnt[d]:
            d += 1


# 0번부터 3번까지 각각 → ↓ ← ↑
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
change_d = [2, 1, 0, 3]

arr_to_list()

def make_list_full(new_list):
    while len(new_list) < n * n - 1:
        new_list.append(0)

score = 0
def kill_monster(d, p):
    global map_list, score

    # 1
    for i in range(1, p + 1):
        x, y = px + dxs[d] * i, py + dys[d] * i
        score += map_arr[x][y]
        map_arr[x][y] = 0

    # 2
    arr_to_list()
    new_list = []
    for i in range(n * n - 1):
        if map_list[i]: new_list.append(map_list[i])
    make_list_full(new_list)

    map_list = new_list
    list_to_arr()

def delete_more_than_three():
    global map_list, score

    # 3
    last, same_cnt = -1, 0
    same_list, all_same_list = [], []

    while True:
        for i in range(n * n):
            if i < n * n - 1:
                if map_list[i] == last != 0:
                    same_cnt += 1
                    same_list.append(i)
                else:
                    if same_cnt >= 4:
                        all_same_list.extend(same_list)
                    same_cnt = 1
                    same_list = [i]
                    last = map_list[i]
            else:
                if same_cnt >= 4:
                    all_same_list.extend(same_list)

        if len(all_same_list):
            new_list = []
            for i in range(n * n - 1):
                if i not in all_same_list:
                    new_list.append(map_list[i])
                else:
                    score += map_list[i]
            make_list_full(new_list)

            map_list = new_list
            same_list, all_same_list = [], []
        else:
            break

    # 4
    new_list = []
    last, same_cnt = map_list[0], 0
    for i in range(n * n):
        if i < n * n - 1:
            if i != 0 and last == 0:
                break

            if map_list[i] == last:
                same_cnt += 1
            else:
                new_list.extend([same_cnt, last])
                same_cnt = 1
                last = map_list[i]
        else:
            new_list.extend([same_cnt, last])
    make_list_full(new_list)
    map_list = new_list[:n*n-1]
    list_to_arr()

for _ in range(m):
    # 공격 방향 d, 공격 칸 수 p
    d, p = list(map(int, input().split()))
    kill_monster(d, p)  # 1, 2
    delete_more_than_three()  # 3, 4
print(score)