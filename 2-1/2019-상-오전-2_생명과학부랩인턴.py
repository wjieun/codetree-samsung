n, m, k = list(map(int, input().split()))

arr = [
    [[] for _ in range(m)]
    for _ in range(n)
]
for _ in range(k):
    x, y, s, d, b = list(map(int, input().split()))
    arr[x-1][y-1] = [s, d-1, b]

# 위아오왼
dxs = [-1, 1, 0, 0]
dys = [0, 0, 1, -1]

val = {0: 0, 1: n-1, 2: m-1, 3: 0}
max_val = {0: n-1, 1: n-1, 2: m-1, 3: m-1}
change_d = {0: 1, 1: 0, 2: 3, 3: 2}

catch_sum = 0
for j in range(m): # 1
    # 2
    for i in range(n):
        if arr[i][j]:
            catch_sum += arr[i][j][-1]
            arr[i][j] = []
            break

    # 3
    new_arr = [
        [[] for _ in range(m)]
        for _ in range(n)
    ]

    for init_x in range(n):
        for init_y in range(m):
            x, y = init_x, init_y
            if arr[x][y]:
                s, d, b = arr[x][y]
                init_s = s

                if d < 2: s = s % ((n-1) * 2)
                else: s = s % ((m-1) * 2)

                new_x, new_y = x, y
                if d < 2:
                    while s > abs(x - val[d]):
                        s -= abs(x - val[d])
                        x = val[d]
                        d = change_d[d]
                    new_x = x + s * dxs[d]
                else:
                    while s > abs(y - val[d]):
                        s -= abs(y - val[d])
                        y = val[d]
                        d = change_d[d]

                    new_y = y + s * dys[d]

                new_arr[new_x][new_y].append([init_s, d, b])

    for x in range(n):
        for y in range(m):
            a_len = len(new_arr[x][y])
            if a_len >= 1:
                if a_len > 1:
                    new_arr[x][y].sort(key=lambda k: k[-1], reverse=True)
                new_arr[x][y] = new_arr[x][y][0]

    arr = new_arr

print(catch_sum)