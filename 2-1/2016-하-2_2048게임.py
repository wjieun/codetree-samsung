from copy import deepcopy

n = int(input())

init_arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def push(arr, d):
    new_arr = [[0] * n for _ in range(n)]

    if d == 0: # 아래
        for j in range(n):
            i = n-1
            now = n-1
            while i >= 0:
                if arr[i][j] != 0:
                    if i != 0:
                        can_sum = False
                        for k in range(i-1, -1, -1):
                            if arr[k][j]:
                                if arr[i][j] == arr[k][j]:
                                    can_sum = True
                                break

                        if can_sum:
                            new_arr[now][j] = arr[i][j] * 2
                            i = k - 1
                        else:
                            new_arr[now][j] = arr[i][j]
                            i = k
                        now -= 1
                    else:
                        new_arr[now][j] = arr[i][j]
                        i -= 1
                else:
                    i -= 1
    elif d == 1:  # 위
        for j in range(n):
            i = 0
            now = 0
            while i < n:
                if arr[i][j] != 0:
                    if i != n-1:
                        can_sum = False
                        for k in range(i + 1, n, 1):
                            if arr[k][j]:
                                if arr[i][j] == arr[k][j]:
                                    can_sum = True
                                break

                        if can_sum:
                            new_arr[now][j] = arr[i][j] * 2
                            i = k + 1
                        else:
                            new_arr[now][j] = arr[i][j]
                            i = k
                        now += 1
                    else:
                        new_arr[now][j] = arr[i][j]
                        i += 1
                else:
                    i += 1
    if d == 2:  # 오른쪽
        for i in range(n):
            j = n - 1
            now = n - 1
            while j >= 0:
                if arr[i][j] != 0:
                    if j != 0:
                        can_sum = False
                        for k in range(j - 1, -1, -1):
                            if arr[i][k]:
                                if arr[i][j] == arr[i][k]:
                                    can_sum = True
                                break

                        if can_sum:
                            new_arr[i][now] = arr[i][j] * 2
                            j = k - 1
                        else:
                            new_arr[i][now] = arr[i][j]
                            j = k
                        now -= 1
                    else:
                        new_arr[i][now] = arr[i][j]
                        j -= 1
                else:
                    j -= 1
    if d == 3:  # 왼쪽
        for i in range(n):
            j = 0
            now = 0
            while j < n:
                if arr[i][j] != 0:
                    if j != n-1:
                        can_sum = False
                        for k in range(j + 1, n, 1):
                            if arr[i][k]:
                                if arr[i][j] == arr[i][k]:
                                    can_sum = True
                                break

                        if can_sum:
                            new_arr[i][now] = arr[i][j] * 2
                            j = k + 1
                        else:
                            new_arr[i][now] = arr[i][j]
                            j = k
                        now += 1
                    else:
                        new_arr[i][now] = arr[i][j]
                        j += 1
                else:
                    j += 1

    return new_arr

max_block = 0
def recursive(arr, count):
    global max_block

    if count == 5:
        max_a = max(max(a) for a in arr)
        max_block = max(max_a, max_block)
        return

    for direction in range(4):
        recursive(push(arr, direction), count + 1)

recursive(init_arr, 0)
print(max_block)