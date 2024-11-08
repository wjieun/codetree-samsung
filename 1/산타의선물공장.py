from collections import defaultdict

MAX_M = 10

q = int(input())
n, m = -1, -1

weight = {}
prv, nxt = defaultdict(lambda: 0), defaultdict(lambda: 0)

head = [0] * MAX_M
tail = [0] * MAX_M
broken = [False] * MAX_M

belt_num = defaultdict(lambda: -1)

for turn in range(q):
    command = tuple(map(int, input().split()))

    if command[0] == 100:
        n, m = command[1], command[2]
        IDs = command[3:3+n]
        Ws = command[3+n:]

        for i in range(n):
            weight[IDs[i]] = Ws[i]

        size = n // m
        for i in range(m):
            head[i] = IDs[i * size]
            tail[i] = IDs[(i + 1) * size - 1]

            for j in range(size):
                idx = i * size + j
                belt_num[IDs[idx]] = i

                if j < size - 1:
                    nxt[IDs[idx]] = IDs[idx + 1]
                    prv[IDs[idx + 1]] = IDs[idx]

    elif command[0] == 200:
        w_max = command[1]
        w_sum = 0
        for i in range(m):
            if head[i] and not broken[i]:
                if weight[head[i]] <= w_max:
                    w_sum += weight[head[i]]
                    belt_num[head[i]] = -1
                    if tail[i] == head[i]: tail[i] = 0
                else:
                    nxt[tail[i]] = head[i]
                    prv[head[i]] = tail[i]
                    tail[i] = head[i]

                head[i] = nxt[head[i]]
                nxt[tail[i]] = 0
        print(w_sum)

    elif command[0] == 300:
        r_id = command[1]
        if belt_num[r_id] == -1:
            print(-1)
        else:
            print(r_id)
            if r_id == head[belt_num[r_id]]: head[belt_num[r_id]] = nxt[r_id]
            if r_id == tail[belt_num[r_id]]: tail[belt_num[r_id]] = prv[r_id]
            belt_num[r_id] = -1
            prv[nxt[r_id]] = prv[r_id]
            nxt[prv[r_id]] = nxt[r_id]

    elif command[0] == 400:
        f_id = command[1]
        bn = belt_num[f_id]
        if bn == -1:
            print(-1)
        else:
            print(bn + 1)
            if f_id != head[bn]:
                prv[head[bn]] = tail[bn]
                nxt[tail[bn]] = head[bn]

                head[bn] = f_id
                tail[bn] = prv[f_id]

                nxt[tail[bn]] = 0
                prv[f_id] = 0

    elif command[0] == 500:
        b_num = command[1] - 1
        if broken[b_num]:
            print(-1)
        else:
            print(b_num + 1)
            broken[b_num] = True

            if head[b_num]:
                for i in range(1, m):
                    new_b = (b_num + i) % m
                    if not broken[new_b]:
                        now = head[b_num]
                        while now:
                            belt_num[now] = new_b
                            now = nxt[now]

                        nxt[tail[new_b]] = head[b_num]
                        prv[head[b_num]] = tail[new_b]
                        tail[new_b] = tail[b_num]

                        head[b_num] = 0
                        tail[b_num] = 0

                        break