MOD = 10 ** 9 + 7
BASE = 31


def compute_hashes(s):
    n = len(s)
    hs = [0] * (n + 1)
    ps = [1] * (n + 1)

    for i in range(1, n + 1):
        hs[i] = (hs[i - 1] * BASE + ord(s[i - 1]) - ord('a') + 1) % MOD
        ps[i] = (ps[i - 1] * BASE) % MOD

    return hs, ps


def get_hash(hs, ps, l, r, n):
    if l == 0:
        return (hs[r] * ps[n]) % MOD
    return (((hs[r] - hs[l - 1] + MOD) % MOD) * ps[n - l]) % MOD

def equals(hs, ps, l, r, h, n):
    return get_hash(hs, ps, l, r, n) == (h * ps[n]) % MOD


def find_next(pos, n, m, ths, tps, phs):
    l = pos + 1
    r = n
    while r - l > 1:
        mid = (r + l) // 2
        if equals(ths, tps, pos, mid, phs[m], n):
            l = mid
        else:
            r = mid
    if equals(ths, tps, pos, r, phs, n):
        return r
    return l

def find_patterns(k, t, p):
    n, m = len(t), len(p)

    ths, tps = compute_hashes(t)
    phs, pwhs = compute_hashes(p)

    m = []

    for i in range(n - m + 1):
        mismatches = 0
        # for j in range(m):
        #     if t[i + j] != p[j]:
        #         mismatches += 1
        #     if mismatches > k:
        #
        #        break
        pos = i - 1
        for j in range(k + 1):
            pos = find_next(pos, n, m, ths, tps, phs)
            if pos == n:
                break
        if pos - 1 - i + 1 >= m:
            m.append(i)

    return m



with open("input.txt", "r") as f:
    strs = f.readline().strip().split()
    k, t, p = int(strs[0]), strs[1], strs[2]



m = find_patterns(k, t, p)

with open("output.txt", "w") as f:
    if len(m) == 0:
        f.write("0\n")
    else:
        f.write(f"{len(m)} " + " ".join(map(str, m)) + "\n")


