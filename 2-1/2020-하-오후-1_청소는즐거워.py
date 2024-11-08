n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

move_num = []
for i in range(n-1):
    move_num.extend([i+1] * 2)
move_num.append(n-1)

# 왼아오위
d = 0
dxs = [0, 1, 0, -1]
dys = [-1, 0, 1, 0]

now_x, now_y = n // 2, n // 2
out_dust = 0

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

def move_dust():
    global out_dust

    left = d
    right = (d + 2) % 4
    top = (d - 1) % 4
    bottom = (d + 1) % 4

    moved_dust = 0
    now_dust = arr[now_x][now_y]

    # 5%
    new_x, new_y = now_x + dxs[left]*2, now_y + dys[left]*2
    dust = int(now_dust * 0.05)
    moved_dust += dust
    if in_range(new_x, new_y):
        arr[new_x][new_y] += dust
    else:
        out_dust += dust

    # 10%, 7%, 1%, 2%
    for d1 in [top, bottom]:
        init_x, init_y = now_x + dxs[d1], now_y + dys[d1]

        for d2, pct in zip([-1, left, right, d1], [0.07, 0.1, 0.01, 0.02]):
            if d2 == -1:
                new_x, new_y = init_x, init_y
            else:
                new_x, new_y = init_x + dxs[d2], init_y + dys[d2]

            dust = int(now_dust * pct)
            moved_dust += dust

            if in_range(new_x, new_y):
                arr[new_x][new_y] += dust
            else:
                out_dust += dust

    # a%
    new_x, new_y = now_x + dxs[left], now_y + dys[left]
    dust = now_dust - moved_dust
    if in_range(new_x, new_y):
        arr[new_x][new_y] += dust
    else:
        out_dust += dust

    # delete now
    arr[now_x][now_y] = 0

for num in move_num:
    for _ in range(num):
        now_x, now_y = now_x + dxs[d], now_y + dys[d]
        move_dust()
    d = (d + 1) % 4

print(out_dust)
