import copy
from queue import Queue

n, m = list(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
# 빈 칸 0, 방화벽 1, 불 2
blank_list = []
fire_list = []
selected = set()
max_blank_sum = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            blank_list.append((i, j))
        elif arr[i][j] == 2:
            fire_list.append((i, j))

x_list = [1, -1, 0, 0]
y_list = [0, 0, 1, -1]

def spread_fire(f_arr, f_queue):
    while not f_queue.empty():
        x, y = f_queue.get()
        for i in range(4):
            new_x = x + x_list[i]
            new_y = y + y_list[i]
            if 0 <= new_x < n and 0 <= new_y < m:
                if f_arr[new_x][new_y] == 0:
                    f_arr[new_x][new_y] = 2
                    f_queue.put((new_x, new_y))


def calc_fire():
    new_arr = copy.deepcopy(arr)
    for x, y in selected:
        new_arr[x][y] = 1

    fire_queue = Queue()
    for f in fire_list:
        fire_queue.put(f)
    spread_fire(new_arr, fire_queue)

    blank_sum = 0
    for i in range(n):
        for j in range(m):
            if new_arr[i][j] == 0:
                blank_sum += 1

    return blank_sum

def find(idx, cnt):
    global max_blank_sum

    if cnt == 3:
        blank_sum = calc_fire()
        max_blank_sum = max(max_blank_sum, blank_sum)
        return

    if idx == len(blank_list):
        return

    find(idx + 1, cnt)

    selected.add(blank_list[idx])
    find(idx + 1, cnt + 1)
    selected.remove(blank_list[idx])

find(0, 0)
print(max_blank_sum)