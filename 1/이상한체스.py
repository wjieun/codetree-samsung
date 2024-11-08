n, m = list(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

x_list = [-1, 0, 1, 0]
y_list = [0, 1, 0, -1]
chess_dict = {1: [0], 2: [1, 3], 3: [0, 1], 4: [0, 1, 3], 5: [0, 1, 2, 3]}
chess_coord = []
horse_list = []

for i in range(n):
    for j in range(m):
        if 1 <= arr[i][j] <= 5:
            chess_coord.append((i, j))
            horse_list.append(arr[i][j])

selected = []
min_blank = float('inf')

def calc_blank():
    global n, m

    colored_arr = [
        [False for _ in range(m)]
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                colored_arr[i][j] = True

    for i in range(len(horse_list)):
        dir_num = selected[i]
        c = horse_list[i]
        dir_list = chess_dict[c]

        for d in dir_list:
            x, y = chess_coord[i]
            new_d = (d + dir_num) % 4
            while True:
                new_x = x + x_list[new_d]
                new_y = y + y_list[new_d]

                if 0 <= new_x < n and 0 <= new_y < m and arr[new_x][new_y] != 6:
                    colored_arr[new_x][new_y] = True
                    x, y = new_x, new_y
                else:
                    break

    return n * m - sum([sum(ca) for ca in colored_arr]), colored_arr

def find():
    global min_blank

    if len(selected) == len(horse_list):
        blank, colored = calc_blank()
        min_blank = min(min_blank, blank)
        return

    for i in range(4):
        selected.append(i)
        find()
        selected.pop()

find()
print(min_blank)