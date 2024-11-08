import copy

n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

def put_flour():
    min_flour = min(arr)
    for i in range(len(arr)):
        if arr[i] == min_flour:
            arr[i] += 1

def roll(d_arr):
    new_d_arr = [
        [0 for _ in range(len(d_arr))]
        for _ in range(len(d_arr[0]))
    ]

    for i in range(len(d_arr)):
        for j in range(len(d_arr[0])):
            new_d_arr[j][len(d_arr) - 1 - i] = d_arr[i][j]

    return new_d_arr

def roll_dough():
    global arr
    if len(arr) == 1:
        return [arr[0]]
    if len(arr) == 2:
        return [[arr[0]], [arr[1]]]
    else:
        up_arr = [[arr[0]]]
        down_arr = arr[1:].copy()

        while len(up_arr) + 1 <= len(down_arr) - len(up_arr[0]):
            up_arr.append(down_arr[:len(up_arr[0])])
            down_arr = down_arr[len(up_arr[0]):]

            up_arr = roll(up_arr)

        for up in up_arr:
            while len(up) < len(down_arr):
                up.append(0)

        up_arr.append(down_arr)
        return up_arr

def push_dough(d_arr):
    new_d_arr = copy.deepcopy(d_arr)
    for i in range(len(d_arr)):
        for j in range(len(d_arr[i])):
            if i != len(d_arr) - 1:
                if d_arr[i + 1][j] and d_arr[i][j]:
                    d = abs(d_arr[i + 1][j] - d_arr[i][j]) // 5
                    if d_arr[i + 1][j] > d_arr[i][j]:
                        new_d_arr[i + 1][j] -= d
                        new_d_arr[i][j] += d
                    elif d_arr[i + 1][j] < d_arr[i][j]:
                        new_d_arr[i + 1][j] += d
                        new_d_arr[i][j] -= d

            if j != len(d_arr[i]) - 1:
                if d_arr[i][j + 1] and d_arr[i][j]:
                    d = abs(d_arr[i][j + 1] - d_arr[i][j]) // 5
                    if d_arr[i][j + 1] > d_arr[i][j]:
                        new_d_arr[i][j + 1] -= d
                        new_d_arr[i][j] += d
                    elif d_arr[i][j + 1] < d_arr[i][j]:
                        new_d_arr[i][j + 1] += d
                        new_d_arr[i][j] -= d

    new_arr = []
    for j in range(len(d_arr[0])):
        for i in range(len(d_arr) - 1, -1, -1):
            if new_d_arr[i][j]:
                new_arr.append(new_d_arr[i][j])
    return new_arr

def roll_twice_dough(d_arr):
    mid = len(d_arr) // 2
    once = roll([d_arr[:mid]])
    once = roll(once)
    once.append(d_arr[mid:])

    mid = mid // 2
    twice = roll([a[:mid] for a in once])
    twice = roll(twice)
    twice.extend([a[mid:] for a in once])

    return twice

turn = 0
while True:
    turn += 1
    put_flour()
    rolled_dough = roll_dough()
    pushed_dough = push_dough(rolled_dough)
    rolled_twice_dough = roll_twice_dough(pushed_dough)
    arr = push_dough(rolled_twice_dough)
    if max(arr) - min(arr) <= k:
        break

print(turn)