arr = [
    [0] * 4
    for _ in range(4)
]

position = dict()
direction = dict()
dead = dict()

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, -1, -1, -1, 0, 1, 1, 1]

def deepcopy(old):
    if type(old) == list:
        new = [
            list(old[i]) for i in range(4)
        ]
        return new
    elif type(old) == dict:
        new = {i: list(old[i]) for i in old}
        return new

def in_range(a, b):
    return 0 <= a < 4 and 0 <= b < 4

for i in range(4):
    l = list(map(int, input().split()))
    for j in range(4):
        p, d = l[j * 2], l[j * 2 + 1] - 1
        arr[i][j] = p
        position[p] = [i, j]
        direction[p] = d
        dead[p] = False

tagger_x, tagger_y, tagger_d = 0, 0, 0
max_score = 0

def recursive(score):
    global position, direction, dead
    global arr, tagger_x, tagger_y, tagger_d, max_score

    before_i = arr[tagger_x][tagger_y]
    dead[before_i] = True
    tagger_d = direction[before_i]
    score += before_i
    arr[tagger_x][tagger_y] = -1

    # 도둑말
    for i in range(1, 17):
        if not dead[i]:
            now_x, now_y = position[i]
            now_d = direction[i]

            for now_d in range(now_d, now_d+8):
                now_d = now_d % 8
                new_x, new_y = now_x + dxs[now_d], now_y + dys[now_d]

                if in_range(new_x, new_y) and arr[new_x][new_y] != -1:
                    there_i = arr[new_x][new_y]
                    arr[new_x][new_y] = i
                    arr[now_x][now_y] = there_i

                    position[there_i] = [now_x, now_y]
                    position[i] = [new_x, new_y]
                    direction[i] = now_d
                    break

    # 술래말
    can_move = False
    for i in range(1, 4):
        new_x, new_y = tagger_x + dxs[tagger_d] * i, tagger_y + dys[tagger_d] * i
        if in_range(new_x, new_y):
            if arr[new_x][new_y] > 0:
                orig_arr = deepcopy(arr)
                arr[tagger_x][tagger_y] = 0
                orig_x, orig_y, orig_d = tagger_x, tagger_y, tagger_d
                orig_pos, orig_dir, orig_dead = deepcopy(position), direction.copy(), dead.copy()
                tagger_x, tagger_y = new_x, new_y

                recursive(score)

                position, direction, dead = orig_pos, orig_dir, orig_dead
                tagger_x, tagger_y, tagger_d = orig_x, orig_y, orig_d
                arr = orig_arr

                can_move = True
        else:
            break

    if not can_move:
        max_score = max(max_score, score)

recursive(0)

print(max_score)