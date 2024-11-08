from copy import deepcopy

N, M, K = list(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(N)
]

people = []
for _ in range(M):
    x, y = list(map(int, input().split()))
    people.append((x-1, y-1))


exit_x, exit_y = list(map(int, input().split()))
exit_x, exit_y = exit_x - 1, exit_y - 1

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(a, b):
    return 0 <= a < N and 0 <= b < N

def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def rotate(r):
    global arr, people, exit_x, exit_y

    size, bx, by = r

    new_arr = deepcopy(arr)
    # box
    for i in range(size):
        for j in range(size):
            temp = arr[bx + i][by + j]
            if temp > 0:
                new_arr[bx + j][by + size - 1 - i] = temp - 1
            else:
                new_arr[bx + j][by + size - 1 - i] = temp
    arr = new_arr

    # people
    for pi, (px, py) in enumerate(people):
        if bx <= px < bx + size and by <= py < by + size:
            i, j = px - bx, py - by
            people[pi] = (bx + j, by + size - 1 - i)

    # exit
    if bx <= exit_x < bx + size and by <= exit_y < by + size:
        i, j = exit_x - bx, exit_y - by
        exit_x, exit_y = (bx + j, by + size - 1 - i)

move = 0
for _ in range(K):
    # 1
    new_people = []
    for pi, (px, py) in enumerate(people):
        can_move = False
        now_dis = get_distance(px, py, exit_x, exit_y)

        for dx, dy in zip(dxs, dys):
            new_x, new_y = px + dx, py + dy
            if in_range(new_x, new_y) and arr[new_x][new_y] == 0:
                new_dis = get_distance(new_x, new_y, exit_x, exit_y)
                if new_dis < now_dis:
                    move += 1
                    can_move = True
                    if (new_x, new_y) != (exit_x, exit_y):
                        new_people.append((new_x, new_y))
                    break

        if not can_move:
            new_people.append((px, py))

    people = new_people

    if len(people) == 0:
        break

    # 2
    min_result = (float('inf'), float('inf'), float('inf'))
    for px, py in people:
        x_diff, y_diff = abs(px - exit_x), abs(py - exit_y)
        box_diff = max(x_diff, y_diff)

        box_x = max(0, max(px, exit_x) - box_diff)
        box_y = max(0, max(py, exit_y) - box_diff)

        result = (box_diff + 1, box_x, box_y)
        min_result = min(min_result, result)

    rotate(min_result)

print(move)
print(exit_x + 1, exit_y + 1)