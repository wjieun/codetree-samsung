n, m = list(map(int, input().split()))
matrix = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs = [0, 1, 0, -1]
dys = [-1, 0, 1, 0]

def in_range(a, b):
    if 0 <= a < n and 0 <= b < m:
        return True
    return False

max_sum = 0

def T_block(now_x, now_y):
    global max_sum
    rounds = list()
    for dx, dy in zip(dxs, dys):
        new_x, new_y = now_x + dx, now_y + dy
        if in_range(new_x, new_y):
            rounds.append((new_x, new_y))

    if len(rounds) == 3:
        block_sum = 0
        for bx, by in rounds + [(now_x, now_y)]:
            block_sum += matrix[bx][by]
        if block_sum > max_sum:
            max_sum = block_sum
    elif len(rounds) == 4:
        all_sum = 0
        for bx, by in rounds + [(now_x, now_y)]:
            all_sum += matrix[bx][by]
        for bx, by in rounds:
            block_sum = all_sum - matrix[bx][by]
            if block_sum > max_sum:
                max_sum = block_sum


def recursive(now_x, now_y, block, block_sum):
    global max_sum

    if len(block) == 4:
        if block_sum > max_sum:
            max_sum = block_sum
        return

    for dx, dy in zip(dxs, dys):
        new_x, new_y = now_x + dx, now_y + dy
        if in_range(new_x, new_y) and (new_x, new_y) not in block:
            new_block = block.union({(new_x, new_y)})
            recursive(new_x, new_y, new_block, block_sum + matrix[new_x][new_y])

for i in range(n):
    for j in range(m):
        recursive(i, j, {(i, j)}, matrix[i][j])
        T_block(i, j)

print(max_sum)