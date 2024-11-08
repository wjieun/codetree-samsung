n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_squre(x, y, k, l):
    return in_range(x - k, y + k) and in_range(x - k - l, y + k - l) and in_range(x - l, y - l)

def get_border(x, y, k, l):
    x_list = [-1, -1, 1, 1]
    y_list = [1, -1, -1, 1]
    move_nums = [k, l, k, l]

    border = [
        [False for _ in range(n)]
        for _ in range(n)
    ]

    for move_x, move_y, move_num in zip(x_list,y_list, move_nums):
        for _ in range(move_num):
            x, y = x + move_x, y + move_y
            border[x][y] = True

    return border

def get_score(x, y, k, l):
    ppl = [0 for _ in range(5)]
    border = get_border(x, y, k, l)

    for i in range(x - l):
        for j in range(y + k - l + 1):
            if border[i][j]:
                break
            ppl[0] += arr[i][j]

    for i in range(x - l, n):
        for j in range(y):
            if border[i][j]:
                break
            ppl[1] += arr[i][j]

    for i in range(x - k + 1):
        for j in range(n - 1, y + k - l, -1):
            if border[i][j]:
                break
            ppl[2] += arr[i][j]

    for i in range(x - k + 1, n):
        for j in range(n - 1, y - 1, -1):
            if border[i][j]:
                break
            ppl[3] += arr[i][j]

    ppl[4] = sum([sum(a) for a in arr]) - sum(ppl)

    return max(ppl) - min(ppl)

min_diff = float('inf')

for i in range(n):
    for j in range(n):
        for k in range(1, n):
            for l in range(1, n):
                if can_squre(i, j, k, l):
                    diff = get_score(i, j, k, l)
                    min_diff = min(min_diff, diff)

print(min_diff)