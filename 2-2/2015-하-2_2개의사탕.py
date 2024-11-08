N, M = list(map(int, input().split()))

mapping = {'#': -1, '.': 0, 'O': 1, 'B': 2, 'R': 3}

arr = [
    [mapping[x] for x in list(input())]
    for _ in range(N)
]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            blue_x, blue_y = i, j
            arr[i][j] = 0
        elif arr[i][j] == 3:
            red_x, red_y = i, j
            arr[i][j] = 0

visited = {(blue_x, blue_y, red_x, red_y): 0}

def get_candies(bx, by, rx, ry, d):
    if d == 0: # 위
        if bx < rx: return True, -1, 0
        else: return False, -1, 0
    elif d == 1: # 아래
        if bx < rx: return False, 1, 0
        else: return True, 1, 0
    elif d == 2: # 왼쪽
        if by < ry: return True, 0, -1
        else: return False, 0, -1
    else: # 오른쪽
        if by < ry: return False, 0, 1
        else: return True, 0, 1

def in_range(a, b):
    return 0 <= a < N and 0 <= b < M

def roll(bx, by, rx, ry, d):
    blue_first, x_move, y_move = get_candies(bx, by, rx, ry, d)

    if blue_first: candies = [[bx, by], [rx, ry]]
    else: candies = [[rx, ry], [bx, by]]

    if x_move:
        for ci in range(2):
            cx, cy = candies[ci]

            j = cy
            for i in range(cx + x_move, cx + N * x_move, x_move):
                if ci == 1 and (i, j) == tuple(candies[0]):
                    pass
                elif in_range(i, j):
                    if arr[i][j] == 1:
                        candies[ci] = [-1, -1]
                        break
                    if arr[i][j] != -1:
                        continue

                candies[ci][0] = i - x_move
                break
    else:
        for ci in range(2):
            cx, cy = candies[ci]

            i = cx
            for j in range(cy + y_move, cy + M * y_move, y_move):
                if ci == 1 and (i, j) == tuple(candies[0]):
                    pass
                elif in_range(i, j):
                    if arr[i][j] == 1:
                        candies[ci] = [-1, -1]
                        break
                    if arr[i][j] != -1:
                        continue

                candies[ci][1] = j - y_move
                break

    if blue_first:
        return candies[0][0], candies[0][1], candies[1][0], candies[1][1]
    else:
        return candies[1][0], candies[1][1], candies[0][0], candies[0][1]


min_count = 11
def recursive(bx, by, rx, ry, count):
    global min_count

    if count >= min_count - 1:
        return

    for d in range(4):
        new_bx, new_by, new_rx, new_ry = roll(bx, by, rx, ry, d)

        if (new_bx, new_by, new_rx, new_ry) not in visited \
                or visited[(new_bx, new_by, new_rx, new_ry)] > count + 1:
            visited[(new_bx, new_by, new_rx, new_ry)] = count + 1

            if (new_bx, new_by) == (-1, -1):
                continue
            elif (new_rx, new_ry) == (-1, -1):
                min_count = min(min_count, count + 1)
                continue

            recursive(new_bx, new_by, new_rx, new_ry, count + 1)

recursive(blue_x, blue_y, red_x, red_y, 0)

if min_count == 11:
    print(-1)
else:
    print(min_count)