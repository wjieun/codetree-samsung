from queue import Queue

# 격자의 크기 n, 승객의 수 m, 초기 배터리 충전량 c
n, m, c = list(map(int, input().split()))

road_arr = [
    list(map(int, input().split()))
    for _ in range(n)
] # 0 도로, 1 벽

car_x, car_y = list(map(int, input().split()))
car_x, car_y = car_x - 1, car_y - 1

passenger_arr = [
    [x - 1 for x in list(map(int, input().split()))]
    for _ in range(m)
] # 출발지의 위치 정보 x_s, y_s, 도착지의 위치 정보 x_e, y_e

x_list = [1, -1, 0, 0]
y_list = [0, 0, 1, -1]

def can_go(x, y):
    if 0 <= x < n and 0 <= y < n:
        if road_arr[x][y] == 0:
            return True
    return False

def find_close_distance(min_dis, s_x, s_y, e_x, e_y):
    if s_x == e_x and s_y == e_y:
        return 0

    q = Queue(); q.put((s_x, s_y, 0))
    visited = set(); visited.add((s_x, s_y))

    while not q.empty():
        now_x, now_y, dis = q.get()

        if dis > min_dis:
            return -1

        for d in range(4):
            new_x, new_y = now_x + x_list[d], now_y + y_list[d]
            if can_go(new_x, new_y):
                if (new_x, new_y) not in visited:
                    if (new_x, new_y) == (e_x, e_y):
                        return dis + 1

                    q.put((new_x, new_y, dis + 1))
                    visited.add((new_x, new_y))

    return -1

def find_close_passenger():
    global passenger_arr, car_x, car_y
    min_dis = float('inf')
    min_x, min_y = -1, -1
    p_idx = -1
    for i in range(len(passenger_arr)):
        if i not in arrived_list:
            x_s, y_s, _, _ = passenger_arr[i]
            dis_i = find_close_distance(min_dis, car_x, car_y, x_s, y_s)
            if dis_i != -1:
                if min_dis > dis_i:
                    min_dis, p_idx = dis_i, i
                    min_x, min_y = x_s, y_s
                elif min_dis == dis_i:
                    if (min_x > x_s) or (min_x == x_s and min_y > y_s):
                        min_dis, p_idx = dis_i, i
                        min_x, min_y = x_s, y_s

    return p_idx, min_dis

passenger_distance = []
for x_s, y_s, x_e, y_e in passenger_arr:
    dis = find_close_distance(float('inf'), x_s, y_s, x_e, y_e)
    passenger_distance.append(dis)

if any([dis == -1 for dis in passenger_distance]):
    print(-1)
else:
    arrived_list = []
    while True:
        p, dis = find_close_passenger()
        move_dis = passenger_distance[p]

        if dis + move_dis <= c:
            _, _, x_e, y_e = passenger_arr[p]
            c = c - dis + move_dis
            car_x, car_y = x_e, y_e
            arrived_list.append(p)

            if len(arrived_list) == m:
                print(c)
                break
        else:
            print(-1)
            break