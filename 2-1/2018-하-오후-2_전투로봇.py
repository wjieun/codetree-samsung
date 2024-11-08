from collections import deque

n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
] # 0 빈곳, 1~6 몬스터 레벨, 9 전투로봇

robot_level, robot_count = 2, 0
robot_x, robot_y = -1, -1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            robot_x, robot_y = i, j

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

def get_dis(i, j, min_dis):
    visited = {(robot_x, robot_y)}
    q = deque()
    q.append((robot_x, robot_y, 0))

    while q:
        x, y, count = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if count + 1 <= min_dis:
                if in_range(new_x, new_y) and (new_x, new_y) not in visited \
                        and arr[new_x][new_y] <= robot_level:
                    if (new_x, new_y) == (i, j):
                        return count + 1

                    visited.add((new_x, new_y))
                    q.append((new_x, new_y, count + 1))

    return float('inf')

def get_monster():
    min_dis, min_row, min_col = float('inf'), float('inf'), float('inf')

    for i in range(n):
        for j in range(n):
            if 0 < arr[i][j] < robot_level:
                now_dis = get_dis(i, j, min_dis)
                min_dis, min_row, min_col = min((min_dis, min_row, min_col), (now_dis, i, j))

    return min_dis, min_row, min_col

time = 0
while True:
    d, r, c = get_monster()
    if d == float('inf'):
        break
    else:
        arr[robot_x][robot_y] = 0
        robot_x, robot_y = r, c
        arr[robot_x][robot_y] = 9
        time += d

        robot_count += 1
        if robot_count == robot_level:
            robot_level += 1
            robot_count = 0

print(time)