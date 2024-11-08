import copy

N, M, K = list(map(int, input().split()))
maze_arr = [
    list(map(int, input().split()))
    for _ in range(N)
]
people_arr = [
    [[] for _ in range(N)]
    for _ in range(N)
]

for i in range(M):
    r, c = list(map(int, input().split()))
    r, c = r - 1, c - 1
    people_arr[r][c].append(i)

exit_x, exit_y = list(map(int, input().split()))
exit = exit_x - 1, exit_y - 1

def calc_dis(x, y):
    return abs(x - exit[0]) + abs(y - exit[1])

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def get_min_square(x, y):
    x_diff = abs(x - exit[0])
    y_diff = abs(y - exit[1])
    square_size = max(x_diff, y_diff)

    r = max(x - square_size, exit[0] - square_size)
    c = max(y - square_size, exit[1] - square_size)
    r = 0 if r < 0 else r
    c = 0 if c < 0 else c

    return square_size + 1, r, c

x_list = [1, -1, 0, 0]
y_list = [0, 0, 1, -1]

move_sum = 0
for k in range(K):
    people_list = dict()
    for i in range(N):
        for j in range(N):
            for num in people_arr[i][j]:
                people_list[num] = (i, j)

    # move
    del_list = []
    for people_num in people_list:
        people_x, people_y = people_list[people_num]
        now_dis = calc_dis(people_x, people_y)

        dis_list = []
        for d in range(4):
            new_x, new_y = people_x + x_list[d], people_y + y_list[d]
            if in_range(new_x, new_y):
                if maze_arr[new_x][new_y] == 0:
                    is_updown = 1 if d in [0, 1] else 0
                    new_dis = calc_dis(new_x, new_y)
                    if new_dis < now_dis:
                        dis_list.append([new_dis, is_updown, new_x, new_y])

        if len(dis_list):
            sort_updown = sorted(dis_list, key=lambda d:d[1], reverse=True)
            sort_dis = sorted(sort_updown, key=lambda d:d[0])

            move_sum += 1
            move_x, move_y = sort_dis[0][-2:]
            people_arr[people_x][people_y].remove(people_num)
            if (move_x, move_y) == exit:
                del_list.append(people_num)
            else:
                people_arr[move_x][move_y].append(people_num)
                people_list[people_num] = (move_x, move_y)

    for del_num in del_list:
        del people_list[del_num]

    if len(people_list) == 0:
        break

    # rotate
    min_square_list = []
    for people_num in people_list:
        people_x, people_y = people_list[people_num]
        min_square_list.append(get_min_square(people_x, people_y))

    sort_c = sorted(min_square_list, key=lambda m:m[2])
    sort_r = sorted(sort_c, key=lambda m:m[1])
    sort_square = sorted(sort_r, key=lambda m:m[0])

    rotate_size, rotate_r, rotate_c = sort_square[0]
    new_maze_arr = copy.deepcopy(maze_arr)
    new_people_arr = copy.deepcopy(people_arr)

    change_exit = False
    for i in range(rotate_size):
        for j in range(rotate_size):
            new_people_arr[rotate_r + j][rotate_c + rotate_size - 1 - i] = people_arr[rotate_r + i][rotate_c + j]
            new_maze_arr[rotate_r + j][rotate_c + rotate_size - 1 - i] = maze_arr[rotate_r + i][rotate_c + j]
            if maze_arr[rotate_r + i][rotate_c + j]:
                new_maze_arr[rotate_r + j][rotate_c + rotate_size - 1 - i] -= 1

            if exit == (rotate_r + i, rotate_c + j) and not change_exit:
                exit = (rotate_r + j, rotate_c + rotate_size - 1 - i)
                change_exit = True

    maze_arr = new_maze_arr
    people_arr = new_people_arr

print(move_sum)
print(exit[0] + 1, exit[1] + 1)