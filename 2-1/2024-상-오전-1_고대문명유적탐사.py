from collections import deque
from copy import deepcopy

K, M = list(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(5)
]
relics = list(map(int, input().split()))
relic_idx = 0

def in_range(a, b):
    if 0 <= a < 5 and 0 <= b < 5:
        return True
    return False

def rotate_right(mat, x, y):
    new_mat = deepcopy(mat)
    for i in range(3):
        for j in range(3):
            new_mat[x - 1 + j][y - 1 + 3 - 1 - i] = mat[x - 1 + i][y - 1 + j]
    return new_mat

def get_score(mat):
    visited = [[False] * 5 for _ in range(5)]
    score = 0

    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                visited[i][j] = True
                count = 1
                q = deque(); q.append((i, j))

                while q:
                    now_x, now_y = q.popleft()

                    for dx, dy in zip([0, 1, 0, -1], [1, 0, -1, 0]):
                        new_x, new_y = now_x + dx, now_y + dy
                        if in_range(new_x, new_y) and not visited[new_x][new_y]\
                                and mat[now_x][now_y] == mat[new_x][new_y]:
                            visited[new_x][new_y] = True
                            q.append((new_x, new_y))
                            count += 1

                if count >= 3:
                    score += count

    return score

def get_final_score(mat):
    global relic_idx

    score = 0

    while True:
        all_count = set()
        visited = [[False] * 5 for _ in range(5)]

        for i in range(5):
            for j in range(5):
                if not visited[i][j]:
                    visited[i][j] = True
                    count = {(i, j)}
                    q = deque(); q.append((i, j))

                    while q:
                        now_x, now_y = q.popleft()

                        for dx, dy in zip([0, 1, 0, -1], [1, 0, -1, 0]):
                            new_x, new_y = now_x + dx, now_y + dy
                            if in_range(new_x, new_y) and not visited[new_x][new_y] \
                                    and mat[now_x][now_y] == mat[new_x][new_y]:
                                visited[new_x][new_y] = True
                                q.append((new_x, new_y))
                                count.add((new_x, new_y))

                    if len(count) >= 3:
                        all_count.update(count)
                        score += len(count)

        if len(all_count):
            for sx, sy in sorted(all_count, key=lambda x: (x[1], 5 - x[0])):
                mat[sx][sy] = relics[relic_idx]
                relic_idx += 1
        else:
            break

    return score

max_score = 1
min_angle = 3
min_col = 5
min_row = 5
new_arr = None

for _ in range(K):
    for rx in range(1, 4):
        for ry in range(1, 4):
            rotated = arr
            for angle in range(3):
                rotated = rotate_right(rotated, rx, ry)
                score = get_score(rotated)

                change = False
                if score > max_score: change = True
                elif score == max_score:
                    if angle < min_angle: change = True
                    elif angle == min_angle:
                        if ry < min_col: change = True
                        elif ry == min_col:
                            if rx < min_row: change = True

                if change:
                    max_score, min_angle, min_col, min_row = score, angle, ry, rx
                    new_arr = rotated

    if new_arr:
        print(get_final_score(new_arr), end=' ')
        arr = new_arr
        new_arr = None
        max_score, min_angle, min_col, min_row = 1, 3, 5, 5
    else:
        break