import sys

sys.setrecursionlimit(10 ** 6)


def is_bst(tree, idx, min_key, max_key):
    if idx == -1:
        return True

    key, l, r = tree[idx]

    if not (min_key < key < max_key):
        return False

    return is_bst(tree, l, min_key, key) and is_bst(tree, r, key, max_key)


with open("input.txt", "r") as f:
    n = int(f.readline().strip())

    if n == 0:
        with open("output.txt", "w") as out:
            out.write("CORRECT")
        exit(0)

    tree = [tuple(map(int, f.readline().split())) for _ in range(n)]

if is_bst(tree, 0, -float('inf'), float('inf')):
    with open("output.txt", "w") as out:
        out.write("CORRECT")
else:
    with open("output.txt", "w") as out:
        out.write("INCORRECT")

