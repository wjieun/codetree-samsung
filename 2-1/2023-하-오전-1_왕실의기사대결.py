from collections import deque

L, N, Q = list(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(L)
] # 0 빈칸, 1 함정, 2 벽

def set_knight_arr():
    global knight_arr

    knight_arr = [
        [-1] * L
        for _ in range(L)
    ]

    for idx, (r, c, h, w, k) in enumerate(knight_list):
        if k > 0:
            for i in range(h):
                for j in range(w):
                    knight_arr[r + i][c + j] = idx

knight_list = []
knight_damage_list = []
for idx in range(N):
    r, c, h, w, k = list(map(int, input().split()))
    r, c = r - 1, c - 1
    knight_list.append([r, c, h, w, k])
    knight_damage_list.append(0)

knight_arr = None
set_knight_arr()

# 0~3 위오아왼
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

for _ in range(Q):
    init_i, d = list(map(int, input().split()))
    init_i = init_i - 1

    if knight_list[init_i][-1] <= 0:
        continue

    q = deque()
    q.append(init_i)

    can_move = True
    move_list = [init_i]

    while q:
        pi = q.popleft()
        pr, pc, ph, pw, pk = knight_list[pi]

        if d == 0 or d == 2: # 상하
            if d == 0:
                next_r = pr - 1
            else:
                next_r = pr + ph

            if not 0 <= next_r < L:
                can_move = False
                break

            for next_c in range(pc, pc + pw):
                ai = arr[next_r][next_c]
                ki = knight_arr[next_r][next_c]
                if ai == 2:
                    can_move = False
                    break
                if ki not in move_list and ki >= 0:
                    q.append(ki)
                    move_list.append(ki)

        else: # 좌우
            if d == 1:
                next_c = pc + pw
            else:
                next_c = pc - 1

            if not 0 <= next_c < L:
                can_move = False
                break

            for next_r in range(pr, pr + ph):
                ai = arr[next_r][next_c]
                ki = knight_arr[next_r][next_c]
                if ai == 2:
                    can_move = False
                    break
                if ki not in move_list and ki >= 0:
                    q.append(ki)
                    move_list.append(ki)

        if can_move == False:
            break

    if can_move:
        for mi in move_list:
            mr, mc, mh, mw, mk = knight_list[mi]
            mr += dxs[d]
            mc += dys[d]

            if mi != init_i:
                count = 0
                for x in range(mr, mr + mh):
                    for y in range(mc, mc + mw):
                        if arr[x][y] == 1:
                            count += 1

                mk -= count
                knight_damage_list[mi] += count

            knight_list[mi] = [mr, mc, mh, mw, mk]

        set_knight_arr()

damage_sum = 0
for i, (_, _, _, _, k) in enumerate(knight_list):
    if k > 0:
        damage_sum += knight_damage_list[i]

print(damage_sum)