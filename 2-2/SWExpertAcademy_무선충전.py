def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def in_range(a, b):
    return 0 <= a < N and 0 <= b < N

def get_best(Ap, Bp):
    max_power = 0

    if not Ap:
        Ap = [0]
    if not Bp:
        Bp = [0]

    for ai in Ap:
        for bi in Bp:
            if ai == bi:
                max_power = max(max_power, BCs_power[ai])
            else:
                power = BCs_power[ai] + BCs_power[bi]
                max_power = max(max_power, power)

    return max_power

T = int(input())
for test_case in range(1, T + 1):
    N = 10
    M, A = list(map(int, input().split()))

    Ax, Ay, Bx, By = 0, 0, 9, 9
    A_move = list(map(int, input().split()))
    B_move = list(map(int, input().split()))

    BCs = dict()
    BCs_power = dict()
    BCs_power[0] = 0
    for i in range(1, A + 1):
        y, x, c, p = list(map(int, input().split()))
        x, y = x - 1, y - 1
        BCs[i] = (x, y, c)
        BCs_power[i] = p

    arr = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(1, A + 1):
        BCx, BCy, BCc = BCs[i]

        for x in range(BCx - BCc, BCx + BCc + 1):
            for y in range(BCy - BCc, BCy + BCc + 1):
                if in_range(x, y) and get_distance(BCx, BCy, x, y) <= BCc:
                    arr[x][y].append(i)

    def move_people(t):
        global Ax, Ay, Bx, By

        Ad = A_move[t]
        Ax, Ay = Ax + dxs[Ad], Ay + dys[Ad]
        Ap = arr[Ax][Ay]

        Bd = B_move[t]
        Bx, By = Bx + dxs[Bd], By + dys[Bd]
        Bp = arr[Bx][By]

        return get_best(Ap, Bp)


    # X상우하좌
    dxs = [0, -1, 0, 1, 0]
    dys = [0, 0, 1, 0, -1]

    power_sum = get_best(arr[Ax][Ay], arr[Bx][By])
    for turn in range(M):
        now_power = move_people(turn)
        power_sum += now_power
    print(f'#{test_case} {power_sum}')