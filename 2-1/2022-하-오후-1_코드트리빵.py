from collections import deque

n, m = list(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
] # 0 빈 공간, 1 베이스캠프, -1 못 지나감

base = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            base.append((i, j))

store = []
for _ in range(m):
    store_x, store_y = list(map(int, input().split()))
    store.append((store_x-1, store_y-1))

people = [None] * m

# ↑, ←, →, ↓
dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

def get_basecamp(idx):
    min_dis, min_row, min_col = float('inf'), float('inf'), float('inf')
    sx, sy = store[idx-1]

    q = deque()
    q.append((sx, sy, 0))
    visited = [[False] * n for _ in range(n)]
    visited[sx][sy] = True

    while q:
        qi, qj, dis = q.popleft()

        if dis > min_dis:
            continue
        else:
            if arr[qi][qj] == 1:
                min_dis, min_row, min_col = min((min_dis, min_row, min_col), (dis, qi, qj))
                continue

        for dx, dy in zip(dxs, dys):
            new_x, new_y = qi + dx, qj + dy

            if in_range(new_x, new_y) and not visited[new_x][new_y]\
                    and arr[new_x][new_y] != -1:
                visited[new_x][new_y] = True
                q.append((new_x, new_y, dis + 1))

    return min_row, min_col

def all_move():
    arrived = []

    for i in range(m):
        if people[i]:
            px, py = people[i]

            q = deque()
            q.append((-1, -1, px, py))

            visited = [[False] * n for _ in range(n)]
            visited[px][py] = True

            while q:
                start_x, start_y, now_x, now_y = q.popleft()

                if (now_x, now_y) == store[i]:
                    if (start_x, start_y) == store[i]:
                        people[i] = None
                        arrived.append(i)
                    else:
                        people[i] = (start_x, start_y)
                    break

                for dx, dy in zip(dxs, dys):
                    new_x, new_y = now_x + dx, now_y + dy

                    if in_range(new_x, new_y) and not visited[new_x][new_y]\
                            and arr[new_x][new_y] != -1:
                        visited[new_x][new_y] = True
                        if (start_x, start_y) == (-1, -1):
                            q.append((new_x, new_y, new_x, new_y))
                        else:
                            q.append((start_x, start_y, new_x, new_y))

    return arrived

minute = 0
while True:
    minute += 1

    # 1
    arrived = all_move()

    # 2
    for arrived_idx in arrived:
        r, c = store[arrived_idx]
        arr[r][c] = -1

    # 3
    if minute <= m:
        r, c = get_basecamp(minute)
        people[minute - 1] = (r, c)
        arr[r][c] = -1

    if not any(people):
        break

print(minute)