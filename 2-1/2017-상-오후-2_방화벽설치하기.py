from collections import deque

n, m = list(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
] # 불 2, 방화벽 1, 빈칸 0

fires = []
blanks = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            fires.append((i, j))
        elif arr[i][j] == 0:
            blanks.append((i, j))

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(a, b):
    if 0 <= a < n and 0 <= b < m:
        return True
    return False

def get_fire():
    global selected
    fire_num = 0
    for s in selected:
        si, sj = blanks[s]
        arr[si][sj] = 1

    q = deque()
    q.extend(fires)
    visited = [[False] * m for _ in range(n)]

    while q:
        fi, fj = q.popleft()
        fire_num += 1

        for dx, dy in zip(dxs, dys):
            new_i, new_j = fi + dx, fj + dy
            if in_range(new_i, new_j) and not visited[new_i][new_j]:
                if arr[new_i][new_j] == 0:
                    visited[new_i][new_j] = True
                    q.append((new_i, new_j))

    for s in selected:
        si, sj = blanks[s]
        arr[si][sj] = 0

    return fire_num

selected = []
min_fire = float('inf')
def recursive(idx):
    global min_fire

    if len(selected) == 3:
        fire = get_fire()
        min_fire = min(fire, min_fire)
        return

    if idx >= len(blanks):
        return

    recursive(idx + 1)

    selected.append(idx)
    recursive(idx + 1)
    selected.pop()

recursive(0)
print(len(fires) + len(blanks) - 3 - min_fire)