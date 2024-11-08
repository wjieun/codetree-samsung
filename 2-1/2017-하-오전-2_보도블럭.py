n, L = list(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

count = 0

# row
for i in range(n):
    built = [False] * n
    can = False
    j = 0

    while j < n:
        if j == n - 1:
            can = True
            break

        diff = abs(arr[i][j] - arr[i][j + 1])
        if diff > 1: break
        elif diff == 0: j += 1
        elif diff == 1:
            if arr[i][j] > arr[i][j + 1]:
                can_go = True
                for k in range(j + 1, j + 1 + L):
                    if k >= n or arr[i][k] != arr[i][j + 1]:
                        can_go = False
                        break
                    built[k] = True

                if can_go: j = j + L
                else: break
            else:
                can_go = True
                for k in range(j, j - L, -1):
                    if k < 0 or built[k] or arr[i][k] != arr[i][j]:
                        can_go = False
                        break
                    built[k] = True

                if can_go: j += 1
                else: break

    if can:
        count += 1

# col
for j in range(n):
    built = [False] * n
    can = False
    i = 0

    while i < n:
        if i == n - 1:
            can = True
            break

        diff = abs(arr[i][j] - arr[i + 1][j])
        if diff > 1: break
        elif diff == 0: i += 1
        elif diff == 1:
            if arr[i][j] > arr[i + 1][j]:
                can_go = True
                for k in range(i + 1, i + 1 + L):
                    if k >= n or arr[k][j] != arr[i + 1][j]:
                        can_go = False
                        break
                    built[k] = True

                if can_go: i = i + L
                else: break
            else:
                can_go = True
                for k in range(i, i - L, -1):
                    if k < 0 or built[k] or arr[k][j] != arr[i][j]:
                        can_go = False
                        break
                    built[k] = True

                if can_go: i += 1
                else: break

    if can:
        count += 1

print(count)