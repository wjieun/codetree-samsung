k = int(input())

h_list = [1, 1, 2]
w_list = [1, 2, 1]

arr = [
    [False for _ in range(10)]
    for _ in range(10)
]

def put_blocks():
    global arr, h_list, w_list
    t, x, y = list(map(int, input().split()))
    t = t - 1

    min_j = 9
    for i in range(x, x + h_list[t]):
        for j in range(4, 10):
            if arr[i][j]:
                min_j = min(min_j, j - 1)
                break

    min_i = 9
    for j in range(y, y + w_list[t]):
        for i in range(4, 10):
            if arr[i][j]:
                min_i = min(min_i, i - 1)
                break

    for i in range(x, x + h_list[t]):
        for j in range(min_j, min_j - w_list[t], -1):
            arr[i][j] = True

    for j in range(y, y + w_list[t]):
        for i in range(min_i, min_i - h_list[t], -1):
            arr[i][j] = True

score = 0
def delete_dark():
    global arr, score

    i = 9
    while i > 3:
        if all(arr[i][:4]):
            score += 1
            for i2 in range(i - 1, 3, -1):
                for j in range(4):
                    arr[i2 + 1][j] = arr[i2][j]
            i += 1
        i -= 1

    j = 9
    while j > 3:
        all_True = True
        for i in range(4):
            if not arr[i][j]:
                all_True = False
                break

        if all_True:
            score += 1
            for j2 in range(j - 1, 3, -1):
                for i in range(4):
                    arr[i][j2 + 1] = arr[i][j2]
            j += 1
        j -= 1

def delete_light():
    global arr

    True_cnt = 0
    for i in range(4, 6):
        any_True = False
        for j in range(4):
            if arr[i][j]:
                any_True = True
                break
        if any_True:
            True_cnt += 1

    for _ in range(True_cnt):
        for i in range(8, 2, -1):
            for j in range(4):
                arr[i + 1][j] = arr[i][j]

    True_cnt = 0
    for j in range(4, 6):
        any_True = False
        for i in range(4):
            if arr[i][j]:
                any_True = True
                break
        if any_True:
            True_cnt += 1

    for _ in range(True_cnt):
        for j in range(8, 2, -1):
            for i in range(4):
                arr[i][j + 1] = arr[i][j]

def count_blocks():
    red = 0
    for j in range(6, 10):
        for i in range(4):
            if arr[i][j]:
                red += 1

    yellow = 0
    for i in range(6, 10):
        for j in range(4):
            if arr[i][j]:
                yellow += 1

    return red + yellow


for _ in range(k):
    put_blocks()
    delete_dark()
    delete_light()


print(score)
print(count_blocks())