MAX_T = 25
DIR_NUM = 8
P_DIR_NUM = 4
MAX_DECAY = 2

n = 4
m, t = tuple(map(int, input().split()))
px, py = tuple(map(int, input().split()))
px, py = px - 1, py - 1

# t번째 턴에 (x, y)에 위치한 방향 move_dir을 바라보는 몬스터
monster = [
    [
        [[0] * DIR_NUM for _ in range(n)]
    ]
    for _ in range(MAX_T + 1)
]

dead = [
    [[0] * (MAX_DECAY + 1) for _ in range(n)]
    for _ in range(n)
]

dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, -1, -1, -1, 0, 1, 1, 1]

p_dxs = [-1, 0, 1, 0]
p_dys = [0, -1, 0, 1]

t_num = 1


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def can_go(x, y):
    return in_range(x, y) and dead[x][y][0] == 0 and dead[x][y][1] == 0 \
        and (x, y) != (px, py)


def get_next_pos(x, y, move_dir):
    for c_dir in range(DIR_NUM):
        n_dir = (move_dir + c_dir + DIR_NUM) % DIR_NUM
        nx, ny = x + dxs[n_dir], y + dys[n_dir]
        if can_go(nx, ny):
            return nx, ny, n_dir
    return x, y, move_dir


# 같은 좌표와 방향을 가진 몬스터를 모두 한 번에 옮김
def move_m():
    for i in range(n):
        for j in range(n):
            for k in range(DIR_NUM):
                x, y, next_dir = get_next_pos(i, j, k)
                monster[t_num][x][y][next_dir] += monster[t_num - 1][i][j][k]


def get_killed_num(dir1, dir2, dir3):
    x, y = px, py
    killed_num = 0

    v_pos = []

    for move_dir in [dir1, dir2, dir3]:
        nx, ny = x + p_dxs[move_dir], y + p_dys[move_dir]
        if not in_range(nx, ny):
            return -1
        if (nx, ny) not in v_pos:
            killed_num += sum(monster[t_num][nx][ny])
            v_pos.append((nx, ny))

        x, y = nx, ny

    return killed_num


def do_kill(best_route):
    global px, py

    dir1, dir2, dir3 = best_route

    for move_dir in [dir1, dir2, dir3]:
        nx, ny = px + p_dxs[move_dir], py + p_dys[move_dir]

        for i in range(DIR_NUM):
            dead[nx][ny][MAX_DECAY] += monster[t_num][nx][ny][i]
            monster[t_num][nx][ny][i] = 0

        px, py = nx, ny


def move_p():
    max_cnt = -1
    best_route = (-1, -1, -1)

    for i in range(P_DIR_NUM):
        for j in range(P_DIR_NUM):
            for k in range(P_DIR_NUM):
                m_cnt = get_killed_num(i, j, k)
                if m_cnt > max_cnt:
                    max_cnt = m_cnt
                    best_route = (i, j, k)

    do_kill(best_route)


def decay_m():
    for i in range(n):
        for j in range(n):
            for k in range(MAX_DECAY):
                dead[i][j][k] = dead[i][j][k + 1]
            dead[i][j][MAX_DECAY] = 0


def add_m():
    for i in range(n):
        for j in range(n):
            for k in range(DIR_NUM):
                monster[t_num][i][j][k] += monster[t_num - 1][i][j][k]


def simulate():
    move_m()
    move_p()
    decay_m()
    add_m()


def count_monster():
    cnt = 0

    for i in range(n):
        for j in range(n):
            for k in range(DIR_NUM):
                cnt += monster[t][i][j][k]

    return cnt


for _ in range(m):
    mx, my, mdir = tuple(map(int, input().split()))
    monster[0][mx - 1][my - 1][mdir - 1] += 1

while t_num <= t:
    simulate()
    t_num += 1

print(count_monster())