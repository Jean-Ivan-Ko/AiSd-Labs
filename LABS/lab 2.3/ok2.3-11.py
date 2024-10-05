from collections import deque


def alchemy(reactions, start, target):

    g = {}
    used = {}
    for reaction in reactions:
        x, y = reaction.split('->')
        if x.strip() in g:
            g[x.strip()].append(y.strip())
        else:
            g[x.strip()] = [y.strip()]
            used[x.strip()] = 0
        if not (y.strip() in g):
            g[y.strip()] = []
            used[y.strip()] = 0

    queue = deque([(start, 0)])

    used[start] = 1
    while queue:
        cur, moves = queue.popleft()

        if cur == target:
            return moves

        for to in g[cur]:
            if not used[to]:
                used[to] = 1
                queue.append((to, moves + 1))

    return -1


def solve():
    m = int(input().strip())
    reactions = [input().strip() for _ in range(m)]
    start = input().strip()
    target = input().strip()

    result = alchemy(reactions, start, target)

    print(result)


solve()
