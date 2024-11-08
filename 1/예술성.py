import copy
from queue import Queue

n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

x_list = [1, -1, 0, 0]
y_list = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def get_groups():
    all_set = set()
    group_set = []
    for i in range(n):
        for j in range(n):
            if (i, j) not in all_set:
                now_num = arr[i][j]

                q = Queue(); q.put((i, j))
                s = set(); s.add((i, j))
                all_set.add((i, j))

                while not q.empty():
                    now_i, now_j = q.get()
                    for d in range(4):
                        new_i, new_j = now_i + x_list[d], now_j + y_list[d]
                        if in_range(new_i, new_j):
                            if arr[new_i][new_j] == now_num and (new_i, new_j) not in s:
                                q.put((new_i, new_j))
                                s.add((new_i, new_j))
                                all_set.add((new_i, new_j))

                group_set.append(s)
    return group_set

def get_score(group1, group2):
    adjacent = 0
    for x, y in group1:
        for d in range(4):
            new_x, new_y = x + x_list[d], y + y_list[d]
            if (new_x, new_y) in group2:
                adjacent += 1

    group1_x, group1_y = list(group1)[0]
    group2_x, group2_y = list(group2)[0]
    group1_num = arr[group1_x][group1_y]
    group2_num = arr[group2_x][group2_y]

    score = (len(group1) + len(group2)) * group1_num * group2_num * adjacent
    return score

def rotate_square(x, y, new_arr):
    global n
    size = n // 2
    for i in range(size):
        for j in range(size):
            new_arr[x + j][y + size - 1 - i] = arr[x + i][y + j]

def rotate_cross(new_arr):
    global n
    for i in range(n):
        for j in range(n):
            if i == n // 2 or j == n // 2:
                new_arr[n - 1 - j][i] = arr[i][j]

def rotate():
    global arr, n
    new_arr = copy.deepcopy(arr)

    for i in range(0, n, n // 2 + 1):
        for j in range(0, n, n // 2 + 1):
            rotate_square(i, j, new_arr)

    rotate_cross(new_arr)

    arr = new_arr

all_score_sum = 0
for k in range(4):
    groups = get_groups()
    score_sum = 0
    for i in range(len(groups)):
        for j in range(i + 1, len(groups)):
            score = get_score(groups[i], groups[j])
            score_sum += score
    all_score_sum += score_sum

    if k == 3:
        break

    rotate()

print(all_score_sum)