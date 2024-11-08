n, m, k = list(map(int, input().split()))

arr = [
    [5] * n
    for _ in range(n)
]

plus_arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

virus = [
    [[] for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    r, c, a = list(map(int, input().split()))
    virus[r-1][c-1].append(a)

dxs = [0, 1, 1, 1, 0, -1, -1, -1]
dys = [1, 1, -1, 0, -1, -1, 0, 1]

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

for _ in range(k):
    # 1
    for i in range(n):
        for j in range(n):
            new_virus = []
            dead = 0

            for v in sorted(virus[i][j]):
                if arr[i][j] >= v:
                    new_virus.append(v+1)
                    arr[i][j] -= v
                else: # 2
                    dead += v // 2

            virus[i][j] = new_virus
            arr[i][j] += dead

    # 3
    for i in range(n):
        for j in range(n):
            for v in virus[i][j]:
                if v % 5 == 0:
                    for dx, dy in zip(dxs, dys):
                        new_x, new_y = i + dx, j + dy
                        if in_range(new_x, new_y):
                            virus[new_x][new_y].append(1)

    # 4
    for i in range(n):
        for j in range(n):
            arr[i][j] += plus_arr[i][j]

virus_sum = 0
for i in range(n):
    for j in range(n):
        virus_sum += len(virus[i][j])
print(virus_sum)