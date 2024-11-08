from collections import deque

n, m = list(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
] # 0 빈 공간, 1 베이스캠프, -1 지나갈 수 없음

people_dest = [
    [x - 1 for x in list(map(int, input().split()))]
    for _ in range(m)
]

people_pos = [
    (-1, -1)
    for _ in range(m)
]

moved_num = 0

# ↑, ←, →, ↓
dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

def get_basecamp(idx):
    dest_x, dest_y = people_dest[idx]

    visited = [[False] * n for _ in range(n)]
    visited[dest_x][dest_y] = True

    q = deque()
    q.append((dest_x, dest_y, 0))

    min_c, min_x, min_y = float('inf'), n, n

    while q:
        qx, qy, qc = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = qx + dx, qy + dy

            if in_range(new_x, new_y) and not visited[new_x][new_y]:
                if arr[new_x][new_y] == 0:
                    q.append((new_x, new_y, qc + 1))
                elif arr[new_x][new_y] == 1:
                    min_c, min_x, min_y = min(
                        (min_c, min_x, min_y),
                        (qc + 1, new_x, new_y)
                    )

                visited[new_x][new_y] = True

    return min_x, min_y

def move_person(idx):
    global moved_num

    start_x, start_y = people_pos[idx]
    dest_x, dest_y = people_dest[idx]

    visited = [[False] * n for _ in range(n)]
    visited[start_x][start_y] = True

    q = deque()
    for dx, dy in zip(dxs, dys):
        new_x, new_y = start_x + dx, start_y + dy
        if in_range(new_x, new_y) and arr[new_x][new_y] != -1:
            q.append((new_x, new_y, new_x, new_y, 1))
            visited[new_x][new_y] = True

    while q:
        sx, sy, qx, qy, qc = q.popleft()
        if (qx, qy) == (dest_x, dest_y):
            if qc == 1:
                moved_num += 1
                people_pos[idx] = (-1, -1)
                return sx, sy
            else:
                people_pos[idx] = (sx, sy)
                return -1, -1

        for dx, dy in zip(dxs, dys):
            new_x, new_y = qx + dx, qy + dy

            if in_range(new_x, new_y) and arr[new_x][new_y] != -1 \
                    and not visited[new_x][new_y]:
                q.append((sx, sy, new_x, new_y, qc + 1))
                visited[new_x][new_y] = True

def move_people():
    cant_go = []
    for i in range(m):
        if people_pos[i][0] != -1:
            mx, my = move_person(i)
            if mx != -1:
                cant_go.append((mx, my))

    for cgx, cgy in cant_go:
        arr[cgx][cgy] = -1

t = 0
while True:
    t += 1

    # 1
    move_people()

    # 3
    if t <= m:
        tx, ty = get_basecamp(t-1)
        people_pos[t-1] = (tx, ty)
        arr[tx][ty] = -1

    if moved_num == m:
        break

print(t)