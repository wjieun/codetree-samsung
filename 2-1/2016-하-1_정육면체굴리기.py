n, m, x, y, k = list(map(int, input().split()))

matrix = [
    list(map(int, input().split()))
    for _ in range(n)
]

roll_dir = list(map(int, input().split()))
roll_dir = [r-1 for r in roll_dir]

dice = [0] * 6

# 동서북남
dxs = [0, 0, -1, 1]
dys = [1, -1, 0, 0]

# 시작 0 1 2 3 4 5
rolling_dice = [
    [4, 1, 0, 3, 5, 2],
    [2, 1, 5, 3, 0, 4],
    [1, 5, 2, 0, 4, 3],
    [3, 0, 2, 5, 4, 1]
]

def roll_dice(d):
    global dice
    new_dice = [0] * 6
    for i in range(6):
        new_dice[i] = dice[rolling_dice[d][i]]
    dice = new_dice

def in_range(a, b):
    if 0 <= a < n and 0 <= b < m:
        return True
    return False

for roll_d in roll_dir:
    new_x, new_y = x + dxs[roll_d], y + dys[roll_d]
    if in_range(new_x, new_y):
        roll_dice(roll_d)

        if matrix[new_x][new_y] == 0:
            matrix[new_x][new_y] = dice[-1]
        else:
            dice[-1] = matrix[new_x][new_y]
            matrix[new_x][new_y] = 0

        x, y = new_x, new_y
        print(dice[0])