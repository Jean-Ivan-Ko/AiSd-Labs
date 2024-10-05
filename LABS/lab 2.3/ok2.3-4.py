import sys

sys.setrecursionlimit(200000)


def dfs(v, g, used, res):
    used[v] = True
    for to in g[v]:
        if not used[to]:
            dfs(to, g, used, res)
    res.append(v)


def top_sort(n, g):
    used = [False] * n
    res = []

    for v in range(n):
        if not used[v]:
            dfs(v, g, used, res)

    return res[::-1]


def solve():

    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        adj[u - 1].append(v - 1)

    res = top_sort(n, adj)

    print(" ".join(map(lambda x: str(x + 1), res)))

solve()
#Данный код представляет собой реализацию алгоритма топологической сортировки с использованием поиска в глубину (Depth-first search, DFS). Алгоритм принимает на вход количество вершин n и матрицу смежности графа adj. Алгоритм возвращает отсортированный по порядку обхода массив вершин.
