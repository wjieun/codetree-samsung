n = 4
m, t = list(map(int, input().split()))
pm_x, pm_y = [x - 1 for x in list(map(int, input().split()))]

monster_arr = [
    [[] for _ in range(n)]
    for _ in range(n)
]

body_arr = [
    [-10] * n
    for _ in range(n)
]

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, -1, -1, -1, 0, 1, 1, 1]

for _ in range(m):
    r, c, d = [x - 1 for x in list(map(int, input().split()))]
    monster_arr[r][c].append(d)

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

def move_monsters(now_turn):
    global monster_arr

    new_monster_arr = [
        [[] for _ in range(n)]
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            for d in monster_arr[i][j]:
                moved = False

                for new_d in range(d, d + 8):
                    new_d = new_d % 8
                    new_x, new_y = i + dxs[new_d], j + dys[new_d]

                    if in_range(new_x, new_y) and body_arr[new_x][new_y] + 2 < now_turn \
                            and (new_x, new_y) != (pm_x, pm_y):
                        new_monster_arr[new_x][new_y].append(new_d)
                        moved = True
                        break

                if not moved:
                    new_monster_arr[i][j].append(d)

    monster_arr = new_monster_arr

def recursive(now_x, now_y, move_list, monster_num):
    global max_monster_num, max_move_list

    if len(move_list) == 3:
        if max_monster_num < monster_num:
            max_monster_num = monster_num
            max_move_list = move_list
        return

    for d in range(0, 8, 2):
        new_x, new_y = now_x + dxs[d], now_y + dys[d]

        if in_range(new_x, new_y):
            new_monster_num = monster_num
            if (new_x, new_y) not in move_list:
                new_monster_num += len(monster_arr[new_x][new_y])

            recursive(new_x, new_y, move_list + [(new_x, new_y)], new_monster_num)

for turn in range(t):
    # 1
    egg_arr = [
        [list(ma) for ma in monster_arr[i]]
        for i in range(n)
    ]

    # 2
    move_monsters(turn)

    # 3
    max_monster_num, max_move_list = -1, []
    recursive(pm_x, pm_y, [], 0)

    for mx, my in max_move_list:
        if monster_arr[mx][my]:
            monster_arr[mx][my] = []
            body_arr[mx][my] = turn
        pm_x, pm_y = mx, my

    # 5
    for i in range(n):
        for j in range(n):
            monster_arr[i][j].extend(egg_arr[i][j])


m_sum = 0
for i in range(n):
    for j in range(n):
        m_sum += len(monster_arr[i][j])
print(m_sum)