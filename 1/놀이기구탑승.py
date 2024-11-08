n = int(input())

arr = {i: [] for i in range(n*n)}
order_list = []
for _ in range(n*n):
    input_ = list(map(int, input().split()))
    order_list.append(input_[0])
    arr[input_[0]] = input_[1:]

seat = [
    [0 for _ in range(n)]
    for _ in range(n)
]

x_list = [1, -1, 0, 0]
y_list = [0, 0, 1, -1]

def find_like_seat(like_list):
    max_like = 0
    max_like_seat = []
    max_like_seat_blank = []

    for i in range(n):
        for j in range(n):
            if seat[i][j] == 0:
                like_sum = 0
                blank_sum = 0
                for k in range(4):
                    new_x = i + x_list[k]
                    new_y = j + y_list[k]
                    if 0 <= new_x < n and 0 <= new_y < n:
                        if seat[new_x][new_y] == 0:
                            blank_sum += 1
                        elif seat[new_x][new_y] in like_list:
                            like_sum += 1

                if like_sum == max_like:
                    max_like_seat.append((i, j))
                    max_like_seat_blank.append(blank_sum)
                elif like_sum > max_like:
                    max_like = like_sum
                    max_like_seat = [(i, j)]
                    max_like_seat_blank = [blank_sum]

    if max_like_seat_blank.count(max(max_like_seat_blank)) > 1:
        new_list_x = []
        new_list_y = []
        for i in range(len(max_like_seat_blank)):
            if max_like_seat_blank[i] == max(max_like_seat_blank):
                new_list_x.append(max_like_seat[i][0])
                new_list_y.append(max_like_seat[i][1])
        return new_list_x[0], new_list_y[0]
    else:
        for i in range(len(max_like_seat_blank)):
            if max_like_seat_blank[i] == max(max_like_seat_blank):
                return max_like_seat[i]

def calc_like(like_list):
    like_sum = 0
    for k in range(4):
        new_x = i + x_list[k]
        new_y = j + y_list[k]
        if 0 <= new_x < n and 0 <= new_y < n:
            if seat[new_x][new_y] in like_list:
                like_sum += 1

    if like_sum > 0:
        return 10 ** (like_sum - 1)
    else:
        return like_sum

for o in order_list:
    my_seat_x, my_seat_y = find_like_seat(arr[o])
    seat[my_seat_x][my_seat_y] = o

all_like_sum = 0
for i in range(n):
    for j in range(n):
        o = seat[i][j]
        all_like_sum += calc_like(arr[o])
print(all_like_sum)