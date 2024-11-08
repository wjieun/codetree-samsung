n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

x_list = [-2, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 2]
y_list = [0, -1, 0, 1, -2, -1, 1, 2, -1, 0, 1, 0]
p_list = [
    [2, 10, 7, 1, 5, -1, 0, 0, 10, 7, 1, 2],
    [0, 1, 0, 1, 2, 7, 7, 2, 10, -1, 10, 5],
    [2, 1, 7, 10, 0, 0, -1, 5, 1, 7, 10, 2],
    [5, 10, -1, 10, 2, 7, 7, 2, 1, 0, 1, 0]
]

move_x = [0, 1, 0, -1]
move_y = [-1, 0, 1, 0]

move_number = [n]
for i in range(n - 1, 0, -1):
    move_number.insert(0, i)
    move_number.insert(0, i)
move_cnt = [0 for _ in range(len(move_number))]
move_idx = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

out_range_dust_sum = 0
now_x, now_y = n // 2, n // 2
for _ in range(n * n - 1):
    d = move_idx % 4
    new_x, new_y = now_x + move_x[d], now_y + move_y[d]
    original_dust = arr[new_x][new_y]
    dust = original_dust

    rest_x, rest_y = -1, -1
    for i in range(12):
        dust_x, dust_y = new_x + x_list[i], new_y + y_list[i]
        dust_p = p_list[d][i]

        if dust_p == -1:
            rest_x, rest_y = dust_x, dust_y
        else:
            new_dust = int(original_dust * (dust_p / 100))
            if in_range(dust_x, dust_y):
                arr[dust_x][dust_y] += new_dust
            else:
                out_range_dust_sum += new_dust
            dust -= new_dust

    if in_range(rest_x, rest_y):
        arr[rest_x][rest_y] += dust
    else:
        out_range_dust_sum += dust
    arr[new_x][new_y] = 0

    move_cnt[move_idx] += 1

    # 방향 전환
    now_x, now_y = new_x, new_y
    if move_cnt[move_idx] == move_number[move_idx]:
        move_idx += 1

print(out_range_dust_sum)