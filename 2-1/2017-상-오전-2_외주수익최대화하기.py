n = int(input())
work = [list(map(int, input().split())) for _ in range(n)]

def get_list(num):
    global n

    l = [0] * n
    j = n - 1

    while num > 1:
        l[j] = num % 2
        j -= 1
        num = num // 2

    if num <= 1:
        l[j] = num

    return l

max_amount = 0
for i in range(1, 2**n):
    do_list = get_list(i)

    next = -1
    amount = 0
    can = True

    for i, d in enumerate(do_list):
        if d == 1:
            if i < next:
                can = False
                break
            else:
                next = i + work[i][0]

                if next > n:
                    can = False
                    break
                else:
                    amount += work[i][1]

    if can and amount > max_amount:
        max_amount = amount

print(max_amount)