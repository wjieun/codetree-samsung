from collections import deque

n = 4
m, t = list(map(int, input().split()))
pr, pc = list(map(int, input().split()))
pr, pc = pr - 1, pc - 1

monster_arr = [
    [[] for _ in range(n)]
    for _ in range(n)
]

deadbody_arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
# 팩맨 우선순위: 상좌하우 0246
dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, -1, -1, -1, 0, 1, 1, 1]

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

for _ in range(m):
    r, c, d = list(map(int, input().split()))
    monster_arr[r-1][c-1].append(d-1)

def move_monsters():
    global monster_arr
    new_arr = [
        [[] for _ in range(n)]
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            for d in monster_arr[i][j]:
                can_move = False
                for new_d in range(d, d + 8):
                    new_d = new_d % 8
                    new_x, new_y = i + dxs[new_d], j + dys[new_d]
                    if in_range(new_x, new_y) and \
                            not deadbody_arr[new_x][new_y] \
                            and (new_x, new_y) != (pr, pc):
                        new_arr[new_x][new_y].append(new_d)
                        can_move = True
                        break

                if not can_move:
                    new_arr[i][j].append(d)

    monster_arr = new_arr

def move_packman():
    max_monster = -1
    max_movement = []

    q = deque()
    q.append(([], 0, pr, pc))

    while q:
        movement, monster_num, now_x, now_y = q.popleft()

        for d in range(0, 8, 2):
            new_x, new_y = now_x + dxs[d], now_y + dys[d]
            if in_range(new_x, new_y):
                new_monster_num = monster_num
                if (new_x, new_y) not in movement:
                    new_monster_num += len(monster_arr[new_x][new_y])

                if len(movement) == 2:
                    if new_monster_num > max_monster:
                        max_monster = new_monster_num
                        max_movement = movement + [(new_x, new_y)]
                else:
                    q.append((movement + [(new_x, new_y)], new_monster_num, new_x, new_y))

    return max_movement


for _ in range(t):
    # 1
    egg_arr = [
        [list(monster_arr[i][j]) for j in range(n)]
        for i in range(n)
    ]

    # 2
    move_monsters()

    # 3
    moves = move_packman()

    for pr, pc in moves:
        if monster_arr[pr][pc]:
            deadbody_arr[pr][pc] = 3
            monster_arr[pr][pc] = []

    # 4
    for i in range(n):
        for j in range(n):
            if deadbody_arr[i][j]:
                deadbody_arr[i][j] -= 1

    # 5
    for i in range(n):
        for j in range(n):
            if egg_arr[i][j]:
                monster_arr[i][j].extend(egg_arr[i][j])

monster_sum = 0
for i in range(n):
    for j in range(n):
        if monster_arr[i][j]:
            monster_sum += len(monster_arr[i][j])

print(monster_sum)