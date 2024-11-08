n = int(input())
seat = [[0] * n for _ in range(n)]
love = {}

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

def in_range(a, b):
    if 0 <= a < n and 0 <= b < n:
        return True
    return False

def find_seat(ns):
    x, y, empty, friend = n, n, -1, -1

    for i in range(n):
        for j in range(n):
            if not seat[i][j]:
                now_empty, now_friend = 0, 0
                for d in range(4):
                    new_i, new_j = i + dxs[d], j + dys[d]
                    if in_range(new_i, new_j):
                        if seat[new_i][new_j] in ns:
                            now_friend += 1
                        elif seat[new_i][new_j] == 0:
                            now_empty += 1

                change = False
                if now_friend > friend:
                    change = True
                elif now_friend == friend:
                    if now_empty > empty:
                        change = True
                    elif now_empty == empty:
                        if i < x:
                            change = True
                        elif i == x:
                            if j < y:
                                change = True

                if change:
                    x, y, empty, friend = i, j, now_empty, now_friend

    return x, y

# get seat
for _ in range(n * n):
    n_list = list(map(int, input().split()))
    now_num, now_list = n_list[0], n_list[1:]

    love[now_num] = now_list
    now_seat = find_seat(now_list)

    seat[now_seat[0]][now_seat[1]] = now_num

# get score
score = 0
for i in range(n):
    for j in range(n):
        now_num = seat[i][j]
        now_list = love[now_num]
        now_friend = 0

        for d in range(4):
            new_i, new_j = i + dxs[d], j + dys[d]
            if in_range(new_i, new_j):
                if seat[new_i][new_j] in now_list:
                    now_friend += 1

        if now_friend:
            score += 10 ** (now_friend - 1)

print(score)