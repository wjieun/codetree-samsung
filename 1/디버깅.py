n, m, h = list(map(int, input().split()))

line = [
    [False for _ in range(n-1)]
    for _ in range(h)
]
min_line_cnt = float('inf')

for _ in range(m):
    a, b = list(map(int, input().split()))
    line[a - 1][b - 1] = True

def calc_destination():
    for person in range(n):
        cur_x, cur_y = 0, person

        while True:
            if cur_x == h:
                break

            if cur_y < n - 1:
                if line[cur_x][cur_y]:
                    cur_y += 1
                    cur_x += 1
                    continue
            if cur_y - 1 >= 0:
                if line[cur_x][cur_y - 1]:
                    cur_y -= 1
                    cur_x += 1
                    continue

            cur_x += 1

        if person != cur_y:
            return False

    return True

def find_can_line():
    can_line = []
    for i in range(h):
        for j in range(n - 1):
            if j - 1 >= 0:
                if line[i][j - 1]:
                    continue
            if not line[i][j]:
                can_line.append((i, j))
    return can_line

def is_can_line(i, j):
    if j - 1 >= 0:
        if line[i][j - 1]:
            return False
    if line[i][j]:
        return False
    return True

def get_line_cnt():
    global m
    return sum([sum(l) for l in line]) - m

def find(idx, cnt):
    global min_line_cnt

    if cnt > 3 or cnt >= min_line_cnt:
        return

    if calc_destination():
        line_cnt = get_line_cnt()
        min_line_cnt = min(min_line_cnt, line_cnt)
        return

    if idx == len(can_line_list):
        return

    find(idx + 1, cnt)

    x, y = can_line_list[idx]
    line[x][y] = True
    find(idx + 1, cnt + 1)
    line[x][y] = False

can_line_list = find_can_line()
find(0, 0)

if min_line_cnt == float('inf'):
    print(-1)
else:
    print(min_line_cnt)