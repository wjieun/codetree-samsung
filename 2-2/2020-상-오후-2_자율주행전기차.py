from collections import deque

n, m, fuel = list(map(int, input().split()))

road_arr = [
    list(map(int, input().split()))
    for _ in range(n)
] # 0 도로, 1 벽

passenger_arr = [[0] * n for _ in range(n)]

car_x, car_y = [c - 1 for c in list(map(int, input().split()))]
passenger = dict()

for i in range(1, m + 1):
    passenger[i] = [c - 1 for c in list(map(int, input().split()))]
    s_x, s_y = passenger[i][0], passenger[i][1]
    passenger_arr[s_x][s_y] = i

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

def get_passenger():
    min_c, min_x, min_y = float('inf'), n, n

    visited = [[False] * n for _ in range(n)]
    visited[car_x][car_y] = True

    q = deque()
    q.append((car_x, car_y, 0))

    while q:
        qx, qy, qc = q.popleft()
        if qc > min_c:
            continue
        if passenger_arr[qx][qy]:
            min_c, min_x, min_y = min(
                (min_c, min_x, min_y),
                (qc, qx, qy)
            )
            continue

        for dx, dy in zip(dxs, dys):
            new_x, new_y = qx + dx, qy + dy

            if in_range(new_x, new_y) and not road_arr[new_x][new_y]\
                    and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                q.append((new_x, new_y, qc + 1))

    return min_c, min_x, min_y

def get_destination(idx):
    s_x, s_y, e_x, e_y = passenger[idx]

    visited = [[False] * n for _ in range(n)]
    visited[car_x][car_y] = True

    q = deque()
    q.append((s_x, s_y, 0))

    while q:
        qx, qy, qc = q.popleft()
        if (qx, qy) == (e_x, e_y):
            return qc

        for dx, dy in zip(dxs, dys):
            new_x, new_y = qx + dx, qy + dy

            if in_range(new_x, new_y) and not road_arr[new_x][new_y] \
                    and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                q.append((new_x, new_y, qc + 1))

    return 0

can_move_all = True
for _ in range(m):
    psg_c, psg_x, psg_y = get_passenger()
    car_x, car_y = psg_x, psg_y

    if psg_c == float('inf'):
        can_move_all = False
        break
    else:
        psg_idx = passenger_arr[psg_x][psg_y]
        move_dis = get_destination(psg_idx)

        if not move_dis or psg_c + move_dis > fuel:
            can_move_all = False
            break

        passenger_arr[psg_x][psg_y] = 0
        fuel = fuel - psg_c + move_dis
        _, _, car_x, car_y = passenger[psg_idx]

if can_move_all:
    print(fuel)
else:
    print(-1)