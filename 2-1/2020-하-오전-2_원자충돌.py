n, m, k = list(map(int, input().split()))

arr = [
    [[] for _ in range(n)]
    for _ in range(n)
]

# 0~7 ↑, ↗, →, ↘, ↓, ↙, ←, ↖
dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(m):
    x, y, m, s, d = list(map(int, input().split()))
    x, y = x - 1, y - 1

    arr[x][y].append([m, s, d])

for _ in range(k):
    # 1
    new_arr = [
        [[] for _ in range(n)]
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            for m, s, d in arr[i][j]:
                new_i, new_j = (i + dxs[d] * s) % n, (j + dys[d] * s) % n
                new_arr[new_i][new_j].append([m, s, d])

    # 2
    for i in range(n):
        for j in range(n):
            if len(new_arr[i][j]) >= 2:
                m_sum, s_sum, d_sum = 0, 0, set()
                for m, s, d in new_arr[i][j]:
                    m_sum += m
                    s_sum += s
                    d_sum.add(d % 2)

                new_m = m_sum // 5
                new_s = s_sum // len(new_arr[i][j])
                new_arr[i][j] = []

                if new_m > 0:
                    if len(d_sum) == 1:
                        new_ds = [0, 2, 4, 6]
                    else:
                        new_ds = [1, 3, 5, 7]

                    for new_d in new_ds:
                        new_arr[i][j].append([new_m, new_s, new_d])

    arr = new_arr

all_m_sum = 0
for i in range(n):
    for j in range(n):
        for m, _, _ in arr[i][j]:
            all_m_sum += m

print(all_m_sum)