from collections import deque

R, C, K = list(map(int, input().split()))

arr = [
    [-1] * C
    for _ in range(R)
]

final_d = dict()
final_center = dict()
score_sum = 0

# 0~3 북동남서
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def in_range(a, b):
    return -3 <= a < R and 0 <= b < C

def real_in_range(a, b):
    return 0 <= a < R and 0 <= b < C

def in_box(a, b):
    return 1 <= a < R

def get_score(idx):
    max_score = 0
    visited = {-1, idx}
    q = deque()
    q.append(idx)

    while q:
        qi = q.popleft()
        qx, qy = final_center[qi]
        qd = final_d[qi]

        max_score = max(max_score, qx + 1)
        exit_x, exit_y = qx + dxs[qd], qy + dys[qd]

        for dx, dy in zip(dxs, dys):
            new_x, new_y = exit_x + dx, exit_y + dy
            if real_in_range(new_x, new_y) and arr[new_x][new_y] not in visited:
                visited.add(arr[new_x][new_y])
                q.append(arr[new_x][new_y])

    return max_score + 1

def move(c, d, idx):
    global arr, score_sum
    x, y = -2, c

    while True:
        # 1
        can_move = True
        for dx, dy in zip([1, 2, 1], [-1, 0, 1]):
            new_x, new_y = x + dx, y + dy
            if not in_range(new_x, new_y) or\
                    (real_in_range(new_x, new_y) and arr[new_x][new_y] != -1):
                can_move = False
                break

        if can_move:
            x += 1
            continue

        # 2
        can_move = True
        for dx, dy in zip([-1, 0, 1, 1, 2], [-1, -2, -1, -2, -1]):
            new_x, new_y = x + dx, y + dy
            if not in_range(new_x, new_y) or \
                    (real_in_range(new_x, new_y) and arr[new_x][new_y] != -1):
                can_move = False
                break

        if can_move:
            x += 1
            y -= 1
            d = (d - 1) % 4
            continue

        # 3
        can_move = True
        for dx, dy in zip([-1, 0, 1, 1, 2], [1, 2, 1, 2, 1]):
            new_x, new_y = x + dx, y + dy
            if not in_range(new_x, new_y) or \
                    (real_in_range(new_x, new_y) and arr[new_x][new_y] != -1):
                can_move = False
                break

        if can_move:
            x += 1
            y += 1
            d = (d + 1) % 4
            continue

        # fix
        if in_box(x, y):
            for dx, dy in zip([0, -1, 0, 1, 0], [0, 0, -1, 0, 1]):
                arr[x + dx][y + dy] = idx
            final_d[idx] = d
            final_center[idx] = (x, y)

            score = get_score(idx)
            score_sum += score
        else:
            arr = [
                [-1] * C
                for _ in range(R)
            ]

        break


for ss_idx in range(K):
    ci, di = list(map(int, input().split()))
    move(ci-1, di, ss_idx)

print(score_sum)