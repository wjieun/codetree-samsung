n, m, k = list(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(m)
] # 위치 x, y(1~n), 질량 m, 속력 s, 방향 d(↑, ↗, →, ↘, ↓, ↙, ←, ↖)
in_map_list = dict()

for x, y, m, s, d in arr:
    if (x, y) not in in_map_list:
        in_map_list[(x, y)] = [(m, s, d)]
    else:
        in_map_list[(x, y)].append((m, s, d))

x_list = [-1, -1, 0, 1, 1, 1, 0, -1]
y_list = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k):
    keys = list(in_map_list.keys())
    new_in_map_list = dict()
    # 움직이기
    for in_map in keys:
        x, y = in_map
        for m, s, d in in_map_list[in_map]:
            new_x = (x + x_list[d] * s) % n
            new_y = (y + y_list[d] * s) % n
            if (new_x, new_y) in new_in_map_list:
                new_in_map_list[(new_x, new_y)].append((m, s, d))
            else:
                new_in_map_list[(new_x, new_y)] = [(m, s, d)]
    in_map_list = new_in_map_list

    # 움직이고 나서
    keys = list(in_map_list.keys())
    for in_map in keys:
        new_m, new_s = 0, 0
        d_list = []
        if len(in_map_list[in_map]) > 1:
            for m, s, d in in_map_list[in_map]:
                new_m += m
                new_s += s
                d_list.append(d)
            new_m = int(new_m / 5)
            new_s = int(new_s / len(in_map_list[in_map]))

            if new_m != 0:
                all_d1, all_d2 = True, True
                for d in d_list:
                    if d % 2 == 0:
                        all_d2 = False
                    if d % 2 == 1:
                        all_d1 = False

                new_atom_list = []
                if all_d1 or all_d2:
                    for d in range(0, 8, 2):
                        new_atom_list.append((new_m, new_s, d))
                else:
                    for d in range(1, 8, 2):
                        new_atom_list.append((new_m, new_s, d))
                in_map_list[in_map] = new_atom_list
            else:
                del in_map_list[in_map]

m_list = []
for in_map in in_map_list:
    for m, s, d in in_map_list[in_map]:
        m_list.append(m)
sum_m = sum(m_list)
print(sum_m)