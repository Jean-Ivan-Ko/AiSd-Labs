import sys

sys.setrecursionlimit(10 ** 6)#Устанавливает лимит рекурсии


def is_bst(tree, idx, min_key, max_key):#Проверяет, является ли текущий элемент дерева допустимым ключом. Если нет, то возвращает False
    if idx == -1:
        return True

    key, l, r = tree[idx]

    if not (min_key < key < max_key):
        return False

    return is_bst(tree, l, min_key, key) and is_bst(tree, r, key, max_key)#Рекурсивно вызывает функцию is_bst для левого и правого поддеревьев


with open("input.txt", "r") as f:#Считывает количество элементов бинарного дерева из файла input.txt
    n = int(f.readline().strip())

    if n == 0:#Если количество элементов равно нулю, то дерево корректно, и код выводит «CORRECT» в файл output.txt
        with open("output.txt", "w") as out:
            out.write("CORRECT")
        exit(0)

    tree = [tuple(map(int, f.readline().split())) for _ in range(n)]#Создаёт бинарное дерево из данных, считанных из файла

if is_bst(tree, 0, -float('inf'), float('inf')):#Если функция возвращает True, то дерево является корректным, иначе — некорректным
    with open("output.txt", "w") as out:
        out.write("CORRECT")
else:
    with open("output.txt", "w") as out:
        out.write("INCORRECT")

