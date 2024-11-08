from queue import Queue

n, m = list(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 바닥, 동, 남, 서, 북, 하늘
dice = [6, 3, 2, 4, 5, 1]
opp_dict = {1: 3, 2: 4, 3: 1, 4: 2}
dice_x, dice_y, dice_d = 0, 0, 0

# 오아왼위
x_list = [0, 1, 0, -1]
y_list = [1, 0, -1, 0]

def in_range(i, j):
    return 0 <= i < n and 0 <= j < n

def rearrange_dice():
    global dice, dice_d

    new_dice = dice.copy()
    now_d = dice_d + 1
    opp_d = opp_dict[now_d]

    new_dice[now_d] = dice[-1]
    new_dice[opp_d] = dice[0]
    new_dice[0] = dice[now_d]
    new_dice[-1] = dice[opp_d]

    dice = new_dice

def roll_dice():
    global dice_x, dice_y, dice_d

    new_x, new_y = dice_x + x_list[dice_d], dice_y + y_list[dice_d]
    if not in_range(new_x, new_y):
        dice_d = (dice_d + 2) % 4
        new_x, new_y = dice_x + x_list[dice_d], dice_y + y_list[dice_d]
    dice_x, dice_y = new_x, new_y

    rearrange_dice()
    num = arr[dice_x][dice_y]
    bottom = dice[0]

    if bottom > num:
        dice_d = (dice_d + 1) % 4
    elif bottom < num:
        dice_d = (dice_d - 1) % 4

score_sum = 0
for _ in range(m):
    roll_dice()
    now_num = arr[dice_x][dice_y]

    q = Queue()
    q.put((dice_x, dice_y))
    visited = {(dice_x, dice_y)}
    while not q.empty():
        now_x, now_y = q.get()
        score_sum += now_num
        for d in range(4):
            new_x, new_y = now_x + x_list[d], now_y + y_list[d]
            if in_range(new_x, new_y):
                if arr[new_x][new_y] == now_num and (new_x, new_y) not in visited:
                    q.put((new_x, new_y))
                    visited.add((new_x, new_y))

print(score_sum)