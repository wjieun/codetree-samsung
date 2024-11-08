n, m, k = list(map(int, input().split()))
arr = [
    [5 for _ in range(n)]
    for _ in range(n)
]
plus_arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
virus_arr = [
    [[] for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    r, c, a = list(map(int, input().split()))
    virus_arr[r - 1][c - 1].append(a)

x_list = [1, 1, 1, 0, 0, -1, -1, -1]
y_list = [1, 0, -1, 1, -1, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for _ in range(k):
    for i in range(n):
        for j in range(n):
            sorted_virus = sorted(virus_arr[i][j])
            alive_virus = []
            dead_virus = []

            # 1
            for virus in sorted_virus:
                if arr[i][j] >= virus:
                    arr[i][j] -= virus
                    alive_virus.append(virus + 1)
                else:
                    dead_virus.append(virus)

            # 2
            arr[i][j] += sum([virus // 2 for virus in dead_virus])
            virus_arr[i][j] = alive_virus

    # 3
    for i in range(n):
        for j in range(n):
            for virus in virus_arr[i][j]:
                if virus % 5 == 0:
                    for d in range(8):
                        new_i = i + x_list[d]
                        new_j = j + y_list[d]

                        if in_range(new_i, new_j):
                            virus_arr[new_i][new_j].append(1)

    # 4
    for i in range(n):
        for j in range(n):
            arr[i][j] += plus_arr[i][j]

sum_virus = 0
for i in range(n):
    for j in range(n):
        sum_virus += len(virus_arr[i][j])
print(sum_virus)