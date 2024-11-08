n, m, k = list(map(int, input().split()))
arr = [
    [[] for _ in range(m)]
    for _ in range(n)
]

mold_list = []
for _ in range(k):
    # 곰팡이의 위치 x, y (1~n), 거리 s, 방향 d(1~4 위아오왼), 크기 b
    x, y, s, d, b = list(map(int, input().split()))
    arr[x-1][y-1].append([s, d-1, b])
    mold_list.append((x-1, y-1))

x_list = [-1, 1, 0, 0]
y_list = [0, 0, 1, -1]
change_dir = {0: 1, 1: 0, 2: 3, 3: 2}

sum_size = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 1
for j in range(m):
    # 2
    for i in range(n):
        if len(arr[i][j]):
            sum_size += arr[i][j][0][2]
            mold_list.remove((i, j))
            arr[i][j] = []
            break

    # 3, 4
    new_arr = [
        [[] for _ in range(m)]
        for _ in range(n)
    ]

    new_mold_list = set()
    for x, y in mold_list:
        s, d, b = arr[x][y][0]
        for _ in range(s):
            new_x, new_y = x + x_list[d], y + y_list[d]
            if in_range(new_x, new_y):
                x, y = new_x, new_y
            else:
                d = change_dir[d]
                x, y = x + x_list[d], y + y_list[d]
        new_arr[x][y].append([s, d, b])
        new_mold_list.add((x, y))

    # 5
    for x in range(n):
        for y in range(m):
            if len(new_arr[x][y]) >= 2:
                sorted_arr = sorted(new_arr[x][y], key=lambda mold:mold[2], reverse=True)
                new_arr[x][y] = [sorted_arr[0]]

    arr = new_arr
    mold_list = list(new_mold_list)

print(sum_size)