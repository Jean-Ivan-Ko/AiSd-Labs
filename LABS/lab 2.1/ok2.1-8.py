with open('input.txt', 'r') as file:
    N = int(file.readline())#количество пар чисел, которые будут считаны из файла
    lectures = []#будут добавляться пары чисел

    for _ in range(N):#В цикле считывает N строк из файла, преобразует их в пары целых чисел 
        si, fi = map(int, file.readline().split())
        lectures.append((si, fi))

lectures.sort(key=lambda x: x[1])#Сортирует список lectures по второму элементу каждой пары (по времени окончания лекции)

last = 0#время окончания последней прочитанной лекции
count = 0


for lecture in lectures:#Для каждой пары проверяет, больше ли время начала лекции start, чем время окончания предыдущей лекции
    start, end = lecture
    if start >= last:
        last = end
        count += 1

with open('output.txt', 'w') as file:
    file.write(str(count))
