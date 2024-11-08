from collections import deque
import time
R, C, K = list(map(int, input().split()))
start = time.time()
arr = [
    [True for _ in range(C)]
    for _ in range(R)
]

ss_x = [2, 1, 1]
ss_y = [0, -1, 1]

# 북 동 남 서
dxs = [-1, 0, 1, 0, 0]
dys = [0, 1, 0, -1, 0]

spaceship_list = []
all_spaceship_list = dict()
score_sum = 0

def in_range(x, y):
    return 0 <= x < R and 0 <= y < C

def find_spaceship(x, y):
    if (x, y) in all_spaceship_list:
        return all_spaceship_list[(x, y)]
    return -1

def get_score():
    global score_sum

    q = deque(); q.append(spaceship_list[-1])
    v = set(); v.add(len(spaceship_list) - 1)
    max_score = 0

    while q:
        x, y, d = q.popleft()
        max_score = max(max_score, x + 1)
        exit_x, exit_y = x + dxs[d], y + dys[d]
        for dx, dy in zip(dxs[:4], dys[:4]):
            new_x, new_y = exit_x + dx, exit_y + dy

            if in_range(new_x, new_y):
                ss = find_spaceship(new_x, new_y)

                if ss != -1 and ss not in v:
                    q.append(spaceship_list[ss])
                    v.add(ss)

    score_sum += max_score + 1

for _ in range(K):
    c, d = list(map(int, input().split()))

    now_x, now_y = -2, c - 1
    while True:
        last_x, last_y = now_x, now_y

        # 내려가기
        for i in range(R):
            can_go_down = True
            for dx, dy in zip(ss_x, ss_y):
                new_x, new_y = now_x + i + dx, now_y + dy

                if 0 <= new_x < R:
                    if not arr[new_x][new_y]:
                        now_x = now_x + i
                        can_go_down = False
                        break

            if not can_go_down:
                break

            if i == R - 1:
                now_x = R - 2

        # 왼쪽
        can_go_left = False
        if now_y > 1:
            now_y -= 1

            can_go = True
            for dx, dy in zip(dxs, dys):
                if 0 <= now_x + dx < R:
                    if not arr[now_x + dx][now_y + dy]:
                        can_go = False
                        break
                elif now_x + dx >= R:
                    can_go = False
                    break

            if can_go:
                for dx, dy in zip(ss_x, ss_y):
                    new_x, new_y = now_x + dx, now_y + dy
                    if 0 <= new_x < R:
                        if not arr[new_x][new_y]:
                            can_go = False
                            break
                    elif new_x >= R:
                        can_go = False
                        break

            if can_go:
                now_x += 1
                can_go_left = True
                d = (d - 1) % 4
            else:
                now_y += 1

        if not can_go_left:
            if now_y < C - 2:
                now_y += 1

                can_go = True
                for dx, dy in zip(dxs, dys):
                    if 0 <= now_x + dx < R:
                        if not arr[now_x + dx][now_y + dy]:
                            can_go = False
                            break
                    elif now_x + dx >= R:
                        can_go = False
                        break

                if can_go:
                    for dx, dy in zip(ss_x, ss_y):
                        new_x, new_y = now_x + dx, now_y + dy
                        if 0 <= new_x < R:
                            if not arr[new_x][new_y]:
                                can_go = False
                                break
                        elif new_x >= R:
                            can_go = False
                            break

                if can_go:
                    now_x += 1
                    d = (d + 1) % 4
                else:
                    now_y -= 1

        if (now_x, now_y) == (last_x, last_y):
            break

    if now_x < 1:
        arr = [
            [True for _ in range(C)]
            for _ in range(R)
        ]

        spaceship_list = []
        all_spaceship_list = dict()
    else:
        for dx, dy in zip(dxs, dys):
            arr[now_x + dx][now_y + dy] = False
            all_spaceship_list[(now_x + dx, now_y + dy)] = len(spaceship_list)
        spaceship_list.append((now_x, now_y, d))

        # 점수
        get_score()

print(score_sum)
print(time.time()-start)