n = int(input())
# 시작점 (x, y), 방향 d(오위왼아), 차수 g
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

x_list = [0, -1, 0, 1]
y_list = [1, 0, -1, 0]
all_point = set()

for x, y, d, g in arr:
    point_list = [(x, y), (x + x_list[d], y + y_list[d])]
    for _ in range(g):
        for i in range(len(point_list) - 2, -1, -1):
            x_diff = point_list[i + 1][0] - point_list[i][0]
            y_diff = point_list[i + 1][1] - point_list[i][1]
            ori_d = x_list.index(x_diff) if abs(x_diff) == 1 else y_list.index(y_diff)
            new_d = (ori_d + 1) % 4

            last_point_x, last_point_y = point_list[-1]
            new_point_x = last_point_x + x_list[new_d]
            new_point_y = last_point_y + y_list[new_d]
            if 0 <= new_point_x <= 100 and 0 <= new_point_y <= 100:
                point_list.append((new_point_x, new_point_y))
    all_point = all_point.union(set(point_list))

square_x_list = [0, 1, 1]
square_y_list = [1, 1, 0]
def check_square(now_x, now_y):
    global all_point

    check = True
    for k in range(3):
        new_x = now_x + square_x_list[k]
        new_y = now_y + square_y_list[k]

        if (new_x, new_y) not in all_point:
            check = False

    return check


square_sum = 0
for i in range(101):
    for j in range(101):
        if (i, j) in all_point:
            if check_square(i, j):
                square_sum += 1

print(square_sum)