import copy

L, N, Q = list(map(int, input().split()))
chess_arr = [
    list(map(int, input().split()))
    for _ in range(L)
]
knight_arr = [
    [-1 for _ in range(L)]
    for _ in range(L)
]
knight_dict = dict()

for n in range(N):
    r, c, h, w, k = list(map(int, input().split()))
    r, c = r - 1, c - 1
    knight_dict[n] = [r, c, h, w, k]
    for i in range(r, r + h):
        for j in range(c, c + w):
            knight_arr[i][j] = [n, h, w, k]

first_dict = copy.deepcopy(knight_dict)

def make_knight_arr(push_list):
    global knight_arr

    new_knight_arr = [
        [-1 for _ in range(L)]
        for _ in range(L)
    ]

    remove_list = []
    for n in knight_dict.keys():
        r, c, h, w, k = knight_dict[n]

        trap_sum = 0
        if n in push_list:
            for i in range(r, r + h):
                for j in range(c, c + w):
                    if chess_arr[i][j] == 1:
                        trap_sum += 1

        k -= trap_sum
        if k > 0:
            for i in range(r, r + h):
                for j in range(c, c + w):
                    new_knight_arr[i][j] = [n, h, w, k]
            knight_dict[n][-1] = k
        else:
            remove_list.append(n)

    for remove_num in remove_list:
        del knight_dict[remove_num]

    knight_arr = new_knight_arr

def in_range(x, y):
    return 0 <= x < L and 0 <= y < L

x_list = [-1, 0, 1, 0]
y_list = [0, 1, 0, -1]

def find_push(knight_i, knight_d):
    can_push = True
    push_list = []
    x, y, h, w, k = knight_dict[knight_i]
    start_x, end_x, step_x, start_y, end_y, step_y = -1, -1, -1, -1, -1, -1

    if knight_d in [0, 2]:
        start_y = y; end_y = y + w; step_y = 1
        if knight_d == 0:
            start_x = x - 1; end_x = start_x - 1; step_x = -1
        elif knight_d == 2:
            start_x = x + h; end_x = start_x + 1; step_x = 1
    elif knight_d in [1, 3]:
        start_x = x; end_x = x + h; step_x = 1
        if knight_d == 3:
            start_y = y - 1; end_y = start_y - 1; step_y = -1
        elif knight_d == 1:
            start_y = y + w; end_y = start_y + 1; step_y = 1

    for i in range(start_x, end_x, step_x):
        for j in range(start_y, end_y, step_y):
            if in_range(i, j):
                if chess_arr[i][j] == 2:
                    can_push = False
                    break
                if knight_arr[i][j] != -1:
                    new_knight_i = knight_arr[i][j][0]
                    if new_knight_i not in push_list:
                        push_list.append(new_knight_i)
            else:
                can_push = False
                break
        if not can_push:
            break

    if can_push:
        for push in push_list:
            can_push, new_push_list = find_push(push, knight_d)
            push_list.extend(new_push_list)

            if not can_push:
                break

    return can_push, list(set(push_list))

for _ in range(Q):
    i, d = list(map(int, input().split()))
    i = i - 1

    if i in knight_dict:
        can_p, new_p_list = find_push(i, d)
        if can_p:
            p_list = [i]
            p_list.extend(new_p_list)
            for p in p_list:
                knight_dict[p][0] += x_list[d]
                knight_dict[p][1] += y_list[d]

            make_knight_arr(p_list[1:])

damage_sum = 0
for knight_num in knight_dict:
    now_k = knight_dict[knight_num][-1]
    first_k = first_dict[knight_num][-1]
    damage_sum += first_k - now_k
print(damage_sum)