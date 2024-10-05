import math
from itertools import combinations

def dp(dist):
    n = len(dist)

    dist = [[dist[i][j] for j in range(n)] for i in range(n)]

    C = {}

    for k in range(1, n):
        C[(1 << k, k)] = (dist[0][k], 0)

    for sb_size in range(2, n):
        for subset in combinations(range(1, n), sb_size):
            bits = 0
            for bit in subset:
                bits |= 1 << bit

            for k in subset:
                prev = bits & ~(1 << k)

                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + dist[m][k], m))
                C[(bits, k)] = min(res)

    bits = (2 ** n - 1) - 1
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + dist[k][0], k))
    opt, parent = min(res)

    path = []
    for i in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits

    path.append(0)

    return opt, list(reversed(path))

def get_input():
    with open("input.txt") as file:
        n = int(file.readline())
        dist = [list(map(int, line.split())) for line in file.readlines()]

    return dist

dist = get_input()
min_length, min_path = dp(dist)
print(min_length)
print(' '.join(map(lambda x: str(x + 1), min_path[0:])))

with open("output.txt", "w") as outfile:
    outfile.write(str(min_length))
