n, m, x, y, k = list(map(int, input().split()))
map_arr = []
# now, 동, 서, 북, 남, opposite
dice = [0 for i in range(6)]
opp_dir = {1: 2, 2: 1, 3: 4, 4: 3}

# 동(1) 서(2) 북(3) 남(4)
move_x = [0, 0, -1, 1]
move_y = [1, -1, 0, 0]

# input
for i in range(n):
    map_arr.append(list(map(int, input().split())))
move_arr = list(map(int, input().split()))

# move
for dir in move_arr:
    new_x = x + move_x[dir-1]
    new_y = y + move_y[dir-1]

    if new_x >= 0 and new_x < n and new_y >= 0 and new_y < m:
        # dice 재정렬
        new_dice = dice.copy()
        new_dice[0] = dice[dir]
        new_dice[5] = dice[opp_dir[dir]]
        new_dice[opp_dir[dir]] = dice[0]
        new_dice[dir] = dice[5]
        dice = new_dice.copy()

        x = new_x; y = new_y
        if map_arr[x][y] == 0:
            map_arr[x][y] = dice[0]
        else:
            dice[0] = map_arr[x][y]
            map_arr[x][y] = 0
        print(dice[5])