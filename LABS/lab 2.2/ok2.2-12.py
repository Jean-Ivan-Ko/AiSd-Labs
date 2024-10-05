import sys
sys.setrecursionlimit(200000)

with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    if n == 0:
        # Если дерево пустое
        with open('output.txt', 'w') as output_file:
            output_file.write("")
        sys.exit()

    tree = []
    for _ in range(n):
        tree.append(list(map(int, file.readline().split())))

h = [-1] * n

bals = [-1] * n

def calc(ind):
    if ind == 0:
        return 0

    ind -= 1
    if h[ind] != -1:
        return h[ind]

    key, left, right = tree[ind]

    left = calc(left)
    right = calc(right)

    h[ind] = 1 + max(left, right)

    bals[ind] = right - left

    return h[ind]

calc(1)

with open('output.txt', 'w') as output_file:
    for balance in bals:
        output_file.write(f"{balance}\n")
