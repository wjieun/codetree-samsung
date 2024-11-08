import copy
from collections import deque

K, M = list(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(5)
]

new_list = list(map(int, input().split()))

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5

def get_relic(a):
    v = set()
    for i in range(5):
        for j in range(5):
            if (i, j) not in v:
                number = a[i][j]
                new_relic = {(i, j)}
                q = deque(); q.append((i, j))

                while q:
                    x, y = q.popleft()
                    for dx, dy in zip(dxs, dys):
                        new_x, new_y = x + dx, y + dy
                        if in_range(new_x, new_y) and a[new_x][new_y] == number and (new_x, new_y) not in new_relic:
                            new_relic.add((new_x, new_y))
                            q.append((new_x, new_y))

                if len(new_relic) >= 3:
                    v = v.union(new_relic)
    return v

def rotate(x, y, a):
    x, y = x - 1, y - 1
    new_arr = copy.deepcopy(a)

    for i in range(3):
        for j in range(3):
            new_arr[x + j][y + 3 - 1 - i] = a[x + i][y + j]

    relics = get_relic(new_arr)

    return new_arr, relics

def compare(relics, rtt, r, c, max_relics, min_rotate, min_r, min_c):
    is_max = False

    if relics > max_relics:
        is_max = True
    elif relics == max_relics:
        if rtt < min_rotate:
            is_max = True
        elif rtt == min_rotate:
            if c < min_c:
                is_max = True
            elif c == min_c and r < min_r:
                is_max = True

    return is_max

idx = 0
for _ in range(K):
    score = 0

    max_relics, min_rotate, rotate_arr = {}, float('inf'), None
    min_r, min_c = float('inf'), float('inf')
    for i in range(1, 4):
        for j in range(1, 4):
            # 90
            rotated_arr, relics = rotate(i, j, arr)
            change = compare(len(relics), 90, i, j, len(max_relics), min_rotate, min_r, min_c)
            if change:
                max_relics, min_rotate, rotate_arr = relics, 90, rotated_arr
                min_r, min_c = i, j

            # 180
            rotated_arr, relics = rotate(i, j, rotated_arr)
            change = compare(len(relics), 180, i, j, len(max_relics), min_rotate, min_r, min_c)
            if change:
                max_relics, min_rotate, rotate_arr = relics, 180, rotated_arr
                min_r, min_c = i, j

            # 270
            rotated_arr, relics = rotate(i, j, rotated_arr)
            change = compare(len(relics), 270, i, j, len(max_relics), min_rotate, min_r, min_c)
            if change:
                max_relics, min_rotate, rotate_arr = relics, 270, rotated_arr
                min_r, min_c = i, j

    if len(max_relics) == 0:
        break
    else:
        arr = rotate_arr
        while len(max_relics):
            score += len(max_relics)
            sorted_relics = sorted(list(max_relics), key=lambda x:x[0], reverse=True)
            sorted_relics = sorted(sorted_relics, key=lambda x:x[1])
            for x, y in sorted_relics:
                arr[x][y] = new_list[idx]
                idx += 1

            max_relics = get_relic(arr)

        print(score, end=' ')