from queue import PriorityQueue

Q = int(input())
N, M, P = -1, -1, -1
all_score = 0

rabbits = PriorityQueue()
rabbits_idx = dict()
rabbits_score = dict()

class Rabbit:
    def __init__(self, pid, d):
        self.jump = 0
        self.x = 1
        self.y = 1
        self.pid = pid
        self.d = d

    def __lt__(self, other):
        if self.jump == other.jump:
            if self.x + self.y == other.x + other.y:
                if self.x == other.x:
                    if self.y == other.y:
                        return self.pid < other.pid
                    else:
                        return self.y < other.y
                else:
                    return self.x < other.x
            else:
                return self.x + self.y < other.x + other.y
        else:
            return self.jump < other.jump

    def change_d(self, L):
        self.d *= L

def ready(cmd):
    global N, M, P, rabbits
    N, M, P = cmd[1], cmd[2], cmd[3]
    for i in range(P):
        pid, d = cmd[4 + 2 * i], cmd[4 + 2 * i + 1]
        rb = Rabbit(pid, d)
        rabbits.put(rb)
        rabbits_idx[pid] = rb
        rabbits_score[pid] = 0

def compare(mx, my, nx, ny):
    if mx + my == nx + ny:
        if mx == nx:
            return my < ny
        else:
            return mx < nx
    else:
        return mx + my < nx + ny

def get_new_coord(rabbit):
    x, y, d = rabbit.x, rabbit.y, rabbit.d
    max_x, max_y = -1, -1

    # 상하
    for direction in [1, -1]:
        new_x, new_y = x, y
        new_d = d % ((N - 1) * 2)
        while new_d > 0:
            if new_x + new_d * direction > N:
                new_d -= N - new_x
                new_x = N
                direction = -direction
            elif new_x + new_d * direction < 1:
                new_d -= new_x - 1
                new_x = 1
                direction = -direction
            else:
                new_x = new_x + new_d * direction
                new_d = 0
        if compare(max_x, max_y, new_x, new_y):
            max_x, max_y = new_x, new_y

    # 좌우
    for direction in [1, -1]:
        new_x, new_y = x, y
        new_d = d % ((M - 1) * 2)
        while new_d > 0:
            if new_y + new_d * direction > M:
                new_d -= M - new_y
                new_y = M
                direction = -direction
            elif new_y + new_d * direction < 1:
                new_d -= new_y - 1
                new_y = 1
                direction = -direction
            else:
                new_y = new_y + new_d * direction
                new_d = 0
        if compare(max_x, max_y, new_x, new_y):
            max_x, max_y = new_x, new_y

    return max_x, max_y

def race(cmd):
    global all_score
    K, S = cmd[1], cmd[2]

    all_rabbits = set()
    for _ in range(K):
        rb = rabbits.get()

        r, c = get_new_coord(rb)
        rb.x, rb.y, rb.jump = r, c, rb.jump + 1

        all_score += r + c
        rabbits_score[rb.pid] -= r + c

        rabbits.put(rb)
        all_rabbits.add(rb.pid)

    max_pid, max_x, max_y = -1, -1, -1
    for rabbit in all_rabbits:
        r_x, r_y = rabbits_idx[rabbit].x, rabbits_idx[rabbit].y
        if compare(max_x, max_y, r_x, r_y):
            max_pid, max_x, max_y = rabbit, r_x, r_y

    rabbits_score[max_pid] += S

def change_dis(cmd):
    pid, L = cmd[1], cmd[2]
    rabbits_idx[pid].change_d(L)

for _ in range(Q):
    command = tuple(map(int, input().split()))

    if command[0] == 100:
        ready(command)

    elif command[0] == 200:
        race(command)

    elif command[0] == 300:
        change_dis(command)

    elif command[0] == 400:
        print(max(rabbits_score.values()) + all_score)