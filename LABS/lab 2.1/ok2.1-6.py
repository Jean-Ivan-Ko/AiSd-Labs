from functools import cmp_to_key# позволяет преобразовать функцию сравнения в ключ для сортировки элементов


def comp(a, b):#сравнивает два числа и возвращает -1, если первое число больше второго, 1 — если первое меньше второго, и 0 — если они равны
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0


def solve(a):
    a = list(map(str, a))#Преобразует входной список чисел в список строк

    srt = sorted(a, key=cmp_to_key(comp))#Сортирует строки в алфавитном порядке 

    result = ''.join(srt)#Объединяет отсортированные строки в одну строку

    if result[0] == '0':
        return '0'

    return result



with open("input.txt", "r") as infile:#Читает данные
    n = int(infile.readline().strip())#целое число n
    a = list(map(int, infile.readline().split()))# n целых чисел, которые записываются в список a

result = solve(a)

with open("output.txt", "w") as outfile:
    outfile.write(result)



