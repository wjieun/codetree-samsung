n, m, k, c = list(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
tree_list = []
wall_list = []

for i in range(n):
    for j in range(n):
        if arr[i][j] > 0:
            tree_list.append((i, j))
        elif arr[i][j] == -1:
            wall_list.append((i, j))

x_list = [1, -1, 0, 0]
y_list = [0, 0, 1, -1]
killer_x_list = [1, 1, -1, -1]
killer_y_list = [1, -1, 1, -1]
sum_kill_num = 0

killer_arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def get_max_kill():
    max_kill_num = 0
    max_kill_coord = []

    for x, y in tree_list:
        now_kill_num = arr[x][y]
        for i in range(4):
            now_x, now_y = x, y
            for _ in range(k):
                new_x = now_x + killer_x_list[i]
                new_y = now_y + killer_y_list[i]

                if 0 <= new_x < n and 0 <= new_y < n:
                    if arr[new_x][new_y] > 0:
                        now_kill_num += arr[new_x][new_y]
                        now_x, now_y = new_x, new_y
                        continue
                break

        if max_kill_num < now_kill_num:
            max_kill_num = now_kill_num
            max_kill_coord = [(x, y)]
        elif max_kill_num == now_kill_num:
            max_kill_coord.append((x, y))

    if len(max_kill_coord) == 0:
        return 0, (0, 0)
    elif len(max_kill_coord) > 1:
        sorted_x_min = sorted(max_kill_coord, key=lambda x:x[0])
        x_min = []
        for coord in sorted_x_min:
            if coord[0] == sorted_x_min[0][0]:
                x_min.append(coord)
        sorted_y_min = sorted(x_min, key=lambda y:y[1])
        max_kill_coord = sorted_y_min

    return max_kill_num, max_kill_coord[0]

for _ in range(m):
    # 0
    for i in range(n):
        for j in range(n):
            if killer_arr[i][j]:
                killer_arr[i][j] -= 1

    # 1
    for tree_x, tree_y in tree_list:
        for i in range(4):
            new_x = tree_x + x_list[i]
            new_y = tree_y + y_list[i]

            if 0 <= new_x < n and 0 <= new_y < n and (new_x, new_y) in tree_list:
                arr[tree_x][tree_y] += 1

    # 2
    grow_arr = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    for tree_x, tree_y in tree_list:
        grow_list = []
        for i in range(4):
            new_x = tree_x + x_list[i]
            new_y = tree_y + y_list[i]

            if 0 <= new_x < n and 0 <= new_y < n:
                if arr[new_x][new_y] == 0 and not killer_arr[new_x][new_y]:
                    grow_list.append((new_x, new_y))

        if len(grow_list):
            grow_num = arr[tree_x][tree_y] // len(grow_list)
            for grow_x, grow_y in grow_list:
                grow_arr[grow_x][grow_y] += grow_num

    for i in range(n):
        for j in range(n):
            if not arr[i][j] and grow_arr[i][j]:
                tree_list.append((i, j))
            arr[i][j] += grow_arr[i][j]

    # 3
    kill_num, kill_coord = get_max_kill()
    sum_kill_num += kill_num

    kill_x, kill_y = kill_coord
    killer_arr[kill_x][kill_y] = c + 1
    arr[kill_x][kill_y] = 0
    if kill_coord in tree_list:
        tree_list.remove(kill_coord)

    for i in range(4):
        now_x, now_y = kill_x, kill_y
        for _ in range(k):
            new_x = now_x + killer_x_list[i]
            new_y = now_y + killer_y_list[i]

            if 0 <= new_x < n and 0 <= new_y < n:
                if arr[new_x][new_y] >= 0:
                    killer_arr[new_x][new_y] = c + 1
                    now_x, now_y = new_x, new_y

                    if arr[new_x][new_y] > 0:
                        arr[new_x][new_y] = 0
                        tree_list.remove((new_x, new_y))
                        continue
            break

print(sum_kill_num)