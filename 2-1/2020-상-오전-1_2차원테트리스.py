k = int(input())

blocks = {
    1: [(0, 0)],
    2: [(0, 0), (0, 1)],
    3: [(0, 0), (1, 0)]
}

red_arr = [
    [0] * 6
    for _ in range(4)
]

yel_arr = [
    [0] * 4
    for _ in range(6)
]

score = 0
for _ in range(k):
    t, x, y = list(map(int, input().split()))

    # put yellow
    min_x = 5
    previous_y = -1
    for dx, dy in blocks[t]:
        new_y = y + dy
        if new_y != previous_y:
            for i in range(2, 6):
                if yel_arr[i][new_y]:
                    min_x = min(i-1, min_x)
            previous_y = new_y

    for dx, dy in blocks[t]:
        new_x = min_x - dx
        new_y = y + dy
        yel_arr[new_x][new_y] = 1

    # put red
    min_y = 5
    previous_x = -1
    for dx, dy in blocks[t]:
        new_x = x + dx
        if new_x != previous_x:
            for j in range(2, 6):
                if red_arr[new_x][j]:
                    min_y = min(j - 1, min_y)
            previous_x = new_x

    for dx, dy in blocks[t]:
        new_x = x + dx
        new_y = min_y - dy
        red_arr[new_x][new_y] = 1

    # get score yellow
    for i in range(6):
        if all(yel_arr[i]):
            score += 1
            yel_arr.pop(i)
            yel_arr.insert(0, [0] * 4)

    remove_num = 0
    for i in range(2):
        if any(yel_arr[i]):
            remove_num += 1

    for i in range(remove_num):
        yel_arr.pop()
        yel_arr.insert(0, [0] * 4)

    # get score red:
    for j in range(6):
        if all(red_arr[i][j] for i in range(4)):
            score += 1
            for i in range(4):
                red_arr[i].pop(j)
                red_arr[i].insert(0, 0)

    remove_num = 0
    for j in range(2):
        if any(red_arr[i][j] for i in range(4)):
            remove_num += 1

    for i in range(remove_num):
        for i in range(4):
            red_arr[i].pop()
            red_arr[i].insert(0, 0)

print(score)

y_sum = sum(sum(y) for y in yel_arr)
r_sum = sum(sum(r) for r in red_arr)
print(y_sum + r_sum)