n, m = list(map(int, input().split()))

height = [
    list(map(int, input().split()))
    for _ in range(n)
]

nutrition = []
for i in range(n-2, n):
    for j in range(2):
        nutrition.append((i, j))

# d 1~8 → ↗ ↑ ↖ ← ↙ ↓ ↘
dxs = [0, -1, -1, -1, 0, 1, 1, 1]
dys = [1, 1, 0, -1, -1, -1, 0, 1]

def in_range(a, b):
    if 0 <= a < n and 0 <= b < n:
        return True
    return False

for _ in range(m):
    d, p = list(map(int, input().split()))
    d -= 1

    # 1
    temp_nutrition = []
    for ni, nj in nutrition:
        new_ni, new_nj = (ni + dxs[d]*p) % n, (nj + dys[d]*p) % n
        height[new_ni][new_nj] += 1
        temp_nutrition.append((new_ni, new_nj))

    # 2
    counts = []
    for ni, nj in temp_nutrition:
        count = 0
        for nd in range(1, 8, 2):
            new_ni, new_nj = ni + dxs[nd], nj + dys[nd]
            if in_range(new_ni, new_nj) and height[new_ni][new_nj]:
                count += 1
        counts.append((ni, nj, count))

    for ni, nj, count in counts:
        height[ni][nj] += count

    # 3
    new_nutrition = []
    for i in range(n):
        for j in range(n):
            if height[i][j] >= 2 and (i, j) not in temp_nutrition:
                height[i][j] -= 2
                new_nutrition.append((i, j))
    nutrition = new_nutrition

h_sum = [sum(h) for h in height]
print(sum(h_sum))