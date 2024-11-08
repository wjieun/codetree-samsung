n, m, k = list(map(int, input().split()))
k = k + 1

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

contract_owner = [[0] * n for _ in range(n)]
contract_turn = [[0] * n for _ in range(n)]
position = dict()

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            position[arr[i][j]] = (i, j)
            contract_owner[i][j] = arr[i][j]
            contract_turn[i][j] = k

direction = {
    i: x - 1
    for i, x in zip(
        range(1, m + 1),
        list(map(int, input().split()))
    )
}
priority = dict()
dead = dict()
save_people = m

for i in range(1, m + 1):
    dead[i] = False
    priority[i] = [
        [x - 1 for x in list(map(int, input().split()))]
        for _ in range(4)
    ]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

def move_player(idx, new_arr):
    global save_people

    now_direction = direction[idx]
    move_priority = priority[idx][now_direction]
    now_x, now_y = position[idx]

    # 아무도 독점계약을 맺지 않은 칸
    for d in move_priority:
        new_x, new_y = now_x + dxs[d], now_y + dys[d]

        if in_range(new_x, new_y) and not contract_owner[new_x][new_y]:
            if not new_arr[new_x][new_y]: # 아무도 없을 때
                new_arr[new_x][new_y] = idx
                direction[idx] = d
                position[idx] = (new_x, new_y)

            else: # 누군가 있을 때 -> 작은 번호부터 이동하므로 탈락
                dead[idx] = True
                save_people -= 1

            return

    # 본인이 독점계약한 땅
    for d in move_priority:
        new_x, new_y = now_x + dxs[d], now_y + dys[d]

        if in_range(new_x, new_y) and contract_owner[new_x][new_y] == idx:
            new_arr[new_x][new_y] = idx

            direction[idx] = d
            position[idx] = (new_x, new_y)

            return

    new_arr[now_x][now_y] = idx

def move_players():
    new_arr = [[0] * n for _ in range(n)]

    for i in range(1, m + 1):
        if not dead[i]:
            move_player(i, new_arr)

    for i in range(1, m + 1):
        if not dead[i]:
            x, y = position[i]
            contract_owner[x][y] = i
            contract_turn[x][y] = k

for turn in range(1, 1001):
    for i in range(n):
        for j in range(n):
            if contract_turn[i][j] > 0:
                contract_turn[i][j] -= 1

                if contract_turn[i][j] == 0:
                    contract_owner[i][j] = 0

    move_players()

    if save_people == 1:
        break

if turn >= 1000:
    print(-1)
else:
    print(turn)