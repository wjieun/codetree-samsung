from collections import deque

N, M = list(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(N)
] # 0 바이러스, 1 벽, 2 병원

hospitals = []
virus = set()

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            hospitals.append((i, j))
        elif arr[i][j] == 0:
            virus.add((i, j))

def in_range(a, b):
    return 0 <= a < N and 0 <= b < N

def simulation():
    virus_set = virus.copy()

    q = deque()
    q.extend([(hospitals[s][0], hospitals[s][1], 0) for s in selected])
    visited = set(selected)

    while q:
        x, y, count = q.popleft()
        virus_set.discard((x, y))

        if len(virus_set) == 0:
            return count

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if in_range(new_x, new_y) and arr[new_x][new_y] != 1 \
                    and (new_x, new_y) not in visited:
                q.append((new_x, new_y, count + 1))
                visited.add((new_x, new_y))

    return -1

selected = deque()
min_count = float('inf')
def recursive(idx):
    global min_count

    if len(selected) == M:
        c = simulation()
        if c != -1:
            min_count = min(min_count, c)
        return

    if idx == len(hospitals):
        return

    recursive(idx + 1)

    selected.append(idx)
    recursive(idx + 1)
    selected.pop()

recursive(0)

if min_count == float('inf'):
    print(-1)
else:
    print(min_count)