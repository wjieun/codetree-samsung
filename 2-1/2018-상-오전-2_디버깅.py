n, m, h = list(map(int, input().split()))

arr = [
    [False] * (n - 1)
    for _ in range(h)
]

for _ in range(m):
    a, b = list(map(int, input().split()))
    a, b = a - 1, b - 1

    arr[a][b] = True

all_line = []
for i in range(h):
    for j in range(n-1):
        if arr[i][j] == False:
            if j + 1 < n - 1 and arr[i][j + 1] == True:
                continue
            if j - 1 >= 0 and arr[i][j - 1] == True:
                continue
            all_line.append((i, j))

def can_go(pi):
    px, py = 0, pi

    while px < h:
        if py != n - 1 and arr[px][py] == True:
            py += 1
        elif py != 0 and arr[px][py-1] == True:
            py -= 1

        px += 1

    return pi == py

def can_all_go():
    all_go = True
    for person in range(n):
        if not can_go(person):
            all_go = False
            break
    return all_go

min_cnt = 4
def recursive(idx, cnt):
    global min_cnt

    if cnt < min_cnt:
        if can_all_go():
            min_cnt = cnt
            return
    else:
        return

    if idx >= len(all_line):
        return

    rx, ry = all_line[idx]

    recursive(idx + 1, cnt)

    arr[rx][ry] = True
    recursive(idx + 1, cnt + 1)
    arr[rx][ry] = False

recursive(0, 0)
print(min_cnt)