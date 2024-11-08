n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

def roll_right(now):
    r, c = len(now), len(now[0])
    new = [[0] * r for _ in range(c)]

    for i in range(r):
        for j in range(c):
            new[j][r - 1 - i] = now[i][j]

    return new

def roll_dough():
    global arr
    new_arr = [[arr[0]], arr[1:]]

    while len(new_arr) <= len(new_arr[-1]) - len(new_arr[0]):
        down_len = len(new_arr[0])
        up = new_arr[:-1]
        up.append(new_arr[-1][:down_len])
        up = roll_right(up)
        up.append(new_arr[-1][down_len:])
        new_arr = up

    arr = new_arr
    down_len = len(new_arr[-1])

    for a in arr:
        if len(a) < down_len:
            a.extend([0] * (down_len - len(a)))

def push_dough():
    global arr
    r, c = len(arr), len(arr[0])
    plus_arr = [[0] * c for _ in range(r)]

    for i in range(r):
        for j in range(c-1):
            a, b = arr[i][j], arr[i][j + 1]
            if a and b:
                d = abs(a - b) // 5
                if a > b:
                    plus_arr[i][j] -= d
                    plus_arr[i][j + 1] += d
                elif a < b:
                    plus_arr[i][j] += d
                    plus_arr[i][j + 1] -= d

    for i in range(r-1):
        for j in range(c):
            a, b = arr[i][j], arr[i + 1][j]
            if a and b:
                d = abs(a - b) // 5
                if a > b:
                    plus_arr[i][j] -= d
                    plus_arr[i + 1][j] += d
                elif a < b:
                    plus_arr[i][j] += d
                    plus_arr[i + 1][j] -= d

    new_arr = []
    for j in range(c):
        for i in range(r-1, -1, -1):
            if arr[i][j]:
                new_arr.append(arr[i][j] + plus_arr[i][j])

    arr = new_arr

def roll_dough_twice():
    global arr

    # once
    mid = n // 2
    new_arr = [list(reversed(arr[:mid])), arr[mid:]]

    # twice
    mid = mid // 2
    up = [a[:mid] for a in new_arr]
    up = roll_right(roll_right(up))
    down = [a[mid:] for a in new_arr]
    up.extend(down)
    arr = up

turn = 0
while True:
    if max(arr) - min(arr) <= k:
        break

    turn += 1

    # 1
    min_num = min(arr)
    for i in range(n):
        if arr[i] == min_num:
            arr[i] += 1

    roll_dough()  # 2
    push_dough()  # 3
    roll_dough_twice()  # 4
    push_dough()  # 5

print(turn)