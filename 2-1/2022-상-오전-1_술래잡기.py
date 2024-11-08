n, m, h, k = list(map(int, input().split()))
tagger_x, tagger_y = n // 2, n // 2

peoples = []
trees = [[False] * n for _ in range(n)]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
tagger_d = 3

for _ in range(m):
    x, y, d = list(map(int, input().split()))
    if d == 1:
        peoples.append([x-1, y-1, 0])
    elif d == 2:
        peoples.append([x - 1, y - 1, 1])

for _ in range(h):
    x, y = list(map(int, input().split()))
    trees[x-1][y-1] = True

move_dir, move_num, move_count = 1, 0, 0
moves = []
for i in range(1, n):
    moves.append(i)
    moves.append(i)
moves.append(n-1)

def distance(a, b):
    return abs(tagger_x - a) + abs(tagger_y - b)

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

score = 0
for turn in range(1, k+1):
    # 도망자
    for pi, (px, py, pd) in enumerate(peoples):
        if distance(px, py) <= 3:
            new_x, new_y = px + dxs[pd], py + dys[pd]
            if in_range(new_x, new_y):
                if (new_x, new_y) != (tagger_x, tagger_y):
                    peoples[pi][0], peoples[pi][1] = new_x, new_y
            else:
                pd = (pd + 2) % 4
                new_x, new_y = px + dxs[pd], py + dys[pd]
                if (new_x, new_y) != (tagger_x, tagger_y):
                    peoples[pi] = [new_x, new_y, pd]

    # 술래
    tagger_x, tagger_y = tagger_x + dxs[tagger_d], tagger_y + dys[tagger_d]
    move_count += 1

    if (move_dir == 1 and move_count == moves[move_num])\
            or (move_dir == -1 and move_count == moves[len(moves) - 1 - move_num]):
        tagger_d = (tagger_d + move_dir) % 4
        move_count = 0
        move_num += 1

        if move_num == len(moves):
            tagger_d = (tagger_d + move_dir) % 4
            move_num = 0
            move_dir = -move_dir

    deleted_sum = 0
    for i in range(3):
        new_x, new_y = tagger_x + dxs[tagger_d] * i, tagger_y + dys[tagger_d] * i
        if not in_range(new_x, new_y):
            break

        deleted = []
        for pi, (px, py, _) in enumerate(peoples):
            if (new_x, new_y) == (px, py) and not trees[px][py]:
                deleted.append(pi)

        for idx, pi in enumerate(sorted(deleted)):
            peoples.pop(pi - idx)
        deleted_sum += len(deleted)

    score += turn * deleted_sum

print(score)