from collections import defaultdict

q = int(input())
n, m = -1, -1

head, tail, belt_cnt = (dict() for _ in range(3))

prv = defaultdict(lambda: 0)
nxt = defaultdict(lambda: 0)

for turn in range(q):
    command = tuple(map(int, input().split()))

    if command[0] == 100:
        n, m = command[1], command[2]
        head, tail, belt_cnt = ({x: 0 for x in range(1, n + 1)} for _ in range(3))

        for i in range(1, m + 1):
            bn = command[2 + i]
            if belt_cnt[bn]:
                nxt[tail[bn]] = i
                prv[i] = tail[bn]
                tail[bn] = i
            else:
                head[bn], tail[bn] = i, i
            belt_cnt[bn] += 1

    elif command[0] == 200:
        m_src, m_dst = command[1], command[2]

        if belt_cnt[m_src]:
            belt_cnt[m_dst] += belt_cnt[m_src]
            belt_cnt[m_src] = 0

            if head[m_dst]:
                nxt[tail[m_src]] = head[m_dst]
            else:
                tail[m_dst] = tail[m_src]
            prv[head[m_dst]] = tail[m_src]

            head[m_dst] = head[m_src]
            head[m_src], tail[m_src] = 0, 0
        print(belt_cnt[m_dst])

    elif command[0] == 300:
        m_src, m_dst = command[1], command[2]
        if belt_cnt[m_src] and belt_cnt[m_dst]:
            head_src, head_dst = head[m_src], head[m_dst]
            nxt_head_src, nxt_head_dst = nxt[head_src], nxt[head_dst]

            nxt[head[m_src]], nxt[head[m_dst]] = nxt_head_dst, nxt_head_src
            prv[nxt_head_src], prv[nxt_head_dst] = head_dst, head_src
            head[m_src], head[m_dst] = head_dst, head_src

            if belt_cnt[m_src] == 1: tail[m_src] = head[m_src]
            if belt_cnt[m_dst] == 1: tail[m_dst] = head[m_dst]
        elif not belt_cnt[m_src] and belt_cnt[m_dst]:
            belt_cnt[m_src] += 1
            belt_cnt[m_dst] -= 1

            head[m_src] = head[m_dst]
            tail[m_src] = head[m_dst]

            if nxt[head[m_dst]]:
                head[m_dst] = nxt[head[m_dst]]
                prv[head[m_dst]] = 0
                nxt[head[m_src]] = 0
            else:
                head[m_dst], tail[m_dst] = 0, 0
        elif belt_cnt[m_src] and not belt_cnt[m_dst]:
            belt_cnt[m_src] -= 1
            belt_cnt[m_dst] += 1

            head[m_dst] = head[m_src]
            tail[m_dst] = head[m_src]

            if nxt[head[m_src]]:
                head[m_src] = nxt[head[m_src]]
                prv[head[m_src]] = 0
                nxt[head[m_dst]] = 0
            else:
                head[m_src], tail[m_src] = 0, 0
        print(belt_cnt[m_dst])

    elif command[0] == 400:
        m_src, m_dst = command[1], command[2]

        if belt_cnt[m_src] > 1:
            mid = belt_cnt[m_src] // 2
            belt_cnt[m_src] -= mid
            belt_cnt[m_dst] += mid

            now = head[m_src]
            for _ in range(mid):
                now = nxt[now]

            prv[head[m_dst]] = prv[now]
            nxt[prv[now]] = head[m_dst]
            head[m_dst] = head[m_src]
            head[m_src] = now
            if not tail[m_dst]: tail[m_dst] = prv[now]
            prv[now] = 0

        print(belt_cnt[m_dst])

    elif command[0] == 500:
        p_num = command[1]
        a = prv[p_num] if prv[p_num] else -1
        b = nxt[p_num] if nxt[p_num] else -1
        print(a + 2 * b)

    elif command[0] == 600:
        b_num = command[1]
        a = head[b_num] if head[b_num] else -1
        b = tail[b_num] if tail[b_num] else -1
        c = belt_cnt[b_num]
        print(a + 2 * b + 3 * c)