import copy

N, M = list(map(int, input().split()))

map_arr = [
    [0 for _ in range(M)]
    for _ in range(N)
]
map_dict = {'.': 0, '#': 1, 'B': 2, 'R': 3, 'O': -1}

rr, rc, br, bc = -1, -1, -1, -1
for i in range(N):
    input_list = list(input())
    for j in range(M):
        map_arr[i][j] = map_dict[input_list[j]]
        if map_arr[i][j] == 2: br, bc = i, j
        elif map_arr[i][j] == 3: rr, rc = i, j

# 상좌하우
dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

def move_red(move_d):
    global rr, rc, map_arr
    now_x, now_y = rr, rc
    map_arr[rr][rc] = 0
    while True:
        new_x, new_y = now_x + dxs[move_d], now_y + dys[move_d]
        if map_arr[new_x][new_y] == 0:
            now_x, now_y = new_x, new_y
        elif map_arr[new_x][new_y] == -1:
            now_x, now_y = -1, -1
            break
        else:
            break
    rr, rc = now_x, now_y
    if (rr, rc) != (-1, -1):
        map_arr[rr][rc] = 3

def move_blue(move_d):
    global br, bc, map_arr
    now_x, now_y = br, bc
    map_arr[br][bc] = 0
    while True:
        new_x, new_y = now_x + dxs[move_d], now_y + dys[move_d]
        if map_arr[new_x][new_y] == 0:
            now_x, now_y = new_x, new_y
        elif map_arr[new_x][new_y] == -1:
            now_x, now_y = -1, -1
            break
        else:
            break
    br, bc = now_x, now_y
    if (br, bc) != (-1, -1):
        map_arr[br][bc] = 2

def move_candy(move_d):
    if (move_d == 0 and rr < br) or (move_d == 2 and rr > br)\
            or (move_d == 1 and rc < bc) or (move_d == 3 and rc > bc):
        move_red(move_d)
        move_blue(move_d)
    else:
        move_blue(move_d)
        move_red(move_d)

selected = []
min_cnt = float('inf')
def recur(d, cnt):
    global map_arr, min_cnt, rr, rc, br, bc

    if cnt == 11:
        return

    if (br, bc) == (-1, -1):
        return
    elif (rr, rc) == (-1, -1):
        min_cnt = min(min_cnt, cnt)
        return

    for i in range(4):
        if i != d and (d == -1 or i != (d + 2) % 4):
            origin_map = copy.deepcopy(map_arr)
            origin_coord = rr, rc, br, bc
            selected.append(i)

            move_candy(i)
            recur(i, cnt + 1)

            map_arr = origin_map
            rr, rc, br, bc = origin_coord
            selected.pop()

recur(-1, 0)
if min_cnt == float('inf'):
    print(-1)
else:
    print(min_cnt)