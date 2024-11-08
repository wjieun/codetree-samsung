n, k = list(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
] # 0 흰색, 1 빨간색, 2 파란색

piece = [
    [[] for _ in range(n)]
    for _ in range(n)
]

piece_info = {}

for i in range(k):
    x, y, d = list(map(int, input().split()))
    x, y, d = x-1, y-1, d-1
    piece[x][y].append(i)
    piece_info[i] = [x, y, d]

# 오왼위아
dxs = [0, 0, -1, 1]
dys = [1, -1, 0, 0]
change_d = {0: 1, 1: 0, 2: 3, 3: 2}

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

def move():
    for pi in range(k):
        for count in range(2):
            px, py, pd = piece_info[pi]
            new_x, new_y = px + dxs[pd], py + dys[pd]

            if in_range(new_x, new_y):
                pi_idx = piece[px][py].index(pi)
                move_pieces = piece[px][py][pi_idx:]

                if arr[new_x][new_y] == 1:
                    move_pieces.reverse()
                elif arr[new_x][new_y] == 2:
                    if count != 1:
                        piece_info[pi][-1] = change_d[pd]
                    continue

                piece[px][py] = piece[px][py][:pi_idx]
                piece[new_x][new_y].extend(move_pieces)

                for mi in move_pieces:
                    piece_info[mi][0] = new_x
                    piece_info[mi][1] = new_y

                if len(piece[new_x][new_y]) >= 4:
                    return True

                break

            else:
                if count != 1:
                    piece_info[pi][-1] = change_d[pd]

    return False

for turn in range(1, 1002):
    stop = move()
    if stop: break

if turn == 1001:
    print(-1)
else:
    print(turn)