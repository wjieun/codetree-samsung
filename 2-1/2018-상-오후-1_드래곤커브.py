n = int(input())

# 0~3 오위왼아
dxs = [0, -1, 0, 1]
dys = [1, 0, -1, 0]

map_d = {(0, 1): 0, (-1, 0): 1, (0, -1): 2, (1, 0): 3}

box_xs = [0, 1, 1]
box_ys = [1, 0, 1]

all_curves = set()
for _ in range(n):
    x, y, d, g = list(map(int, input().split()))
    curves = [(x, y), (x + dxs[d], y + dys[d])]

    for _ in range(g):
        for i in range(len(curves)-1, 0, -1):
            dx, dy = curves[i][0] - curves[i-1][0], curves[i][1] - curves[i-1][1]
            new_d = (map_d[(dx, dy)] + 1) % 4
            curves.append((curves[-1][0] + dxs[new_d], curves[-1][1] + dys[new_d]))

    all_curves.update(set(curves))

count = 0
for cx, cy in all_curves:
    can = True
    for bx, by in zip(box_xs, box_ys):
        if (cx + bx, cy + by) not in all_curves:
            can = False
            break

    if can:
        count += 1

print(count)