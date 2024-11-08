N, K = list(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(N)
]

max_num = max(max(ar) for ar in arr)

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

def in_range(a, b):
    return 0 <= a < N and 0 <= b < N

def recursive(now_x, now_y, now_num, count, cut_num):
    global max_count
    can_go = False

    for dx, dy in zip(dxs, dys):
        new_x, new_y = now_x + dx, now_y + dy

        if in_range(new_x, new_y) and not visited[new_x][new_y]:
            new_num = arr[new_x][new_y]
            if new_num < now_num:
                can_go = True
                visited[new_x][new_y] = True
                recursive(
                    new_x, new_y, new_num,
                    count + 1, cut_num
                )
                visited[new_x][new_y] = False
            elif not cut_num and new_num - K < now_num:
                can_go = True
                visited[new_x][new_y] = True
                recursive(
                    new_x, new_y, now_num - 1,
                    count + 1, count + 1
                )
                visited[new_x][new_y] = False

    if not can_go:
        max_count = max(max_count, count)

max_count = 1
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == max_num:
            visited[i][j] = True
            recursive(i, j, max_num, 1, 0)
            visited[i][j] = False

print(max_count)