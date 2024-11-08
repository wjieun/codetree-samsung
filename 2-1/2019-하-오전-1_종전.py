n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

a_sum = [sum(a) for a in arr]
a_sum = sum(a_sum)

mul_x = [1, 1, -1, -1]
mul_y = [-1, 1, 1, -1]

def get_score(x, y, l, r):
    lines = {(x, y)}

    now_x, now_y = x, y
    for i, (length) in enumerate([l, r, l, r]):
        new_lines = [(now_x + k*mul_x[i], now_y + k*mul_y[i]) for k in range(1, length+1)]
        now_x, now_y = new_lines[-1]
        if not (0 <= now_x < n and 0 <= now_y < n):
            return float('inf')
        lines.update(new_lines)

    groups = [0] * 5

    # 2
    for i in range(0, x+l):
        for j in range(0, y+1):
            if (i, j) in lines:
                break
            else:
                groups[0] += arr[i][j]

    # 3
    for j in range(0, y-l+r):
        for i in range(n-1, x+l-1, -1):
            if (i, j) in lines:
                break
            else:
                groups[1] += arr[i][j]

    # 4
    for i in range(n-1, x+r, -1):
        for j in range(n-1, y-l+r-1, -1):
            if (i, j) in lines:
                break
            else:
                groups[2] += arr[i][j]

    # 5
    for j in range(n-1, y, -1):
        for i in range(0, x+r+1):
            if (i, j) in lines:
                break
            else:
                groups[3] += arr[i][j]

    groups[4] = a_sum - sum(groups)

    return max(groups) - min(groups)

min_sc = float('inf')
for i in range(n-2):
    for j in range(1, n-1):

        for l in range(1, n-1):
            for r in range(1, n-1):

                sc = get_score(i, j, l, r)
                min_sc = min(min_sc, sc)

print(min_sc)