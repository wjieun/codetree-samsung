from collections import defaultdict

Q = int(input())
COLOR_MAX = 5

nodes = dict()
isRoot = defaultdict(lambda: False)

class Node():
    def __init__(self, m_id, p_id, color, max_depth, turn):
        self.m_id = m_id
        self.p_id = p_id
        self.color = color
        self.max_depth = max_depth
        self.update = turn
        self.child = []

    def add_child(self, c_id):
        self.child.append(c_id)

    def change_color(self, color, turn):
        self.color = color
        self.update = turn

class ColorCount:
    def __init__(self):
        self.cnt = [0] * (COLOR_MAX + 1)

    def __add__(self, obj):
        res = ColorCount()
        for i in range(1, COLOR_MAX + 1):
            res.cnt[i] = self.cnt[i] + obj.cnt[i]
        return res

    def score(self):
        result = 0
        for i in range(1, COLOR_MAX + 1):
            result += 1 if self.cnt[i] else 0
        return result * result

def can_child(curr, depth):
    if curr.p_id == -1:
        return True
    if curr.max_depth <= depth:
        return False
    return can_child(nodes[curr.p_id], depth + 1)

def get_color(curr):
    if curr.p_id == -1:
        return 0, 0

    info = get_color(nodes[curr.p_id])
    if info[1] > curr.update:
        return info
    else:
        return curr.color, curr.update

def get_beauty(curr, color, update):
    if update < curr.update:
        update = curr.update
        color = curr.color

    result = [0, ColorCount()]
    result[1].cnt[color] = 1
    for c_id in curr.child:
        c = nodes[c_id]

        sub_result = get_beauty(c, color, update)
        result[1] = result[1] + sub_result[1]
        result[0] = result[0] + sub_result[0]

    result[0] += result[1].score()
    return result

for i in range(1, Q + 1):
    command = list(map(int, input().split()))
    command_num = command[0]

    if command_num == 100:
        m_id, p_id, color, max_depth = command[1:]
        if p_id == -1:
            isRoot[m_id] = True
        if isRoot[m_id] or can_child(nodes[p_id], 1):
            nodes[m_id] = Node(m_id, p_id, color, max_depth, i)

            if not isRoot[m_id]:
                nodes[p_id].add_child(m_id)

    elif command_num == 200:
        m_id, color = command[1:]
        nodes[m_id].change_color(color, i)

    elif command_num == 300:
        m_id = command[1]
        m_color, _ = get_color(nodes[m_id])
        print(m_color)

    elif command_num == 400:
        beauty = 0
        for root_id, is_root in isRoot.items():
            if is_root:
                root_node = nodes[root_id]
                now_beauty, _ = get_beauty(root_node, root_node.color, root_node.update)
                beauty += now_beauty
        print(beauty)
