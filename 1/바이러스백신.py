n, m = list(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
] # 바이러스 0, 벽 1, 병원 2

hospital_list = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            hospital_list.append((i, j))

x_list = [1, -1, 0, 0]
y_list = [0, 0, 1, -1]
min_t = float('inf')

def spread_vaccine():
    vaccine_list = []
    visited = [
        [False for _ in range(n)]
        for _ in range(n)
    ]
    time = [
        [float('inf') for _ in range(n)]
        for _ in range(n)
    ]

    for s in selected:
        vaccine_list.append(hospital_list[s])
        visited[hospital_list[s][0]][hospital_list[s][1]] = True
        time[hospital_list[s][0]][hospital_list[s][1]] = 0

    while len(vaccine_list) > 0:
        new_vaccine_list = []
        for vaccine_x, vaccine_y in vaccine_list:
            for d in range(4):
                new_x = vaccine_x + x_list[d]
                new_y = vaccine_y + y_list[d]

                if 0 <= new_x < n and 0 <= new_y < n:
                    if arr[new_x][new_y] != 1 and not visited[new_x][new_y]:
                        new_vaccine_list.append((new_x, new_y))
                        visited[new_x][new_y] = True
                        time[new_x][new_y] = time[vaccine_x][vaccine_y] + 1
        vaccine_list = new_vaccine_list

    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                time[i][j] = 0

    return max([max(t) for t in time])

selected = []
def find(idx):
    global min_t

    if len(selected) == m:
        t = spread_vaccine()
        min_t = min(min_t, t)
        return

    if idx == len(hospital_list):
        return

    find(idx + 1)

    selected.append(idx)
    find(idx + 1)
    selected.pop()

find(0)

if min_t == float('inf'):
    print(-1)
else:
    print(min_t)