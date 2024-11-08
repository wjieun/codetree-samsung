move_arr = list(map(int, input().split()))

final_num = 40
map_arr = [
    [2, 4, 6, 8, 10],
    [12, 14, 16, 18, 20],
    [13, 16, 19],
    [22, 24, 26, 28, 30],
    [22, 24],
    [32, 34, 36, 38],
    [28, 27, 26],
    [25, 30, 35],
    [40]
]

# 앞 검정, 뒤 빨강
map_dict = {0: [1, 2], 1: [3, 4], 2: [7], 3: [5, 6], 4: [7], 5: [8], 6: [7], 7: [8], 8: [-1]}
token_list = [[0, -1] for _ in range(4)]
selected = []

def move(token_num, move_num):
    token_x, token_y = token_list[token_num]

    for m in range(move_num):
        if (token_x, token_y) == (-2, -2):
            break

        if token_y == len(map_arr[token_x]) - 1:
            if len(map_dict[token_x]) == 2:
                if m == 0:
                    token_list[token_num] = [map_dict[token_x][1], 0]
                else:
                    token_list[token_num] = [map_dict[token_x][0], 0]
            else:
                if map_dict[token_x][0] == -1:
                    token_list[token_num] = [-2, -2]
                else:
                    token_list[token_num] = [map_dict[token_x][0], 0]
        else:
            token_list[token_num][1] += 1
        token_x, token_y = token_list[token_num]

    if (token_x, token_y) == (-2, -2):
        return 0
    if token_list.count([token_x, token_y]) > 1:
        return -1
    return map_arr[token_x][token_y]

def can_go(token_num):
    token_x, token_y = token_list[token_num]
    return False if (token_x, token_y) == (-2, -2) else True

max_score = 0
score = 0
def find(idx, cnt):
    global max_score, score

    if cnt == 10:
        max_score = max(max_score, score)
        return

    for i in range(4):
        if can_go(i):
            origin = token_list[i].copy()
            new_score = move(i, move_arr[idx])
            if new_score >= 0:
                score += new_score
                find(idx + 1, cnt + 1)
                score -= new_score
            token_list[i] = origin


find(0, 0)
print(max_score)