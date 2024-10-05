def calc(d, m, stops):
    stops = [0] + stops + [d]
    cnt = 0
    cur = 0
    n = len(stops) - 1

    while cur < n:
        last = cur

        while cur < n and stops[cur + 1] - stops[last] <= m:
            cur += 1

        if cur == last:
            return -1

        if cur < n:
            cnt += 1

    return cnt


with open("input.txt", "r") as infile:
    d = int(infile.readline().strip())
    m = int(infile.readline().strip())
    n = int(infile.readline().strip())
    stops = list(map(int, infile.readline().split()))

result = calc(d, m, stops)

with open("output.txt", "w") as outfile:
    outfile.write(str(result) + "\n")

