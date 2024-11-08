n, m, q = list(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

for _ in range(q):
    # d: 0 시계, 1 반시계
    x, d, k = list(map(int, input().split()))

    # rotate
    for i in range(n):
        if (i + 1) % x == 0:
            if d == 0:
                for _ in range(k):
                    arr[i].insert(0, arr[i].pop())
            else:
                for _ in range(k):
                    arr[i].append(arr[i].pop(0))

    # delete
    delete = set()
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                next_i, next_j = (i + 1) % n, (j + 1) % m
                if i < n - 1 and arr[i][j] == arr[next_i][j]:
                    delete.update({(i, j), (next_i, j)})
                if arr[i][j] == arr[i][next_j]:
                    delete.update({(i, j), (i, next_j)})

    if len(delete):
        for dx, dy in delete:
            arr[dx][dy] = 0
    else:
        all_sum, all_len = 0, 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] > 0:
                    all_sum += arr[i][j]
                    all_len += 1

        all_avg = all_sum // all_len
        for i in range(n):
            for j in range(m):
                if arr[i][j] > 0:
                    if arr[i][j] > all_avg:
                        arr[i][j] -= 1
                    elif arr[i][j] < all_avg:
                        arr[i][j] += 1

a_sum = [sum(a) for a in arr]
print(sum(a_sum))