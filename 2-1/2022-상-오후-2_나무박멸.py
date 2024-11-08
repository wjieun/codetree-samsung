from copy import deepcopy

n, m, k, c = list(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

herbicide = [
    [0] * n
    for _ in range(n)
]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

dxs2 = [1, 1, -1, -1]
dys2 = [1, -1, 1, -1]

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

all_tree = 0
for _ in range(m):
    # 1
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                for dx, dy in zip(dxs, dys):
                    new_i, new_j = i + dx, j + dy
                    if in_range(new_i, new_j) and arr[new_i][new_j] > 0:
                        arr[i][j] += 1

    # 2
    new_arr = deepcopy(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                counts = set()
                for dx, dy in zip(dxs, dys):
                    new_i, new_j = i + dx, j + dy
                    if in_range(new_i, new_j) and arr[new_i][new_j] == 0\
                            and herbicide[new_i][new_j] == 0:
                        counts.add((new_i, new_j))

                if counts:
                    tree_num = arr[i][j] // len(counts)
                    for ci, cj in counts:
                        new_arr[ci][cj] += tree_num

    arr = new_arr

    # 3
    max_tree, max_tree_list, min_row, min_col = 0, {}, n, n

    for i in range(n):
        for j in range(n):
            tree, tree_list = max(arr[i][j], 0), {(i, j)}
            if arr[i][j] > 0:
                for dx, dy in zip(dxs2, dys2):
                    now_x, now_y = i, j
                    for _ in range(k):
                        new_x, new_y = now_x + dx, now_y + dy
                        if in_range(new_x, new_y):
                            tree_list.add((new_x, new_y))
                            if arr[new_x][new_y] > 0:
                                tree += arr[new_x][new_y]
                                now_x, now_y = new_x, new_y
                            else:
                                break
                        else:
                            break

            change = False
            if tree > max_tree: change = True
            elif tree == max_tree:
                if i < min_row: change = True
                elif i == min_row:
                    if j < min_col: change = True

            if change:
                max_tree, max_tree_list, min_row, min_col = tree, tree_list, i, j

    # 4
    for i in range(n):
        for j in range(n):
            if herbicide[i][j] > 0:
                herbicide[i][j] -= 1

    for tx, ty in max_tree_list:
        herbicide[tx][ty] = c
        if arr[tx][ty] != -1:
            arr[tx][ty] = 0

    all_tree += max_tree

print(all_tree)