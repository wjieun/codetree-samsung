from copy import deepcopy

n, m, k = list(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
] # 0 빈칸, 자연수 플레이어

prior_player_arr = deepcopy(arr)

prior_turn_arr = [
    [0] * n
    for _ in range(n)
]

position = {}
for i in range(n):
    for j in range(n):
        if arr[i][j] > 0:
            prior_turn_arr[i][j] = k
            position[arr[i][j]] = [i, j]

direction = [d-1 for d in list(map(int, input().split()))]
direction.insert(0, -1)

priority = {}
dead = {}
for i in range(1, m+1):
    priority[i] = []
    dead[i] = False
    for _ in range(4):
        d_list = list(map(int, input().split()))
        priority[i].append([d-1 for d in d_list])

# 1은 위, 2는 아래, 3은 왼쪽, 4는 오른쪽
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

turn = 0
for turn in range(1, 1001):
    new_arr = [
        [[] for _ in range(n)]
        for _ in range(n)
    ]

    # 이동
    for pi in position:
        if not dead[pi]:
            px, py = position[pi]
            pd = direction[pi]
            moved = False

            # 아무도 독점계약을 맺지 않은 칸
            for d in priority[pi][pd]:
                dx, dy = dxs[d], dys[d]
                new_x, new_y = px + dx, py + dy

                if in_range(new_x, new_y) and not prior_player_arr[new_x][new_y]:
                    new_arr[new_x][new_y].append(pi)
                    direction[pi] = d
                    position[pi] = [new_x, new_y]
                    moved = True
                    break

            # 본인이 독점계약한 땅
            if not moved:
                for d in priority[pi][pd]:
                    dx, dy = dxs[d], dys[d]
                    new_x, new_y = px + dx, py + dy

                    if in_range(new_x, new_y) and prior_player_arr[new_x][new_y] == pi:
                        new_arr[new_x][new_y].append(pi)
                        direction[pi] = d
                        position[pi] = [new_x, new_y]
                        moved = True
                        break

                # 가만히
                if not moved:
                    new_arr[px][py].append(pi)

    # 독점 계약 턴 빼기
    for i in range(n):
        for j in range(n):
            if prior_turn_arr[i][j] == 1:
                prior_turn_arr[i][j] = 0
                prior_player_arr[i][j] = 0
            elif prior_turn_arr[i][j] > 1:
                prior_turn_arr[i][j] -= 1

    # 한 칸에 여러 플레이어
    for i in range(n):
        for j in range(n):
            if len(new_arr[i][j]) == 0:
                new_arr[i][j] = 0
            elif len(new_arr[i][j]) == 1:
                new_arr[i][j] = new_arr[i][j][0]
                prior_player_arr[i][j] = new_arr[i][j]
                prior_turn_arr[i][j] = k
            else:
                min_player = min(new_arr[i][j])
                for player in new_arr[i][j]:
                    if player != min_player:
                        dead[player] = True

                new_arr[i][j] = min_player
                prior_player_arr[i][j] = min_player
                prior_turn_arr[i][j] = k
    arr = new_arr

    # 1번 플레이어만 남았으면 게임 끝내기
    if sum(dead.values()) == m - 1:
        break

if turn >= 1000:
    print(-1)
else:
    print(turn)