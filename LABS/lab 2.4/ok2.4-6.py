s = input()
n = len(s)
z = [0] * n
z[0] = n
l = 0
r = 0
for i in range(1, n):
    if i <= r:
        z[i] = min(r - i + 1, z[i - l])
    while i + z[i] < n and s[z[i]] == s[i + z[i]]:
        z[i] += 1
    if i + z[i] - 1 > r and z[i] != 0:
        r = i + z[i] - 1
        l = i
print(*z)