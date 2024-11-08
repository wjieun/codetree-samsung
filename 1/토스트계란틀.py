n, L, R = list(map(int, input().split()))
eggs = [
    list(map(int, input().split()))
    for _ in range(n)
]

x_list = [1, -1, 0, 0]
y_list = [0, 0, 1, -1]
move_cnt = 0

def compare(my_i1, my_j1, my_i2, my_j2):
    return L <= (abs(eggs[my_i1][my_j1] - eggs[my_i2][my_j2])) <= R

def find_ij(my_i1, my_j1, my_i2, my_j2, my_list):
    in1 = -1
    in2 = -1

    for idx in range(len(my_list)):
        if (my_i1, my_j1) in my_list[idx]:
            in1 = idx
        if (my_i2, my_j2) in my_list[idx]:
            in2 = idx

    if in1 == -1 and in2 == -1:
        side_list.append({(my_i1, my_j1), (my_i2, my_j2)})
    elif in1 == -1 and in2 != -1:
        my_list[in2].add((my_i1, my_j1))
    elif in1 != -1 and in2 == -1:
        my_list[in1].add((my_i2, my_j2))
    elif in1 != in2:
        set1 = my_list.pop(max(in1, in2))
        set2 = my_list.pop(min(in1, in2))
        my_list.append(set1.union(set2))

while True:
    side_list = list()
    for i in range(n):
        for j in range(n):
            for k in range(4):
                i2 = i + x_list[k]; j2 = j + y_list[k]
                if 0 <= i2 < n and 0 <= j2 < n:
                    if compare(i, j, i2, j2):
                        find_ij(i, j, i2, j2, side_list)

    if len(side_list) == 0:
        break

    for side in side_list:
        side_sum = 0
        for s in side:
            side_sum += eggs[s[0]][s[1]]

        new_eggs = int(side_sum / len(side))
        for s in side:
            eggs[s[0]][s[1]] = new_eggs

    move_cnt += 1

print(move_cnt)