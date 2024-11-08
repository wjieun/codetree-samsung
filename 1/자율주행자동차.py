n, m = list(map(int, input().split()))
x, y, d = list(map(int, input().split()))

# d 북(0) 동(1) 남(2) 서(3)
x_list = [-1, 0, 1, 0]
y_list = [0, 1, 0, -1]
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]
visited[x][y] = True

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

four_dir = 0
while True:
    if four_dir == 4:
        new_d = (d - 2) % 4
        new_x = x + x_list[new_d]
        new_y = y + y_list[new_d]
        if not 0 <= new_x < n or not 0 <= new_y < m or arr[new_x][new_y]:
            break
        else:
            four_dir = 0
            visited[new_x][new_y] = True
            x, y = new_x, new_y

    new_d = (d - (1 + four_dir)) % 4
    new_x = x + x_list[new_d]
    new_y = y + y_list[new_d]

    if not 0 <= new_x < n or not 0 <= new_y < m\
        or arr[new_x][new_y] or visited[new_x][new_y]:
        four_dir += 1
        continue

    four_dir = 0
    visited[new_x][new_y] = True
    x, y, d = new_x, new_y, new_d

sum_visited = sum([sum(v) for v in visited])
print(sum_visited)