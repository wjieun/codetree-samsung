moves = list(map(int, input().split()))

map_arr = [
    [i for i in range(0, 40, 2)],
    [13, 16, 19],
    [22, 24],
    [28, 27, 26],
    [25, 30, 35],
    [40, 0, 0, 0, 0, 0, 0, 0]
]

pieces = [[0, 0] for _ in range(4)]
cont = {0: 5, 1: 4, 2: 4, 3: 4, 4: 5}
start = {(0, 5): 1, (0, 10): 2, (0, 15): 3}

def move_piece(idx, move_num):
    now_x, now_y = pieces[idx]

    if (now_x, now_y) in start:
        now_x, now_y = start[(now_x, now_y)], 0
        move_num -= 1

    while now_y + move_num >= len(map_arr[now_x]):
        move_num -= len(map_arr[now_x]) - now_y
        now_x, now_y = cont[now_x], 0

    now_y += move_num
    if [now_x, now_y] in pieces:
        return -1
    else:
        if map_arr[now_x][now_y] == 0:
            pieces[idx] = [-1, -1]
            return 0
        else:
            pieces[idx] = [now_x, now_y]
            return map_arr[now_x][now_y]

def get_pieces():
    new_pieces = []
    no_move = True
    for i in range(4):
        if pieces[i] != [0, 0]:
            new_pieces.append(i)
        elif no_move:
            new_pieces.append(i)
            no_move = False
    return new_pieces

max_score = 0
def recursive(score, count, m_list):
    global max_score

    if count == 10:
        max_score = max(max_score, score)
        return

    for i in get_pieces():
        if pieces[i] != [-1, -1]:
            origin_pos = pieces[i].copy()
            new_score = move_piece(i, moves[count])

            if new_score != -1:
                recursive(score + new_score, count + 1, m_list + [i])
                pieces[i] = origin_pos

recursive(0, 0, [])
print(max_score)