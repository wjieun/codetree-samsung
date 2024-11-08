import copy

n, m, t = list(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dust_coord = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == -1:
            dust_coord.append((i, j))

x_list = [0, -1, 0, 1]
y_list = [1, 0, -1, 0]
for _ in range(t):
    # 먼지 확산
    plus_arr = [
        [0 for _ in range(m)]
        for _ in range(n)
    ]

    for x in range(n):
        for y in range(m):
            if (x, y) not in dust_coord:
                new_dust = arr[x][y] // 5
                for i in range(4):
                    new_x = x + x_list[i]
                    new_y = y + y_list[i]
                    if 0 <= new_x < n and 0 <= new_y < m and (new_x, new_y) not in dust_coord:
                        plus_arr[new_x][new_y] += new_dust
                        plus_arr[x][y] -= new_dust

    for x in range(n):
        for y in range(m):
            if (x, y) not in dust_coord:
                arr[x][y] += plus_arr[x][y]

    # 시공의 돌풍
    new_arr = copy.deepcopy(arr)
    for d in range(len(dust_coord)):
        x, y = dust_coord[d]
        arr[x][y], new_arr[x][y] = 0, 0
        d_x, d_y = x, y

        four_dir = 0
        dir_list = [0, 1, 2, 3] if d == 0 else [0, 3, 2, 1]
        while True:
            direction = dir_list[four_dir]
            new_d_x = d_x + x_list[direction]
            new_d_y = d_y + y_list[direction]

            if new_d_x == x and new_d_y == y:
                break

            if 0 <= new_d_x < n and 0 <= new_d_y < m:
                new_arr[new_d_x][new_d_y] = arr[d_x][d_y]
                d_x, d_y = new_d_x, new_d_y
            else:
                four_dir += 1
    arr = new_arr

sum_dust = sum(sum(dust) for dust in arr)
print(sum_dust)