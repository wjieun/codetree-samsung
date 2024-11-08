from collections import deque

n, m, c = list(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]  # 0 도로, 1 벽

car_x, car_y = [d-1 for d in list(map(int, input().split()))]
passengers = []
moved = []

for _ in range(m):
    psg = list(map(int, input().split()))
    psg = [p-1 for p in psg]
    passengers.append(psg)
    moved.append(False)

dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

def get_distance(x1, y1, x2, y2, md):
    if (x1, y1) == (x2, y2):
        return 0

    visited = {(x1, y1)}
    q = deque()
    q.append((x1, y1, 0))

    while q:
        now_x, now_y, dis = q.popleft()
        if dis > md:
            break

        for dx, dy in zip(dxs, dys):
            new_x, new_y = now_x + dx, now_y + dy

            if in_range(new_x, new_y) and (new_x, new_y) not in visited\
                    and not arr[new_x][new_y]:
                if (new_x, new_y) == (x2, y2):
                    return dis + 1

                visited.add((new_x, new_y))
                q.append((new_x, new_y, dis + 1))

    return float('inf')

def get_passenger():
    min_dis, min_row, min_col, min_idx = n*n+1, 0, 0, 0

    for pi, (sx, sy, _, _) in enumerate(passengers):
        if not moved[pi]:
            dis = get_distance(car_x, car_y, sx, sy, min_dis)
            min_dis, min_row, min_col, min_idx =\
                min((min_dis, min_row, min_col, min_idx), (dis, sx, sy, pi))

    if min_dis == n*n+1:
        return -1
    else:
        return min_dis, min_row, min_col, min_idx

for _ in range(m):
    p = get_passenger()

    if p == -1:
        break
    else:
        dis1, row, col, idx = p
        sx, sy, ex, ey = passengers[idx]
        dis2 = get_distance(sx, sy, ex, ey, float('inf'))

        if c >= dis1 + dis2:
            car_x, car_y = ex, ey
            c += dis2 - dis1
            moved[idx] = True
        else:
            break

if sum(moved) == m:
    print(c)
else:
    print(-1)