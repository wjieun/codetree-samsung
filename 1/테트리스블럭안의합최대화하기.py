n, m = list(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

x_list = [1, -1, 0, 0]
y_list = [0, 0, 1, -1]
selected = set()
max_sum_blocks = 0

def find():
    global max_sum_blocks

    if len(selected) == 4:
        sum_blocks = sum([arr[x][y] for x, y in selected])
        max_sum_blocks = max(max_sum_blocks, sum_blocks)
        return

    for s in selected:
        x, y = s
        for i in range(4):
            new_x = x + x_list[i]
            new_y = y + y_list[i]
            if 0 <= new_x < n and 0 <= new_y < m and (new_x, new_y) not in selected:
                selected.add((new_x, new_y))
                find()
                selected.remove((new_x, new_y))

for i in range(n):
    for j in range(m):
        selected.add((i, j))
        find()
        selected.remove((i, j))

print(max_sum_blocks)