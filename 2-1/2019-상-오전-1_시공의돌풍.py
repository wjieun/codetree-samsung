n, m, t = list(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

winds = []

for i in range(n):
    if arr[i][0] == -1:
        winds.append(i)

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(a, b):
    return 0 <= a < n and 0 <= b < m

for _ in range(t):
    # 1
    new_arr = [
        [0] * m
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                blow = set()
                for dx, dy in zip(dxs, dys):
                    new_i, new_j = i + dx, j + dy
                    if in_range(new_i, new_j) and arr[new_i][new_j] != -1:
                        blow.add((new_i, new_j))

                if len(blow) > 0:
                    blow_dust = arr[i][j] // 5

                    for bx, by in blow:
                        new_arr[bx][by] += blow_dust

                    arr[i][j] -= blow_dust * len(blow)

    for i in range(n):
        for j in range(m):
            if arr[i][j] != -1:
                arr[i][j] += new_arr[i][j]

    # 2
    # 윗칸: 반시계 (오위왼아)
    now_x, now_y = winds[0], 1
    now_dust = 0

    for d in range(4):
        d = (0 - d) % 4
        while True:
            new_x, new_y = now_x + dxs[d], now_y + dys[d]

            if in_range(new_x, new_y) and (new_x, new_y) != (winds[1], 0):
                temp = arr[now_x][now_y]
                arr[now_x][now_y] = now_dust
                now_dust = temp

                now_x, now_y = new_x, new_y
            else:
                break

    # 아랫칸: 시계 (오아왼위)
    now_x, now_y = winds[1], 1
    now_dust = 0

    for d in range(4):
        d = (0 + d) % 4
        while True:
            new_x, new_y = now_x + dxs[d], now_y + dys[d]

            if in_range(new_x, new_y) and (new_x, new_y) != (winds[0], 0):
                temp = arr[now_x][now_y]
                arr[now_x][now_y] = now_dust
                now_dust = temp

                now_x, now_y = new_x, new_y
            else:
                break

d_sum = [sum(d) for d in arr]
print(sum(d_sum) + 2)