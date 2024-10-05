from collections import deque

def bfs(g, u, v):
    q = deque([u])
    used = {u}
    dist = {u: 0}

    while q:
        cur = q.popleft()

        if cur == v:
            return dist[cur]

        for to in g[cur]:
            if to not in used:
                used.add(to)
                dist[to] = dist[cur] + 1
                q.append(to)

    return -1


def solve():

    n, m = map(int, input().split())
    g = {i: [] for i in range(1, n + 1)}

    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    start, end = map(int, input().split())

    result = bfs(g, start, end)

    print(result)

solve()
#Данный код представляет собой реализацию алгоритма поиска в ширину (Breadth-first search, BFS) для нахождения кратчайшего пути между двумя вершинами в графе. Алгоритм принимает на вход неориентированный граф g, заданный в виде словаря, где ключами являются номера вершин, а значениями — списки смежных вершин. Также задаются начальная вершина start и конечная вершина end. Алгоритм возвращает длину кратчайшего пути от start до end или -1, если пути не существует.
