from collections import deque

n, m, k = list(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

team_arr = [[-1] * n for _ in range(n)]
people_arr = [[False] * n for _ in range(n)]

lines = []
lines_len = []
dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

def get_line(now_x, now_y, visited):
    global lines

    line = [(now_x, now_y)]
    visited[now_x][now_y] = True

    next = {1: [2], 2: [2, 3], 3: [4], 4: [4]}
    count = 1

    while True:
        now_num = arr[now_x][now_y]
        is_added = False

        for dx, dy in zip(dxs, dys):
            new_x, new_y = now_x + dx, now_y + dy

            if in_range(new_x, new_y) and not visited[new_x][new_y] \
                    and arr[new_x][new_y] in next[now_num]:
                visited[new_x][new_y] = True
                line.append((new_x, new_y))
                now_x, now_y = new_x, new_y
                is_added = True

                if arr[new_x][new_y] < 4:
                    count += 1

                break

        if not is_added:
            break

    lines.append(line)
    lines_len.append(count)

def get_lines():
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                get_line(i, j, visited)

    for li, line in enumerate(lines):
        for lxyi, (lx, ly) in enumerate(line):
            team_arr[lx][ly] = li

            if 0 < arr[lx][ly] < 4:
                people_arr[lx][ly] = True
get_lines()

def move_teams():
    for line, line_len in zip(lines, lines_len):
        (x1, y1) = line[line_len - 1]
        line.insert(0, line.pop())
        (x2, y2) = line[0]

        people_arr[x1][y1] = False
        people_arr[x2][y2] = True

def throw_ball(t):
    global score

    t = t % (n * 4)
    t_dir = t // n
    t_num = t % n

    if t_dir == 0:
        x_start, x_end, x_step = t_num, t_num + 1, 1
        y_start, y_end, y_step = 0, n, 1
    elif t_dir == 1:
        x_start, x_end, x_step = n - 1, -1, -1
        y_start, y_end, y_step = t_num, t_num + 1, 1
    elif t_dir == 2:
        x_start, x_end, x_step = n - 1 - t_num, n - t_num, 1
        y_start, y_end, y_step = n - 1, -1, -1
    else:
        x_start, x_end, x_step = 0, n, 1
        y_start, y_end, y_step = n - 1 - t_num, n - t_num, 1

    for x in range(x_start, x_end, x_step):
        for y in range(y_start, y_end, y_step):
            if people_arr[x][y]:
                team_idx = team_arr[x][y]
                people_idx = lines[team_idx].index((x, y)) + 1
                score += people_idx ** 2

                reverse_team(team_idx)
                return

def reverse_team(team_idx):
    line = lines[team_idx]
    line_len = lines_len[team_idx]
    lines[team_idx] = list(reversed(line[:line_len])) + list(reversed(line[line_len:]))

score = 0
for turn in range(k):
    move_teams()  # 1
    throw_ball(turn)  # 2
print(score)