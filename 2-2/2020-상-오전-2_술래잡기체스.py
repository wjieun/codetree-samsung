# import sys
# sys.setrecursionlimit(10**7)

n = 4
arr = [
    [0] * n
    for _ in range(n)
]

thieves = dict()

for i in range(n):
    thief_list = list(map(int, input().split()))
    for j in range(n):
        p, d = thief_list[2 * j], thief_list[2 * j + 1] - 1
        thieves[p] = (i, j, d)
        arr[i][j] = p

tagger_x, tagger_y = 0, 0
first_thief = arr[0][0]
tagger_d = thieves[first_thief][-1]
thieves[first_thief] = (-1, -1, -1)
arr[0][0] = -1

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, -1, -1, -1, 0, 1, 1, 1]

max_score = first_thief

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

def move_thieves(now_thieves, now_arr):
    new_arr = [list(ar) for ar in now_arr]
    new_thieves = {i: now_thieves[i] for i in now_thieves}

    for i in range(1, 17):
        if new_thieves[i][0] != -1:
            now_x, now_y, now_d = new_thieves[i]
            moved = False

            for new_d in range(now_d, now_d + 8):
                new_d = new_d % 8
                new_x, new_y = now_x + dxs[new_d], now_y + dys[new_d]

                if in_range(new_x, new_y) and new_arr[new_x][new_y] != -1:
                    new_i = new_arr[new_x][new_y]

                    if new_i:
                        # change new
                        new_thieves[new_i] = (now_x, now_y, new_thieves[new_i][-1])
                    new_arr[now_x][now_y] = new_i

                    # change now
                    new_thieves[i] = (new_x, new_y, new_d)
                    new_arr[new_x][new_y] = i

                    moved = True
                    break

            if not moved:
                new_thieves[i] = (now_x, now_y, new_d)

    return new_thieves, new_arr

def recursive(now_x, now_y, now_d, now_t, now_a, score):
    global max_score

    new_t, new_a = move_thieves(now_t, now_a)

    can_go = False
    for i in range(1, 4):
        new_x, new_y = now_x + dxs[now_d] * i, now_y + dys[now_d] * i
        if not in_range(new_x, new_y):
            break

        new_num = new_a[new_x][new_y]

        if new_num:
            can_go = True

            # change
            orig_thief = new_t[new_num]
            new_d = orig_thief[-1]
            new_t[new_num] = (-1, -1, -1)
            new_a[now_x][now_y], new_a[new_x][new_y] = 0, -1

            recursive(new_x, new_y, new_d, new_t, new_a, score + new_num)

            # restore original
            new_t[new_num] = orig_thief
            new_a[now_x][now_y], new_a[new_x][new_y] = -1, new_num

    if not can_go:
        max_score = max(max_score, score)

recursive(tagger_x, tagger_y, tagger_d, thieves, arr, first_thief)

print(max_score)