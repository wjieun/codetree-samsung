from collections import deque

n, m, k = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

team_head, team_tail, team_list = [], [], []
team_d = [0 for _ in range(m)]
team_score = [0 for _ in range(m)]

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def get_team(x, y):
    team_head.append(0)

    new_team = []
    q = deque(); q.append((x, y))
    while q:
        now_x, now_y = q.popleft()
        new_team.append((now_x, now_y))
        if arr[now_x][now_y] == 3:
            team_tail.append(len(new_team) - 1)

        for dx, dy in zip(dxs, dys):
            new_x, new_y = now_x + dx, now_y + dy
            if in_range(new_x, new_y):
                if (len(new_team) == 1 and arr[new_x][new_y] == 2) \
                        or (len(new_team) != 1 and arr[new_x][new_y] in [2, 3, 4]):
                    if (new_x, new_y) not in new_team:
                        q.append((new_x, new_y))
                        break

    team_list.append(new_team)

def get_all_team():
    global team_head, team_tail, team_list, team_num
    team_head, team_tail, team_list = [], [], []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                get_team(i, j)

def move_people():
    global arr

    new_arr = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    for i in range(m):
        if team_d[i] == 0:
            team_head[i] = (team_head[i] - 1) % len(team_list[i])
            team_tail[i] = (team_tail[i] - 1) % len(team_list[i])
        else:
            team_head[i] = (team_head[i] + 1) % len(team_list[i])
            team_tail[i] = (team_tail[i] + 1) % len(team_list[i])

        for j in range(len(team_list[i])):
            if team_d[i] == 0:
                idx = (team_head[i] + j) % len(team_list[i])
            else:
                idx = (team_head[i] - j) % len(team_list[i])
            x, y = team_list[i][idx]

            if j == 0:
                new_arr[x][y] = 1
            elif j < team_num[i]:
                new_arr[x][y] = 2
            elif j == team_num[i]:
                new_arr[x][y] = 3
            else:
                new_arr[x][y] = 4

    arr = new_arr

def find_team(x, y):
    for i in range(m):
        if (x, y) in team_list[i]:
            head = team_head[i]
            now = team_list[i].index((x, y))
            if team_d[i] == 0:  # 정방향
                s = now - head + 1
                if head > now: s += len(team_list[i])
            else:  # 역방향
                s = head - now + 1
                if head < now: s += len(team_list[i])

            team_score[i] += s * s

            temp = team_head[i]
            team_head[i] = team_tail[i]
            team_tail[i] = temp

            team_d[i] = abs(team_d[i] - 1)

            return

def throw_ball(t):
    if t % (n * 4) < n:
        for y in range(n):
            if 0 < arr[t % n][y] < 4:
                find_team(t % n, y)
                break
    elif t % (n * 4) < n * 2:
        for x in range(n - 1, -1, -1):
            if 0 < arr[x][t % n] < 4:
                find_team(x, t % n)
                break
    elif t % (n * 4) < n * 3:
        for y in range(n - 1, -1, -1):
            if 0 < arr[n - 1 - t % n][y] < 4:
                find_team(n - 1 - t % n, y)
                break
    else:
        for x in range(n):
            if 0 < arr[x][n - 1 - t % n] < 4:
                find_team(x, n - 1 - t % n)
                break

get_all_team()
team_num = team_tail.copy()

for turn in range(k):
    move_people()
    throw_ball(turn)
print(sum(team_score))