import math
from itertools import combinations

def dp(dist):
    n = len(dist)

    dist = [[dist[i][j] for j in range(n)] for i in range(n)]

    C = {}#словарь C пустыми значениями

    for k in range(1, n):#Заполняет начальные значения словаря
        C[(1 << k, k)] = (dist[0][k], 0)

    for sb_size in range(2, n):
        for subset in combinations(range(1, n), sb_size):#Для каждого размера подмножества выполняет перебор всех возможных подмножеств 
            bits = 0#Преобразует подмножество в битовую маску, используя побитовые операции
            for bit in subset:
                bits |= 1 << bit

            for k in subset:#Проходит по каждому элементу подмножества и вычисляет сумму расстояний между текущим элементом и всеми остальными элементами подмножества
                prev = bits & ~(1 << k)

                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + dist[m][k], m))
                C[(bits, k)] = min(res)#Сохраняет полученные суммы в словаре C как ключ (bits, k), где bits — битовая маска подмножества, а k — текущий элемент

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

def get_input():#запрашивает у пользователя количество элементов в множестве и считывает расстояния между ними
    with open("input.txt") as file:#я переделал на взятие из файла
        n = int(file.readline())
        dist = [list(map(int, line.split())) for line in file.readlines()]

    return dist

dist = get_input()
min_length, min_path = dp(dist)#возвращает два значения: минимальную сумму расстояний и путь, который привёл к этой сумме.
print(min_length)
print(' '.join(map(lambda x: str(x + 1), min_path[0:])))

with open("output.txt", "w") as outfile:
    outfile.write(str(min_length))
