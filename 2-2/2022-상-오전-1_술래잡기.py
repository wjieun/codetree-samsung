n, m, h, k = list(map(int, input().split()))

arr = [
    [[] for _ in range(n)]
    for _ in range(n)
]

tree_arr = [
    [False] * n
    for _ in range(n)
]

movements = []
for i in range(1, n):
    movements.extend([i, i])
movements.append(n-1)

movements_num = len(movements)
movements = movements + list(reversed(movements))
tagger_x, tagger_y = n // 2, n // 2
tagger_d, tagger_m, tagger_c = 3, 0, 0

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

people = dict()
for i in range(1, m + 1):
    x, y, d = list(map(int, input().split()))
    x, y = x - 1, y - 1
    arr[x][y].append(i)

    if d == 1:
        people[i] = (x, y, 0)
    elif d == 2:
        people[i] = (x, y, 1)

for _ in range(h):
    x, y = list(map(int, input().split()))
    tree_arr[x-1][y-1] = True

def get_distance(x, y):
    return abs(tagger_x - x) + abs(tagger_y - y)

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

def move_people():
    global arr

    new_arr = [
        [[] for _ in range(n)]
        for _ in range(n)
    ]

    for pi, (px, py, pd) in people.items():
        if get_distance(px, py) <= 3:
            new_x, new_y = px + dxs[pd], py + dys[pd]
            if not in_range(new_x, new_y):
                pd = (pd + 2) % 4
                new_x, new_y = px + dxs[pd], py + dys[pd]

            if (new_x, new_y) != (tagger_x, tagger_y):
                people[pi] = (new_x, new_y, pd)
                new_arr[new_x][new_y].append(pi)
            else:
                people[pi] = (px, py, pd)
                new_arr[px][py].append(pi)
        else:
            new_arr[px][py].append(pi)

    arr = new_arr

def move_tagger():
    global tagger_x, tagger_y, tagger_d, tagger_m, tagger_c

    tagger_x, tagger_y = tagger_x + dxs[tagger_d], tagger_y + dys[tagger_d]

    tagger_c += 1
    if movements[tagger_m] == tagger_c:
        tagger_m += 1
        tagger_c = 0

        if tagger_m == movements_num:
            tagger_d = (tagger_d + 2) % 4
        elif tagger_m < movements_num:
            tagger_d = (tagger_d + 1) % 4
        elif tagger_m == movements_num * 2:
            tagger_m = 0
            tagger_d = (tagger_d - 2) % 4
        else:
            tagger_d = (tagger_d - 1) % 4

score = 0
for t in range(1, k + 1):
    move_people()
    move_tagger()

    deleted_num = 0
    for i in range(3):
        new_tx, new_ty = tagger_x + dxs[tagger_d] * i, tagger_y + dys[tagger_d] * i

        if not in_range(new_tx, new_ty):
            break

        if not tree_arr[new_tx][new_ty]:
            for pi in arr[new_tx][new_ty]:
                del people[pi]
                deleted_num += 1

            arr[new_tx][new_ty] = []

    score += t * deleted_num

print(score)