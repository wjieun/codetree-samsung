from queue import Queue

# 격자의 크기 n과 사람의 수 m
n, m = list(map(int, input().split()))

basecamp_list = []

for i in range(n):
    l = list(map(int, input().split()))
    for j in range(n):
        if l[j] == 1:
            basecamp_list.append((i, j))

can_go = [
    [True for _ in range(n)]
    for _ in range(n)
]

coord_list = [(-1, -1) for _ in range(m)]

store_list = [
    [x - 1 for x in list(map(int, input().split()))]
    for _ in range(m)
]

# ↑, ←, →, ↓
dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def get_min_path(s_x, s_y, e_x, e_y):
    q = Queue(); q.put((s_x, s_y, []))
    v = set(); v.add((s_x, s_y))

    while not q.empty():
        x, y, path = q.get()

        for i, (dx, dy) in enumerate(zip(dxs, dys)):
            new_x, new_y = x + dx, y + dy
            if in_range(new_x, new_y) and (new_x, new_y) not in v:
                if can_go[new_x][new_y]:
                    if (new_x, new_y) == (e_x, e_y):
                        return path + [i]
                    q.put((new_x, new_y, path + [i]))
                    v.add((new_x, new_y))

def move_people():
    global m, coord_list

    # 1
    cant_go_list = []
    for i in range(m):
        if coord_list[i] != (-1, -1):
            coord_x, coord_y = coord_list[i]
            store_x, store_y = store_list[i]
            move_d = get_min_path(coord_x, coord_y, store_x, store_y)[0]

            move_x, move_y = coord_x + dxs[move_d], coord_y + dys[move_d]
            if (move_x, move_y) == (store_x, store_y):
                coord_list[i] = (-1, -1)
                cant_go_list.append((store_x, store_y))
            else:
                coord_list[i] = (move_x, move_y)

    # 2
    for cant_x, cant_y in cant_go_list:
        can_go[cant_x][cant_y] = False

def get_basecamp(idx):
    global basecamp_list, store_list
    store_x, store_y = store_list[idx]
    paths = []

    for basecamp_x, basecamp_y in basecamp_list:
        if can_go[basecamp_x][basecamp_y]:
            path = get_min_path(basecamp_x, basecamp_y, store_x, store_y)
            if path:
                paths.append([len(path), basecamp_x, basecamp_y])

    paths.sort()
    return paths[0][1:]

time = 0
while True:
    move_people()

    if time < m:
        x, y = get_basecamp(time)
        coord_list[time] = (x, y)
        can_go[x][y] = False

    time += 1

    if all([coord == (-1, -1) for coord in coord_list]):
        break

print(time)