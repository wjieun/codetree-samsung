from collections import deque

n, m = list(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
] # -1 검은색 돌, 0 빨간색 폭탄, 1~m 서로 다른 색의 폭탄, -2 빈칸

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

def get_biggest_bomb():
    visited = [[False] * n for _ in range(n)]

    max_bomb, min_red = set(), float('inf')
    max_row, min_col = 0, float('inf')

    for i in range(n-1, -1, -1):
        for j in range(n):
            if not visited[i][j] and arr[i][j] > 0:
                bomb_number = arr[i][j]
                visited[i][j] = True

                now = {(i, j)}
                red = 0

                q = deque()
                q.append((i, j))

                while q:
                    qi, qj = q.popleft()

                    for dx, dy in zip(dxs, dys):
                        new_x, new_y = qi + dx, qj + dy
                        if in_range(new_x, new_y):
                            if arr[new_x][new_y] == 0 and (new_x,new_y) not in now:
                                red += 1
                                now.add((new_x, new_y))
                                q.append((new_x, new_y))
                            elif arr[new_x][new_y] == bomb_number and not visited[new_x][new_y]:
                                visited[new_x][new_y] = True
                                now.add((new_x, new_y))
                                q.append((new_x, new_y))

                change = False
                if len(now) >= 2:
                    if len(max_bomb) < len(now):
                        change = True
                    elif len(max_bomb) == len(now):
                        if min_red > red:
                            change = True
                        elif min_red == red:
                            if max_row < i:
                                change = True
                            elif max_row == i:
                                if min_col > j:
                                    change = True

                if change:
                    max_bomb, min_red, max_row, min_col = now, red, i, j

    return max_bomb

def gravity():
    for j in range(n):
        i = n-2
        while i >= 0:
            if arr[i][j] >= 0:
                for bottom in range(i+1, n+1):
                    if bottom == n or arr[bottom][j] != -2:
                        break

                if bottom-1 != i:
                    arr[bottom-1][j] = arr[i][j]
                    arr[i][j] = -2
            i -= 1
    return

def rotate():
    global arr
    new_arr = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new_arr[n - 1 - j][i] = arr[i][j]

    arr = new_arr

score = 0
while True:
    bomb = get_biggest_bomb()

    if bomb:
        C = len(bomb)
        score += C * C

        for bx, by in bomb:
            arr[bx][by] = -2
    else:
        break

    gravity()
    rotate()
    gravity()

print(score)