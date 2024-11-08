from queue import Queue

n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

robot_x, robot_y, robot_level = -1, -1, 2
monster_list = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            robot_x, robot_y = i, j
            arr[i][j] = 0
        elif arr[i][j] > 0:
            monster_list.append((i, j))

x_list = [1, -1, 0, 0]
y_list = [0, 0, 1, -1]

def in_range(i, j):
    return 0 <= i < n and 0 <= j < n

def get_min_distance():
    min_distance_arr = [
        [float('inf') for _ in range(n)]
        for _ in range(n)
    ]
    visited = [
        [False for _ in range(n)]
        for _ in range(n)
    ]
    q = Queue()

    min_distance_arr[robot_x][robot_y] = 0
    visited[robot_x][robot_y] = True
    q.put((robot_x, robot_y))

    while not q.empty():
        now_x, now_y = q.get()
        for d in range(4):
            new_x, new_y = now_x + x_list[d], now_y + y_list[d]
            if in_range(new_x, new_y) and not visited[new_x][new_y]:
                visited[new_x][new_y] = True

                if arr[new_x][new_y] <= robot_level:
                    min_distance_arr[new_x][new_y] = min_distance_arr[now_x][now_y] + 1
                    q.put((new_x, new_y))

    return min_distance_arr

def get_monster():
    min_monster_coord = (-1, -1)
    min_monster_dis = float('inf')
    min_distance_arr = get_min_distance()

    for monster_x, monster_y in monster_list:
        if arr[monster_x][monster_y] < robot_level:
            if min_distance_arr[monster_x][monster_y] < min_monster_dis:
                min_monster_dis = min_distance_arr[monster_x][monster_y]
                min_monster_coord = (monster_x, monster_y)

    return min_monster_coord, min_monster_dis

kill_monster_num = 0
time = 0
while True:
    if len(monster_list) == 0:
        break

    (m_x, m_y), min_dis = get_monster()
    if m_x == m_y == -1:
        break
    else:
        robot_x, robot_y = m_x, m_y
        monster_list.remove((m_x, m_y))
        kill_monster_num += 1

    if kill_monster_num % robot_level == 0:
        robot_level += 1
        kill_monster_num = 0

    time += min_dis
print(time)