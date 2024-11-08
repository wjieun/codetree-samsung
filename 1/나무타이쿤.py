n, m = list(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
move_rule = [
    list(map(int, input().split()))
    for _ in range(m)
] # 이동 방향(1~8 → ↗ ↑ ↖ ← ↙ ↓ ↘), 이동 칸 수

x_list = (0, -1, -1, -1, 0, 1, 1, 1)
y_list = (1, 1, 0, -1, -1, -1, 0, 1)

nutrition = { (n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1) }

for move in move_rule:
    d = move[0] - 1
    p = move[1]
    new_nutrition = set()

    # 1
    for nut in nutrition:
        x, y = nut
        new_x = (x + x_list[d] * p) % n
        new_y = (y + y_list[d] * p) % n
        new_nutrition.add((new_x, new_y))
    nutrition = new_nutrition

    # 2
    for nut in nutrition:
        x, y = nut
        arr[x][y] += 1

    # 3
    for nut in nutrition:
        x, y = nut
        for i in range(1, 8, 2):
            new_x = x + x_list[i]
            new_y = y + y_list[i]
            if 0 <= new_x < n and 0 <= new_y < n:
                if arr[new_x][new_y] >= 1:
                    arr[x][y] += 1

    # 4
    new_nutrition = set()
    for i in range(n):
        for j in range(n):
            if (i, j) not in nutrition and arr[i][j] >= 2:
                arr[i][j] -= 2
                new_nutrition.add((i, j))
    nutrition = new_nutrition

sum_height = sum([sum(h) for h in arr])
print(sum_height)