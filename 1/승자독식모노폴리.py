# 격자의 크기 n, 플레이어의 수 m, 독점 계약 턴 수 k
import copy

n, m, k = list(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
monopoly_arr = [
    [[0, 0] for _ in range(n)]
    for _ in range(n)
]
people_dict = dict()
for i in range(n):
    for j in range(n):
        if arr[i][j] > 0:
            people_dict[arr[i][j]] = (i, j)
            monopoly_arr[i][j] = [arr[i][j], k]

# 위 아래 왼쪽 오른쪽
dir_list = list(map(int, input().split()))
dir_list = [d - 1 for d in dir_list]
dir_list.insert(0, -1)

x_list = [-1, 1, 0, 0]
y_list = [0, 0, -1, 1]

priority = dict()
for i in range(1, m + 1):
    priority_i = []
    for j in range(4):
        pr = list(map(int, input().split()))
        priority_i.append([p - 1 for p in pr])
    priority[i] = priority_i

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def check_monopoly(x, y):
    return monopoly_arr[x][y][0]

def reduce_turn():
    for i in range(n):
        for j in range(n):
            if monopoly_arr[i][j][1] > 0:
                monopoly_arr[i][j][1] -= 1
            elif monopoly_arr[i][j][1] == 0:
                monopoly_arr[i][j][0] = 0

dead_list = []
for turn in range(1, 1001):
    reduce_turn()

    new_coord = []
    add_monopoly = []
    for i in range(1, m + 1):
        if i not in dead_list:
            x, y = people_dict[i]
            now_d = dir_list[i]
            prior_dir = priority[i][now_d]

            move_list = []
            for d in range(4):
                new_x, new_y = x + x_list[d], y + y_list[d]
                if in_range(new_x, new_y):
                    mnpl = check_monopoly(new_x, new_y)
                    pr_d = prior_dir.index(d)
                    move_list.append([mnpl, pr_d, d, new_x, new_y])

            no_m_list = [mv for mv in move_list if mv[0] == 0]
            my_m_list = [mv for mv in move_list if mv[0] == i]
            move_x, move_y, move_d = -1, -1, -1
            if len(no_m_list):
                no_m_list = sorted(no_m_list, key=lambda mv:mv[1])
                move_d, move_x, move_y = no_m_list[0][-3:]
            else:
                my_m_list = sorted(my_m_list, key=lambda mv:mv[1])
                move_d, move_x, move_y = my_m_list[0][-3:]

            people_dict[i] = (move_x, move_y)
            dir_list[i] = move_d

            if (move_x, move_y) in new_coord:
                dead_list.append(i)
            else:
                new_coord.append((move_x, move_y))
                add_monopoly.append([i, move_x, move_y])

    for i, move_x, move_y in add_monopoly:
        monopoly_arr[move_x][move_y] = [i, k]

    if len(dead_list) == m - 1:
        break

if turn >= 1000:
    print(-1)
else:
    print(turn)