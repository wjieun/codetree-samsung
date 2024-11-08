n, m = list(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 0번부터 3번까지 각각 → ↓ ← ↑
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

mid = n // 2
max_length = n * n - 1

space_num = []
for num in range(1, n):
    space_num.append(num)
    space_num.append(num)
space_num.append(n-1)

def pull_forward():
    global score
    now_x, now_y = mid, mid
    space_d = 2
    lines = []

    # 2
    for num in space_num:
        for i in range(1, num + 1):
            now_x, now_y = now_x + dxs[space_d], now_y + dys[space_d]
            if arr[now_x][now_y]:
                lines.append(arr[now_x][now_y])
        space_d = (space_d - 1) % 4

    # 3
    while True:
        new_lines = []
        previous_num, count = -1, 1
        deleted = False

        for i, num in enumerate(lines):
            if num == previous_num:
                count += 1
            else:
                if count >= 4:
                    deleted = True
                    score += previous_num * count
                elif previous_num > 0:
                    new_lines.extend([previous_num] * count)
                previous_num, count = num, 1

        if count >= 4:
            deleted = True
            score += previous_num * count
        elif previous_num > 0:
            new_lines.extend([previous_num] * count)

        if not deleted:
            break
        lines = new_lines

    # 4
    new_lines = []
    previous_num, count = -1, 1
    for i, num in enumerate(lines):
        if num == previous_num:
            count += 1
        else:
            # 총 개수, 숫자의 크기
            if previous_num != -1:
                new_lines.append(count)
                new_lines.append(previous_num)
            previous_num, count = num, 1
    new_lines.append(count)
    new_lines.append(previous_num)

    if len(new_lines) > max_length:
        new_lines = new_lines[:max_length]

    return new_lines

def make_new_arr():
    global arr
    lines = pull_forward()
    len_lines, now_line = len(lines), 0
    arr = [[0] * n for _ in range(n)]

    now_x, now_y = mid, mid
    space_d = 2
    for num in space_num:
        for i in range(1, num + 1):
            if now_line < len_lines:
                now_x, now_y = now_x + dxs[space_d], now_y + dys[space_d]
                arr[now_x][now_y] = lines[now_line]
                now_line += 1
            else:
                return
        space_d = (space_d - 1) % 4

score = 0
for _ in range(m):
    d, p = list(map(int, input().split()))

    # 1
    for i in range(1, p + 1):
        new_x, new_y = mid + dxs[d] * i, mid + dys[d] * i
        score += arr[new_x][new_y]
        arr[new_x][new_y] = 0

    # 2, 3, 4
    make_new_arr()

print(score)