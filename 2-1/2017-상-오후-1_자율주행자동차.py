n, m = list(map(int, input().split()))
# d: 0 ~ 3 북동남서
# x, y: 0 ~ n-1
x, y, d = list(map(int, input().split()))
state = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]
visited[x][y] = True

x_dir = [-1, 0, 1, 0]
y_dir = [0, 1, 0, -1]

def in_range(a, b):
    if 0 <= a < n and 0 <= b < m:
        if state[a][b] == 0:
            return True
    return False

while True:
    # 1
    move = False
    for _ in range(4):
        d = (d - 1) % 4
        x_pos, y_pos = x + x_dir[d], y + y_dir[d]
        if in_range(x_pos, y_pos) and not visited[x_pos][y_pos]:
            x, y = x_pos, y_pos
            visited[x][y] = True
            move = True
            break

    # 3
    if not move:
        new_d = (d - 2) % 4
        x_pos, y_pos = x + x_dir[new_d], y + y_dir[new_d]

        if in_range(x_pos, y_pos):
            x, y = x_pos, y_pos
        else:
            break

v_count = [v.count(True) for v in visited]
print(sum(v_count))