def solve():
    n = int(input())
    c = [0] * n
    for i in range(n):
        c[i] = int(input())

    mx = n + 1

    dp = [[float('inf')] * mx for _ in range(n + 1)]
    dp[0][0] = 0

    used = [[False] * mx for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(mx):
            if c[i - 1] <= 100:
                if dp[i][j] > dp[i - 1][j] + c[i - 1]:
                    dp[i][j] = dp[i - 1][j] + c[i - 1]
                    used[i][j] = False
            else:
                if j > 0 and dp[i][j] > dp[i - 1][j - 1] + c[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + c[i - 1]
                    used[i][j] = False

            if j < mx - 1 and dp[i][j + 1] > dp[i - 1][j]:
                dp[i][j + 1] = dp[i - 1][j]
                used[i][j + 1] = True

    min_cost = min(dp[n])
    remain = dp[n].index(min_cost)

    used_days = []
    i = n
    j = remain
    while i > 0:
        if used[i][j]:
            used_days.append(i)
            j -= 1
        i -= 1

    used_days.reverse()

    print(min_cost)
    print(remain, len(used_days))
    for day in used_days:
        print(day)

solve()
