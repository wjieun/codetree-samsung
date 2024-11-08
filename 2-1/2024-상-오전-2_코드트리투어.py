from collections import defaultdict
import heapq

Q = int(input())

INF = float('inf')
distance = []
graph = defaultdict(lambda: defaultdict(lambda: INF))

items = []
items_id = set()
deleted_id = set()
m = 0

def dijkstra(start):
    global distance

    h = []
    heapq.heappush(h, (0, start))
    distance[start] = 0

    while h:
        dist, node = heapq.heappop(h)
        if dist > distance[node]:
            continue

        for next_node, next_cost in graph[node].items():
            next_cost += distance[node]
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heapq.heappush(h, (next_cost, next_node))

for _ in range(Q):
    command = list(map(int, input().split()))
    command_num = command[0]

    if command_num == 100:
        n, m = command[1], command[2]
        command = command[3:]

        for i in range(m):
            v, u, w = command[3 * i], command[3 * i + 1], command[3 * i + 2]
            graph[v][u] = min(w, graph[v][u])
            graph[u][v] = min(w, graph[u][v])

        distance = [INF] * n
        dijkstra(0)

    elif command_num == 200:
        id, revenue, dest = command[1:]
        items_id.add(id)
        cost = distance[dest]
        heapq.heappush(items, (-(revenue - cost), id, revenue, dest))

    elif command_num == 300:
        id = command[1]
        if id in items_id:
            deleted_id.add(id)

    elif command_num == 400:
        printed = False

        while items:
            profit, id, revenue, dest = items[0]
            if -profit >= 0:
                heapq.heappop(items)
                if id not in deleted_id:
                    print(id)
                    printed = True
                    break
            else:
                break

        if not printed:
            print(-1)

    elif command_num == 500:
        new_items = []
        distance = [INF] * n
        dijkstra(command[1])

        for _, id, revenue, dest in items:
            if id not in deleted_id:
                cost = distance[dest]
                heapq.heappush(new_items, (-(revenue - cost), id, revenue, dest))

        items = new_items