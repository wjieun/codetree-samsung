# n은 격자의 크기, m은 플레이어의 수, k는 라운드의 수
n, m, k = list(map(int, input().split()))

map_arr = [
    [[] for _ in range(n)]
    for _ in range(n)
]
for i in range(n):
    l = list(map(int, input().split()))
    for j in range(n):
        map_arr[i][j] = [l[j]] if l[j] != 0 else []

player_list = []
for _ in range(m):
    x, y, d, s = list(map(int, input().split()))
    player_list.append([x-1, y-1, d, s])

# ↑, →, ↓, ←
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def find_another_person(idx, x, y):
    global player_list
    return [p for p in range(m) if player_list[p][:2] == [x, y] and p != idx]

def find_new_coord(idx, x, y, d):
    global player_list

    while True:
        new_x, new_y = x + dxs[d], y + dys[d]

        if in_range(new_x, new_y):
            an_p = find_another_person(idx, new_x, new_y)

            if not len(an_p):
                return new_x, new_y, d

        d = (d + 1) % 4

def get_gun(gun, x, y):
    global map_arr
    for g in range(len(map_arr[x][y])):
        if map_arr[x][y][g] > gun:
            temp = gun
            gun = map_arr[x][y][g]
            map_arr[x][y][g] = temp
    if 0 in map_arr[x][y]:
        map_arr[x][y].remove(0)
    return gun

gun_list = [0 for _ in range(m)]
point_list = [0 for _ in range(m)]
def move_people():
    global map_arr, player_list, gun_list, point_list, dxs, dys

    for i in range(m):
        x, y, d, s = player_list[i]
        gun = gun_list[i]

        new_x, new_y = x + dxs[d], y + dys[d]
        if not in_range(new_x, new_y):
            d = (d - 2) % 4
            new_x, new_y = x + dxs[d], y + dys[d]

        another_person = find_another_person(i, new_x, new_y)
        if len(another_person):
            an_player = another_person[0]
            an_x, an_y, an_d, an_s = player_list[an_player]
            an_gun = gun_list[an_player]

            if an_s + an_gun > s + gun or \
                (an_s + an_gun == s + gun and an_s > s):
                point_list[an_player] += (an_s + an_gun) - (s + gun)
                if gun > 0:
                    map_arr[new_x][new_y].append(gun)
                    gun = 0

                new_x, new_y, d = find_new_coord(i, new_x, new_y, d)
                player_list[i] = [new_x, new_y, d, s]
            else:
                point_list[i] += (s + gun) - (an_s + an_gun)
                if an_gun > 0:
                    map_arr[new_x][new_y].append(an_gun)
                    an_gun = 0

                player_list[i] = [new_x, new_y, d, s]
                an_x, an_y, an_d = find_new_coord(an_player, new_x, new_y, an_d)
                player_list[an_player] = [an_x, an_y, an_d, an_s]

            an_gun = get_gun(an_gun, an_x, an_y)
            gun_list[an_player] = an_gun

        player_list[i] = [new_x, new_y, d, s]
        gun = get_gun(gun, new_x, new_y)
        gun_list[i] = gun

for _ in range(k):
    move_people()

for p in point_list:
    print(p, end=' ')