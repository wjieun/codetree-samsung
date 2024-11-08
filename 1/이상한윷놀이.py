n, k = list(map(int, input().split()))
board_arr = [
    list(map(int, input().split()))
    for _ in range(n)
]  # 흰색 0, 빨간색 1, 파란색 2

token_list = []
token_arr = [
    [[] for _ in range(n)]
    for _ in range(n)
]

for i in range(k):
    x, y, d = list(map(int, input().split()))
    token_list.append([x - 1, y - 1, d - 1])
    token_arr[x - 1][y - 1].append([i, d - 1])

# 오른쪽 왼쪽 위쪽 아래쪽
x_list = [0, 0, -1, 1]
y_list = [1, -1, 0, 0]
change_dir = {0: 1, 1: 0, 2: 3, 3: 2}


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

turn = 0
while True:
    turn += 1
    if turn > 1000:
        break
    break_while = False

    for token_num in range(len(token_list)):
        token_x, token_y, token_d = token_list[token_num]
        new_token_x = token_x + x_list[token_d]
        new_token_y = token_y + y_list[token_d]

        if (in_range(new_token_x, new_token_y) and board_arr[new_token_x][new_token_y] == 2) \
                or not in_range(new_token_x, new_token_y):
            token_d = change_dir[token_d]
            token_list[token_num][2] = token_d
            for i in range(len(token_arr[token_x][token_y])):
                if token_arr[token_x][token_y][i][0] == token_num:
                    token_arr[token_x][token_y][i][1] = token_d
            new_token_x = token_x + x_list[token_d]
            new_token_y = token_y + y_list[token_d]

        if in_range(new_token_x, new_token_y):
            if board_arr[new_token_x][new_token_y] == 0:
                after_token = -1
                for i in range(len(token_arr[token_x][token_y])):
                    token = token_arr[token_x][token_y][i]
                    if token[0] == token_num:
                        after_token = i
                    if after_token != -1:
                        token_list[token[0]][0] = new_token_x
                        token_list[token[0]][1] = new_token_y

                token_arr[new_token_x][new_token_y].extend(token_arr[token_x][token_y][after_token:])
                token_arr[token_x][token_y] = token_arr[token_x][token_y][:after_token]
            elif board_arr[new_token_x][new_token_y] == 1:
                after_token = -1
                for i in range(len(token_arr[token_x][token_y])):
                    token = token_arr[token_x][token_y][i]
                    if token[0] == token_num:
                        after_token = i
                    if after_token != -1:
                        token_list[token[0]][0] = new_token_x
                        token_list[token[0]][1] = new_token_y

                new_tokens = []
                can_tokens = token_arr[token_x][token_y][after_token:]
                for t in range(len(can_tokens) - 1, -1, -1):
                    new_tokens.append(can_tokens[t])

                token_arr[new_token_x][new_token_y].extend(new_tokens)
                token_arr[token_x][token_y] = token_arr[token_x][token_y][:after_token]

            if len(token_arr[new_token_x][new_token_y]) >= 4:
                break_while = True
                break

    if break_while: break

if turn > 1000:
    print(-1)
else:
    print(turn)