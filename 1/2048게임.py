import copy

n = int(input())
array = [
    list(map(int, input().split()))
    for _ in range(n)
]

x_list = [1, -1, 0, 0]
y_list = [0, 0, 1, -1]
max_num = 0

def move_board(d, ar):
    arr = copy.deepcopy(ar)
    x_move, y_move = x_list[d], y_list[d]
    if x_move == 1 or y_move == 1:
        start = n-2; end = -1
    else:
        start = 1; end = n

    # 상하
    if abs(x_move) == 1:
        for j in range(n):
            cur = start + x_move
            for i in range(start, end, -x_move):
                if arr[i][j] != 0:
                    if arr[cur][j] == 0:
                        arr[cur][j] = arr[i][j]
                        arr[i][j] = 0
                    elif arr[cur][j] == arr[i][j]:
                        arr[cur][j] *= 2
                        arr[i][j] = 0
                        cur += -x_move
                    elif arr[cur][j] != arr[i][j]:
                        cur += -x_move
                        arr[cur][j] = arr[i][j]
                        if cur != i:
                            arr[i][j] = 0
    # 좌우
    else:
        for i in range(n):
            cur = start + y_move
            for j in range(start, end, -y_move):
                if arr[i][j] != 0:
                    if arr[i][cur] == 0:
                        arr[i][cur] = arr[i][j]
                        arr[i][j] = 0
                    elif arr[i][cur] == arr[i][j]:
                        arr[i][cur] *= 2
                        arr[i][j] = 0
                        cur += -y_move
                    elif arr[i][cur] != arr[i][j]:
                        cur += -y_move
                        arr[i][cur] = arr[i][j]
                        if cur != j:
                            arr[i][j] = 0

    return arr

selected = []
def find(d, a, cnt):
    global max_num

    a = move_board(d, a)

    if cnt == 5:
        now_max_num = max([max(a_num) for a_num in a])
        max_num = max(max_num, now_max_num)
        return

    for i in range(4):
        selected.append(i)
        find(i, a, cnt + 1)
        selected.pop()

for i in range(4):
    selected.append(i)
    find(i, array, 1)
    selected.pop()

print(max_num)