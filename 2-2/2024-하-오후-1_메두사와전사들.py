from collections import deque

N, M = list(map(int, input().split()))
car_x, car_y, dest_x, dest_y = list(map(int, input().split()))

wolf_info = list(map(int, input().split()))
wolf_list = dict()
wolf_arr = [[None] * N for _ in range(N)]
for i in range(M):
    wolf_x, wolf_y = wolf_info[2 * i], wolf_info[2 * i + 1]
    wolf_list[i] = (wolf_x, wolf_y)

    if wolf_arr[wolf_x][wolf_y]:
        wolf_arr[wolf_x][wolf_y].add(i)
    else:
        wolf_arr[wolf_x][wolf_y] = {i}

arr = [
    list(map(int, input().split()))
    for _ in range(N)
]

# 상하좌우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

# 좌우상하
dxs2 = [0, 0, -1, 1]
dys2 = [-1, 1, 0, 0]

def in_range(a, b):
    return 0 <= a < N and 0 <= b < N

def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def move_car():
    visited_car = [[False] * N for _ in range(N)]
    visited_car[car_x][car_y] = True

    q = deque()
    q.append((car_x, car_y, []))

    while q:
        qx, qy, q_list = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = qx + dx, qy + dy

            if in_range(new_x, new_y) and not visited_car[new_x][new_y] \
                    and not arr[new_x][new_y]:
                visited_car[new_x][new_y] = True

                if (new_x, new_y) == (dest_x, dest_y):
                    return q_list + [(new_x, new_y)]

                q.append((new_x, new_y, q_list + [(new_x, new_y)]))

def turn_lights():
    max_count, max_lights = -1, None

    for d in range(4):
        wolf_count = 0
        lights = [[0] * N for _ in range(N)] # -1 그림자, 1 빛

        # 상
        if d == 0:
            for t, i in enumerate(range(car_x - 1, -1, -1)):
                t = t + 1

                start_j = max(0, car_y - t)
                end_j = min(N, car_y + t + 1)

                for j in range(start_j, end_j):
                    if lights[i][j] != -1:
                        lights[i][j] = 1

                        if wolf_arr[i][j]:
                            wolf_count += len(wolf_arr[i][j])

                            if j == car_y:
                                for shadow_i in range(i - 1, -1, -1):
                                    lights[shadow_i][j] = -1
                            else:
                                for shadow_t, shadow_i in enumerate(range(i - 1, -1, -1)):
                                    shadow_t = shadow_t + 1

                                    if j < car_y:
                                        start_shadow_j = max(0, j - shadow_t)
                                        end_shadow_j = min(N, j + 1)
                                    else:
                                        start_shadow_j = max(0, j)
                                        end_shadow_j = min(N, j + shadow_t + 1)

                                    for shadow_j in range(start_shadow_j, end_shadow_j):
                                        lights[shadow_i][shadow_j] = -1

        # 하
        elif d == 1:
            for t, i in enumerate(range(car_x + 1, N, 1)):
                t = t + 1

                start_j = max(0, car_y - t)
                end_j = min(N, car_y + t + 1)

                for j in range(start_j, end_j):
                    if lights[i][j] != -1:
                        lights[i][j] = 1

                        if wolf_arr[i][j]:
                            wolf_count += len(wolf_arr[i][j])

                            if j == car_y:
                                for shadow_i in range(i + 1, N, 1):
                                    lights[shadow_i][j] = -1
                            else:
                                for shadow_t, shadow_i in enumerate(range(i + 1, N, 1)):
                                    shadow_t = shadow_t + 1

                                    if j < car_y:
                                        start_shadow_j = max(0, j - shadow_t)
                                        end_shadow_j = min(N, j + 1)
                                    else:
                                        start_shadow_j = max(0, j)
                                        end_shadow_j = min(N, j + shadow_t + 1)

                                    for shadow_j in range(start_shadow_j, end_shadow_j):
                                        lights[shadow_i][shadow_j] = -1

        # 좌
        elif d == 2:
            for t, j in enumerate(range(car_y - 1, -1, -1)):
                t = t + 1

                start_i = max(0, car_x - t)
                end_i = min(N, car_x + t + 1)

                for i in range(start_i, end_i):
                    if lights[i][j] != -1:
                        lights[i][j] = 1

                        if wolf_arr[i][j]:
                            wolf_count += len(wolf_arr[i][j])

                            if i == car_x:
                                for shadow_j in range(j - 1, -1, -1):
                                    lights[i][shadow_j] = -1
                            else:
                                for shadow_t, shadow_j in enumerate(range(j - 1, -1, -1)):
                                    shadow_t = shadow_t + 1

                                    if i < car_x:
                                        start_shadow_i = max(0, i - shadow_t)
                                        end_shadow_i = min(N, i + 1)
                                    else:
                                        start_shadow_i = max(0, i)
                                        end_shadow_i = min(N, i + shadow_t + 1)

                                    for shadow_i in range(start_shadow_i, end_shadow_i):
                                        lights[shadow_i][shadow_j] = -1

        # 우
        elif d == 3:
            for t, j in enumerate(range(car_y + 1, N, 1)):
                t = t + 1

                start_i = max(0, car_x - t)
                end_i = min(N, car_x + t + 1)

                for i in range(start_i, end_i):
                    if lights[i][j] != -1:
                        lights[i][j] = 1

                        if wolf_arr[i][j]:
                            wolf_count += len(wolf_arr[i][j])

                            if i == car_x:
                                for shadow_j in range(j + 1, N, 1):
                                    lights[i][shadow_j] = -1
                            else:
                                for shadow_t, shadow_j in enumerate(range(j + 1, N, 1)):
                                    shadow_t = shadow_t + 1

                                    if i < car_x:
                                        start_shadow_i = max(0, i - shadow_t)
                                        end_shadow_i = min(N, i + 1)
                                    else:
                                        start_shadow_i = max(0, i)
                                        end_shadow_i = min(N, i + shadow_t + 1)

                                    for shadow_i in range(start_shadow_i, end_shadow_i):
                                        lights[shadow_i][shadow_j] = -1


        if wolf_count > max_count:
            max_count, max_lights = wolf_count, lights

    return max_count, max_lights

def move_wolf(lights):
    global wolf_arr

    wolf_count, total_distance = 0, 0
    new_wolf_arr = [[None] * N for _ in range(N)]
    deleted_list = set()

    for wolf_idx, (wolf_x, wolf_y) in wolf_list.items():
        if lights[wolf_x][wolf_y] != 1: # 전조등에 비춰진 늑대들
            distance = 0
            delete_wolf = False
            now_dis = get_distance(car_x, car_y, wolf_x, wolf_y)

            # 첫 번째 이동
            for dx, dy in zip(dxs, dys):
                new_x, new_y = wolf_x + dx, wolf_y + dy

                if in_range(new_x, new_y) and lights[new_x][new_y] != 1:
                    new_dis = get_distance(car_x, car_y, new_x, new_y)

                    if new_dis < now_dis:
                        distance += 1
                        now_dis = new_dis
                        wolf_x, wolf_y = new_x, new_y

                        if (new_x, new_y) == (car_x, car_y):
                            wolf_count += 1
                            delete_wolf = True

                        break

            # 두 번째 이동
            if distance and not delete_wolf:
                for dx, dy in zip(dxs2, dys2):
                    new_x, new_y = wolf_x + dx, wolf_y + dy

                    if in_range(new_x, new_y) and lights[new_x][new_y] != 1:
                        new_dis = get_distance(car_x, car_y, new_x, new_y)

                        if new_dis < now_dis:
                            distance += 1
                            wolf_x, wolf_y = new_x, new_y

                            if (new_x, new_y) == (car_x, car_y):
                                wolf_count += 1
                                delete_wolf = True

                            break

            total_distance += distance
            if not delete_wolf:
                wolf_list[wolf_idx] = (wolf_x, wolf_y)
                if new_wolf_arr[wolf_x][wolf_y]:
                    new_wolf_arr[wolf_x][wolf_y].add(wolf_idx)
                else:
                    new_wolf_arr[wolf_x][wolf_y] = {wolf_idx}
            else:
                deleted_list.add(wolf_idx)

        else: # 전조등에 비춰지지 않은 늑대들
            if new_wolf_arr[wolf_x][wolf_y]:
                new_wolf_arr[wolf_x][wolf_y].add(wolf_idx)
            else:
                new_wolf_arr[wolf_x][wolf_y] = {wolf_idx}

    wolf_arr = new_wolf_arr

    for wolf_idx in deleted_list:
        del wolf_list[wolf_idx]

    return wolf_count, total_distance

roads = move_car()
if not roads:
    print(-1)
else:
    road_len = len(roads)
    road_idx = 0
    while True:
        # 1 - 마차
        car_x, car_y = roads[road_idx]
        road_idx += 1

        if road_idx == road_len:
            print(0)
            break

        if wolf_arr[car_x][car_y]:
            for wolf_idx in wolf_arr[car_x][car_y]:
                del wolf_list[wolf_idx]
        wolf_arr[car_x][car_y] = None

        # 2 - 전조등
        lights_count, lights_arr = turn_lights()

        # 3 - 늑대
        attack_count, move_distance = move_wolf(lights_arr)

        # 4 - 출력
        print(move_distance, lights_count, attack_count)