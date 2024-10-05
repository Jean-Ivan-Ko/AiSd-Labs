with open('input.txt', 'r') as file:
    N = int(file.readline())
    lectures = []

    for _ in range(N):
        si, fi = map(int, file.readline().split())
        lectures.append((si, fi))

lectures.sort(key=lambda x: x[1])

last = 0
count = 0


for lecture in lectures:
    start, end = lecture
    if start >= last:
        last = end
        count += 1

with open('output.txt', 'w') as file:
    file.write(str(count))