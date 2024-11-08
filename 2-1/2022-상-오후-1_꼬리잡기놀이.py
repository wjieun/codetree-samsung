n, m, k = list(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

team_arr = [
    [-1] * n
    for _ in range(n)
]

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

teams = []
teams_len = []
def get_teams():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                team_len, team_num = 0, len(teams)
                now_team = []
                now_x, now_y, now_n = i, j, 1
                end_loop = False

                while True:
                    now_team.append((now_x, now_y))
                    team_arr[now_x][now_y] = team_num
                    if 1 <= now_n <= 3: team_len += 1

                    for dx, dy in zip(dxs, dys):
                        new_x, new_y = now_x + dx, now_y + dy

                        if now_n == 1: next_ns = [2]
                        elif now_n == 2: next_ns = [2, 3]
                        else: next_ns = [4]

                        if in_range(new_x, new_y) and arr[new_x][new_y] in next_ns \
                                and (new_x, new_y) not in now_team:
                            now_x, now_y, now_n = new_x, new_y, arr[new_x][new_y]
                            break
                        elif in_range(new_x, new_y) and \
                                now_n in [3, 4] and arr[new_x][new_y] == 1:
                            end_loop = True
                            break

                    if end_loop:
                        break

                teams.append(now_team)
                teams_len.append(team_len)

get_teams()
scores = [0] * len(teams)

def throw_ball(turn):
    turn = turn % (n * 4)
    direction = turn // n
    line_num = turn % n
    if direction == 0:
        i_start, i_end, i_step = line_num, line_num + 1, 1
        j_start, j_end, j_step = 0, n, 1
    elif direction == 1:
        i_start, i_end, i_step = n - 1, -1, -1
        j_start, j_end, j_step = line_num, line_num + 1, 1
    elif direction == 2:
        i_start, i_end, i_step = n - 1 - line_num, n - 1 - line_num - 1, -1
        j_start, j_end, j_step = n - 1, -1, -1
    else:
        i_start, i_end, i_step = 0, n, 1
        j_start, j_end, j_step = n - 1 - line_num, n - 1 - line_num - 1, -1

    for i in range(i_start, i_end, i_step):
        for j in range(j_start, j_end, j_step):
            if 0 < arr[i][j] < 4:
                team_num = team_arr[i][j]
                player_num = teams[team_num].index((i, j)) + 1
                scores[team_num] += player_num * player_num

                team_len = teams_len[team_num]
                teams[team_num].reverse()
                teams[team_num] = teams[team_num][-team_len:] + teams[team_num][:-team_len]

                t = teams[team_num]
                re_arr(t, team_len)

                return

def re_arr(now_team, now_team_len):
    first, second, last = now_team[0], now_team[1], now_team[now_team_len - 1]

    arr[first[0]][first[1]] = 1
    arr[second[0]][second[1]] = 2
    arr[last[0]][last[1]] = 3

    if now_team_len < len(now_team):
        out = now_team[now_team_len]
        arr[out[0]][out[1]] = 4


all_team_num = len(teams)
for turn in range(0, k):
    # 1
    for idx in range(all_team_num):
        t, t_len = teams[idx], teams_len[idx]
        t.insert(0, t.pop())
        re_arr(t, t_len)

    # 2
    throw_ball(turn)

print(sum(scores))