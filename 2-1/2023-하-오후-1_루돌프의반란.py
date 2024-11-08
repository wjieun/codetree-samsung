N, M, P, C, D = list(map(int, input().split()))
Rr, Rc = list(map(int, input().split()))
Rr, Rc = Rr - 1, Rc - 1

arr = [
    [0] * N
    for _ in range(N)
]
arr[Rr][Rc] = -1

S_list = dict()
S_dead = dict()
S_faint = dict()
S_score = dict()

for _ in range(P):
    Pn, Sr, Sc = list(map(int, input().split()))
    Sr, Sc = Sr - 1, Sc - 1
    arr[Sr][Sc] = Pn
    S_list[Pn] = [Sr, Sc]
    S_dead[Pn] = False
    S_faint[Pn] = -5
    S_score[Pn] = 0

# 상우하좌
dxs = [-1, 0, 1, 0, 1, 1, -1, -1]
dys = [0, 1, 0, -1, 1, -1, 1, -1]

def in_range(a, b):
    return 0 <= a < N and 0 <= b < N

def get_distance(r1, c1, r2, c2):
    return (r1 - r2) ** 2 + (c1 - c2) ** 2

def move_rudolph():
    global Rr, Rc

    # select
    min_dis, max_r, max_c = float('inf'), -1, -1
    for i in range(1, P+1):
        if not S_dead[i]:
            Sr, Sc = S_list[i]
            dis = get_distance(Rr, Rc, Sr, Sc)

            if min_dis > dis:
                min_dis, max_r, max_c = dis, Sr, Sc
            elif min_dis == dis:
                max_r, max_c = max((max_r, max_c), (Sr, Sc))

    # move
    min_dis, min_x, min_y = float('inf'), -1, -1
    for dx, dy in zip(dxs, dys):
        new_x, new_y = Rr + dx, Rc + dy
        if in_range(new_x, new_y):
            dis = get_distance(max_r, max_c, new_x, new_y)
            if min_dis > dis:
                min_dis, min_x, min_y = dis, new_x, new_y

    # crash
    if arr[min_x][min_y] > 0:
        crash(C, min_x-Rr, min_y-Rc, min_x, min_y, arr[min_x][min_y])

    arr[Rr][Rc] = 0
    Rr, Rc = min_x, min_y
    arr[Rr][Rc] = -1


def move_santas():
    for i in range(1, P + 1):
        if not S_dead[i] and S_faint[i] < turn - 1:
            now_x, now_y = S_list[i]
            min_dis, min_x, min_y = get_distance(Rr, Rc, now_x, now_y), -1, -1

            for dx, dy in zip(dxs[:4], dys[:4]):
                new_x, new_y = now_x + dx, now_y + dy
                if in_range(new_x, new_y) and arr[new_x][new_y] <= 0:
                    dis = get_distance(Rr, Rc, new_x, new_y)
                    if min_dis > dis:
                        min_dis, min_x, min_y = dis, new_x, new_y

            if (min_x, min_y) != (-1, -1):
                arr[now_x][now_y] = 0
                if arr[min_x][min_y] == -1:
                    crash(D, now_x-min_x, now_y-min_y, min_x, min_y, i)
                else:
                    S_list[i] = [min_x, min_y]
                    arr[min_x][min_y] = i


def crash(move, mx, my, cx, cy, idx):
    # mx, my: 움직일 방향
    # cx, cy: 부딪힌 지점
    # idx: 산타 인덱스

    now_x, now_y, now_i = cx, cy, idx
    new_x, new_y = now_x + mx * move, now_y + my * move
    S_score[idx] += move
    S_faint[idx] = turn

    # 상호작용
    while True:
        if in_range(new_x, new_y):
            S_list[now_i] = [new_x, new_y]
            if arr[new_x][new_y] > 0:
                new_i = arr[new_x][new_y]
                arr[new_x][new_y] = now_i
                now_i = new_i

                new_x, new_y = new_x + mx, new_y + my
            else:
                arr[new_x][new_y] = now_i
                break
        else:
            S_dead[now_i] = True
            break

    return

turn = 0
for turn in range(1, M+1):
    # 2
    move_rudolph()
    if all(S_dead.values()):
        break

    # 3
    move_santas()
    if all(S_dead.values()):
        break

    # 7
    for i in S_list:
        if not S_dead[i]:
            S_score[i] += 1

for i in range(1, P + 1):
    print(S_score[i], end=' ')