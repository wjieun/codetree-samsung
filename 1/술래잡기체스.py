import copy

arr = [
    [0 for _ in range(4)]
    for _ in range(4)
]
thief_dir = [-1 for _ in range(17)]
thief_x = [-1 for _ in range(17)]
thief_y = [-1 for _ in range(17)]

for i in range(4):
    line = list(map(int, input().split()))
    for j in range(0, len(line), 2):
        p, d = line[j], line[j + 1]
        if i == 0 and j == 0:
            arr[0][0] = 0
            thief_dir[0] = d - 1
            thief_x[0], thief_y[0] = 0, 0
        else:
            arr[i][j // 2] = p
            thief_dir[p] = d - 1
            thief_x[p], thief_y[p] = i, j // 2

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
x_list = [-1, -1, 0, 1, 1, 1, 0, -1]
y_list = [0, -1, -1, -1, 0, 1, 1, 1]

def in_range(x, y):
    return 0 <= x < 4 and 0 <= y < 4

def move_all_thief():
    for i in range(1, 17):
        x, y, d = thief_x[i], thief_y[i], thief_dir[i]
        d = d - 1

        if x != -1 and y != -1:
            while True:
                d = (d + 1) % 8
                thief_dir[i] = d
                new_x, new_y = x + x_list[d], y + y_list[d]

                if in_range(new_x, new_y):
                    if arr[new_x][new_y] != 0:
                        break

            if arr[new_x][new_y] != -1:
                thief_x[arr[new_x][new_y]] = x
                thief_y[arr[new_x][new_y]] = y

            arr[x][y] = arr[new_x][new_y]
            arr[new_x][new_y] = i

            thief_x[i], thief_y[i] = new_x, new_y

def move_it(x, y):
    thief_x[arr[x][y]], thief_y[arr[x][y]] = -1, -1
    thief_dir[0] = thief_dir[arr[x][y]]
    arr[x][y] = 0
    arr[thief_x[0]][thief_y[0]] = -1
    thief_x[0], thief_y[0] = x, y

def get_score():
    score = 0
    for i in range(1, 17):
        if thief_x[i] == -1 and thief_y[i] == -1:
            score += i
    return score


max_score = 0
def find():
    global max_score, arr, thief_x, thief_y, thief_dir

    move_all_thief()

    it_can_go = []
    it_x, it_y, it_d = thief_x[0], thief_y[0], thief_dir[0]
    while True:
        new_it_x, new_it_y = it_x + x_list[it_d], it_y + y_list[it_d]
        if in_range(new_it_x, new_it_y):
            if arr[new_it_x][new_it_y] > 0:
                it_can_go.append((new_it_x, new_it_y))
            it_x, it_y = new_it_x, new_it_y
        else:
            break

    if len(it_can_go):
        for x, y in it_can_go:
            origin_arr = copy.deepcopy(arr)
            origin_x = thief_x.copy()
            origin_y = thief_y.copy()
            origin_dir = thief_dir.copy()

            move_it(x, y)
            find()

            arr = origin_arr
            thief_x = origin_x
            thief_y = origin_y
            thief_dir = origin_dir
    else:
        max_score = max(max_score, get_score())
        return

find()
print(max_score)