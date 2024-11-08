n, m, k = list(map(int, input().split()))

arr = [
    [[g] for g in list(map(int, input().split()))]
    for _ in range(n)
]

people_arr = [
    [0] * n
    for _ in range(n)
]

gun = dict()
power = dict()
point = dict()
position = dict()
direction = dict()

for i in range(1, m+1):
    x, y, d, s = list(map(int, input().split()))
    x, y = x - 1, y - 1

    people_arr[x][y] = i
    position[i] = (x, y)
    direction[i] = d
    power[i] = s
    point[i] = 0
    gun[i] = 0

# 0~3 ↑, →, ↓, ←
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

def get_gun(idx, gun_x, gun_y):
    arr_guns = arr[gun_x][gun_y]
    if arr_guns:
        max_gun = max(arr_guns)
        if max_gun > gun[idx]:
            max_gun_idx = arr_guns.index(max_gun)
            now_gun = gun[idx]
            gun[idx] = max_gun

            if now_gun:
                arr_guns[max_gun_idx] = now_gun
            else:
                arr_guns.pop(max_gun_idx)

for _ in range(k):
    # 1-1
    for i in range(1, m + 1):
        now_x, now_y = position[i]
        d = direction[i]

        new_x, new_y = now_x + dxs[d], now_y + dys[d]
        if not in_range(new_x, new_y):
            d = (d + 2) % 4
            new_x, new_y = now_x + dxs[d], now_y + dys[d]

        # 2-1
        people_arr[now_x][now_y] = 0
        position[i] = (new_x, new_y)
        direction[i] = d

        if not people_arr[new_x][new_y]:
            get_gun(i, new_x, new_y)
            people_arr[new_x][new_y] = i

        # 2-2
        else:
            # 2-2-1
            there_i = people_arr[new_x][new_y]
            now_s, there_s = power[i], power[there_i]
            now_gun, there_gun = gun[i], gun[there_i]
            now_sum, there_sum = now_s + now_gun, there_s + there_gun

            if now_sum > there_sum or (now_sum == there_sum and now_s > there_s):
                winner, loser = i, there_i
            else:
                winner, loser = there_i, i

            people_arr[new_x][new_y] = winner

            # 2-2-2
            arr[new_x][new_y].append(gun[loser])
            gun[loser] = 0
            loser_d = direction[loser]

            for new_loser_d in range(loser_d, loser_d + 4):
                new_loser_d = new_loser_d % 4

                new_loser_x, new_loser_y = new_x + dxs[new_loser_d], new_y + dys[new_loser_d]
                if in_range(new_loser_x, new_loser_y) and not people_arr[new_loser_x][new_loser_y]:
                    get_gun(loser, new_loser_x, new_loser_y)

                    people_arr[new_loser_x][new_loser_y] = loser
                    position[loser] = (new_loser_x, new_loser_y)
                    direction[loser] = new_loser_d

                    break

            # 2-2-3
            get_gun(winner, new_x, new_y)
            point[winner] += abs(now_sum - there_sum)

for i in range(1, m + 1):
    print(point[i], end=' ')