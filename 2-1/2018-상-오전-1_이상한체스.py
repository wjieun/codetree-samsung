from collections import deque
from copy import deepcopy

n, m = list(map(int, input().split()))
chess_map = [
    list(map(int, input().split()))
    for _ in range(n)
]

chess_piece = []
for i in range(n):
    for j in range(m):
        if 1 <= chess_map[i][j] <= 5:
            chess_piece.append((i, j))

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

movement = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

def in_range(a, b):
    if 0 <= a < n and 0 <= b < m:
        return True
    return False

def get_blank():
    visited = deepcopy(chess_map)

    for pi, (px, py) in enumerate(chess_piece):
        pn = chess_map[px][py]
        pm = moves[pi]
        pds = movement[pn][pm]

        for pd in pds:
            now_x, now_y = px, py
            while True:
                new_x, new_y = now_x + dxs[pd], now_y + dys[pd]
                if in_range(new_x, new_y) and chess_map[new_x][new_y] < 6:
                    visited[new_x][new_y] = 7
                    now_x, now_y = new_x, new_y
                else:
                    break

    v_sum = [v.count(0) for v in visited]
    return sum(v_sum)

moves = deque()
min_blank_num = float('inf')
def recursive(idx):
    global min_blank_num

    if idx == len(chess_piece):
        blank_num = get_blank()
        min_blank_num = min(min_blank_num, blank_num)
        return

    piece_x, piece_y = chess_piece[idx]
    piece_num = chess_map[piece_x][piece_y]
    for move_num in range(len(movement[piece_num])):
        moves.append(move_num)
        recursive(idx + 1)
        moves.pop()

recursive(0)
print(min_blank_num)