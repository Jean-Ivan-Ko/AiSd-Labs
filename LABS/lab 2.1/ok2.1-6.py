from functools import cmp_to_key


def comp(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0


def solve(a):
    a = list(map(str, a))

    srt = sorted(a, key=cmp_to_key(comp))

    result = ''.join(srt)

    if result[0] == '0':
        return '0'

    return result



with open("input.txt", "r") as infile:
    n = int(infile.readline().strip())
    a = list(map(int, infile.readline().split()))

result = solve(a)

with open("output.txt", "w") as outfile:
    outfile.write(result)



