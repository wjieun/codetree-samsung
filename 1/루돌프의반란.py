N, M, P, C, D = list(map(int, input().split()))
rr, rc = [x - 1 for x in list(map(int, input().split()))]
rdx, rdy = -1, -1

santas = dict()
for _ in range(P):
    pn, sr, sc = list(map(int, input().split()))
    santas[pn] = (sr - 1, sc - 1)

dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, -1, -1, -1, 0, 1, 1, 1]

# 상우하좌 우선순위
santa_dxs = [-1, 0, 1, 0]
santa_dys = [0, 1, 0, -1]

points = {santa: 0 for santa in santas}
faints = {santa: -100 for santa in santas}

def calc_dis(r1, c1, r2, c2):
    return (r1 - r2) ** 2 + (c1 - c2) ** 2

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def get_santa():
    global rr, rc

    min_dis = float('inf')
    max_coord = (-1, -1)
    for santa in santas:
        sr, sc = santas[santa]
        if (sr, sc) != (-1, -1):
            dis = calc_dis(rr, rc, sr, sc)
            if dis < min_dis:
                min_dis = dis
                max_coord = (sr, sc)
            elif dis == min_dis:
                max_coord = max([(sr, sc), max_coord])

    return max_coord

def move_rudolph(turn):
    global rr, rc, rdx, rdy, santas, faints
    close_santa_x, close_santa_y = get_santa()

    min_dis = float('inf')
    move_x, move_y = -1, -1
    move_dx, move_dy = -1, -1
    for dx, dy in zip(dxs, dys):
        new_x, new_y = rr + dx, rc + dy
        dis = calc_dis(new_x, new_y, close_santa_x, close_santa_y)
        if dis < min_dis:
            min_dis = dis
            move_x, move_y = new_x, new_y
            move_dx, move_dy = dx, dy

    rr, rc = move_x, move_y
    rdx, rdy = move_dx, move_dy

    santa = there_santa(-1, rr, rc)
    if len(santa):
        santa = santa[0]
        points[santa] += C
        faints[santa] = turn

        santa_new_x = santas[santa][0] + rdx * C
        santa_new_y = santas[santa][1] + rdy * C

        if not in_range(santa_new_x, santa_new_y):
            santas[santa] = (-1, -1)
        else:
            santas[santa] = santa_new_x, santa_new_y
            if len(there_santa(santa, santa_new_x, santa_new_y)):
                interaction(santa, santa_new_x, santa_new_y, rdx, rdy)

def interaction(now_santa, start_x, start_y, dx, dy):
    now_x, now_y = start_x, start_y
    already_santa = there_santa(now_santa, now_x, now_y)[0]
    while True:
        new_x, new_y = now_x + dx, now_y + dy
        if in_range(new_x, new_y):
            santas[already_santa] = (new_x, new_y)

            ts = there_santa(already_santa, new_x, new_y)
            if len(ts):
                already_santa = ts[0]
                now_x, now_y = new_x, new_y
            else:
                break
        else:
            santas[already_santa] = (-1, -1)
            break

def there_santa(now_santa, x, y):
    return [santa for santa in santas if santas[santa] == (x, y) and santa != now_santa]

def move_santas(turn):
    global santas

    for santa in range(1, P + 1):
        if not turn - 1 <= faints[santa] <= turn:
            santa_x, santa_y = santas[santa]
            now_dis = calc_dis(rr, rc, santa_x, santa_y)
            move_x, move_y = -1, -1
            move_d = -1

            for d, (dx, dy) in enumerate(zip(santa_dxs, santa_dys)):
                new_x, new_y = santa_x + dx, santa_y + dy
                if in_range(new_x, new_y):
                    if not len(there_santa(santa, new_x, new_y)):
                        new_dis = calc_dis(rr, rc, new_x, new_y)
                        if new_dis < now_dis:
                            now_dis = new_dis
                            move_x, move_y = new_x, new_y
                            move_d = d

            if (move_x, move_y) != (-1, -1):
                santas[santa] = (move_x, move_y)
                if (move_x, move_y) == (rr, rc):
                    points[santa] += D
                    faints[santa] = turn

                    new_d = (move_d + 2) % 4
                    santa_new_x = santas[santa][0] + santa_dxs[new_d] * D
                    santa_new_y = santas[santa][1] + santa_dys[new_d] * D

                    if not in_range(santa_new_x, santa_new_y):
                        santas[santa] = (-1, -1)
                    else:
                        santas[santa] = (santa_new_x, santa_new_y)
                        if len(there_santa(santa, santa_new_x, santa_new_y)):
                            interaction(santa, santa_new_x, santa_new_y, santa_dxs[new_d], santa_dys[new_d])

def all_santas_in():
    return [santa for santa in santas if santas[santa] != (-1, -1)]

for t in range(M):
    move_rudolph(t)
    move_santas(t)

    santas_in = all_santas_in()
    if len(santas_in):
        for santa in santas_in:
            points[santa] += 1
    else:
        break

for i in range(1, P + 1):
    print(points[i], end=' ')