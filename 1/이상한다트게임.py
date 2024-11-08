n, m, q = list(map(int, input().split()))
board_arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
rotate_arr = [
    list(map(int, input().split()))
    for _ in range(q)
] # 원판 x, 방향 d (시계 0 반시계 1), 칸 k

def rotate_board(board_i, board_d, board_k):
    global m

    board_list = board_arr[board_i]
    new_board_list = [-1 for _ in range(m)]

    if board_d == 0: # 시계
        for j in range(m):
            new_j = (j + board_k) % m
            new_board_list[new_j] = board_list[j]
    elif board_d == 1: # 반시계
        for j in range(m):
            new_j = (j - board_k) % m
            new_board_list[new_j] = board_list[j]

    board_arr[board_i] = new_board_list

for x, d, k in rotate_arr:
    for i in range(x - 1, n, x):
        rotate_board(i, d, k)

    to_delete = set()
    for i in range(n):
        for j in range(m):
            j1, j2 = (j - 1) % m, (j + 1) % m
            if board_arr[i][j] == board_arr[i][j1] != 0:
                to_delete.add((i, j))
                to_delete.add((i, j1))
            elif board_arr[i][j] == board_arr[i][j2] != 0:
                to_delete.add((i, j))
                to_delete.add((i, j2))

    for j in range(m):
        for i in range(n):
            i1, i2 = i - 1, i + 1
            if 0 <= i1 < n:
                if board_arr[i][j] == board_arr[i1][j] != 0:
                    to_delete.add((i1, j))
                    to_delete.add((i, j))
            elif 0 <= i2 < n:
                if board_arr[i][j] == board_arr[i2][j] != 0:
                    to_delete.add((i2, j))
                    to_delete.add((i, j))

    if len(to_delete):
        for i, j in to_delete:
            board_arr[i][j] = 0
    else:
        sum_all, cnt_all = 0, 0
        for i in range(n):
            for j in range(m):
                if board_arr[i][j]:
                    sum_all += board_arr[i][j]
                    cnt_all += 1

        if cnt_all:
            avg = sum_all // cnt_all
            for i in range(n):
                for j in range(m):
                    if board_arr[i][j]:
                        if board_arr[i][j] > avg:
                            board_arr[i][j] -= 1
                        elif board_arr[i][j] < avg:
                            board_arr[i][j] += 1

board_sum = sum([sum(b) for b in board_arr])
print(board_sum)