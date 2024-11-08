from collections import deque

n, m = list(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 오아왼위
d = 0
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

dice_x, dice_y = 0, 0
dice = [1, 2, 3, 6, 5, 4]
opp_dice = {0: 3, 1: 4, 2: 5, 3: 0, 4: 1, 5: 2}
score = dict()

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

visited = [
    [False] * n
    for _ in range(n)
]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            number = arr[i][j]
            number_set = set()

            q = deque()
            q.append((i, j))

            while q:
                qi, qj = q.popleft()
                number_set.add((qi, qj))

                for dx, dy in zip(dxs, dys):
                    new_x, new_y = qi + dx, qj + dy

                    if in_range(new_x, new_y) and not visited[new_x][new_y]\
                            and arr[new_x][new_y] == number:
                        visited[new_x][new_y] = True
                        q.append((new_x, new_y))

            sc = number * len(number_set)
            for np in number_set:
                score[np] = sc

def roll():
    global dice

    if d == 0: new_top_idx = 5
    elif d == 1: new_top_idx = 4
    elif d == 2: new_top_idx = 2
    elif d == 3: new_top_idx = 1

    new_dice = dice.copy()
    new_dice[0] = dice[new_top_idx]
    new_dice[3] = dice[opp_dice[new_top_idx]]
    new_dice[opp_dice[new_top_idx]] = dice[0]
    new_dice[new_top_idx] = dice[3]

    dice = new_dice

score_sum = 0
for _ in range(m):
    new_dice_x, new_dice_y = dice_x + dxs[d], dice_y + dys[d]
    if not in_range(new_dice_x, new_dice_y):
        d = (d + 2) % 4
        new_dice_x, new_dice_y = dice_x + dxs[d], dice_y + dys[d]
    dice_x, dice_y = new_dice_x, new_dice_y

    roll()
    score_sum += score[(dice_x, dice_y)]

    if dice[3] > arr[dice_x][dice_y]:
        d = (d + 1) % 4
    elif dice[3] < arr[dice_x][dice_y]:
        d = (d - 1) % 4

print(score_sum)