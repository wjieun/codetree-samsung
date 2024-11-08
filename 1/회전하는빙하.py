from queue import Queue

n, q = list(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(2 ** n)
]
rotate_level_list = list(map(int, input().split()))

x_list = [1, -1, 0, 0]
y_list = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < 2 ** n and 0 <= y < 2 ** n

for level in rotate_level_list:
    new_arr = [
        [-1 for _ in range(2 ** n)]
        for _ in range(2 ** n)
    ]

    # 네모 나누기
    if level != 0:
        for x in range(0, 2 ** n - 1, 2 ** level):
            for y in range(0, 2 ** n - 1, 2 ** level):
                # 격자 나누기
                for r in range(0, 2 ** level, 2 ** (level - 1)):
                    for c in range(0, 2 ** level, 2 ** (level - 1)):
                        # 회전하기
                        for i in range(2 ** (level - 1)):
                            for j in range(2 ** (level - 1)):
                                new_arr[x + c + i][y + (2 ** level - 1 - r) - (2 ** (level - 1) - 1 - j)] = arr[x + r + i][y + c + j]

        arr = new_arr

    melt_list = []
    for i in range(2 ** n):
        for j in range(2 ** n):
            ice = 0
            for d in range(4):
                new_i, new_j = i + x_list[d], j + y_list[d]
                if in_range(new_i, new_j):
                    if arr[new_i][new_j] > 0:
                        ice += 1
            if ice < 3:
                melt_list.append((i, j))

    for x, y in melt_list:
        if arr[x][y]:
            arr[x][y] -= 1

ice_sum = sum([sum(ice) for ice in arr])
print(ice_sum)

max_ice = 0
for i in range(2 ** n):
    for j in range(2 ** n):
        if arr[i][j] > 0:
            q = Queue(); q.put((i, j))
            s = set(); s.add((i, j))

            while not q.empty():
                now_i, now_j = q.get()

                for d in range(4):
                    new_i, new_j = now_i + x_list[d], now_j + y_list[d]
                    if in_range(new_i, new_j):
                        if arr[new_i][new_j] > 0 and (new_i, new_j) not in s:
                            q.put((new_i, new_j))
                            s.add((new_i, new_j))

            max_ice = max(max_ice, len(s))
print(max_ice)