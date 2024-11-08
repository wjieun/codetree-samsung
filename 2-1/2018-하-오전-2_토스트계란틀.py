from queue import Queue

n, L, R = list(map(int, input().split()))

eggs = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

def in_range(a, b):
    if 0 <= a < n and 0 <= b < n:
        return True
    return False

def get_contact():
    contact = {}
    for i in range(n):
        for j in range(n):
            now = []
            for dx, dy in zip(dxs, dys):
                new_i, new_j = i + dx, j + dy
                if in_range(new_i, new_j):
                    if L <= abs(eggs[i][j] - eggs[new_i][new_j]) <= R:
                        now.append((new_i, new_j))
            contact[(i, j)] = now
    return contact

def get_bunch(cont):
    visited = set()
    move = False

    for key in cont:
        if key not in visited:
            q = Queue(); q.put(key); visited.add(key)
            indices = set(); egg_sum = 0

            while not q.empty():
                now = q.get()
                indices.add(now)
                egg_sum += eggs[now[0]][now[1]]

                for k in cont[now]:
                    if k not in visited:
                        q.put(k)
                        visited.add(k)

            if len(indices) > 1:
                move = True
                new_egg = egg_sum // len(indices)
                for x, y in indices:
                    eggs[x][y] = new_egg

    return move

count = 0
while True:
    c = get_contact()
    m = get_bunch(c)
    if m:
        count += 1
    else:
        print(count)
        break