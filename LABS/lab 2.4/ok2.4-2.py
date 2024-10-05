

def decode(message: str) -> int:
    class CharState:
        def __init__(self, n: int, cnt: int):
            self.n = n
            self.cnt = cnt

    msg = message.strip()
    prev = {}
    states = []

    for idx, chr in enumerate(msg):
        if chr in prev:
            prev_idx = prev[chr]
            state = CharState(
                n = states[prev_idx].n + 1,
                cnt = states[prev_idx].cnt + states[prev_idx].n * (idx - prev_idx) + (idx - prev_idx - 1)
            )
        else:
            state = CharState(0, 0)

        states.append(state)
        prev[chr] = idx

    return sum(state.cnt for state in states)


with open("input.txt", "r") as infile:
    message = infile.readline().strip()

result = decode(message)

with open("output.txt", "w") as outfile:
    outfile.write(str(result) + "\n")
#Создаёт функцию decode, которая принимает строку message в качестве аргумента и возвращает целое число.

#Внутри функции decode создаётся класс CharState с двумя атрибутами: n и cnt. Атрибут n хранит количество повторений текущего символа, а атрибут cnt — сумму произведений количества повторений каждого символа на его индекс в строке.

#Строка msg инициализируется как копия строки message без пробелов в начале и конце. Затем создаётся пустой словарь prev для хранения индексов предыдущих символов. Также создаётся список states для хранения объектов класса CharState.

#В цикле for перебираются все символы строки msg. Если текущий символ уже есть в словаре prev, то используется его индекс для получения объекта CharState из списка states. Затем этот объект обновляется, увеличивая значение атрибута n на 1 и вычисляя новое значение атрибута cnt на основе предыдущего значения cnt, текущего значения n и индекса текущего символа относительно предыдущего символа.

#Если текущий символ не найден в словаре prev, создаётся новый объект CharState со значениями атрибутов n = 0 и cnt = 0.

#После обновления объекта CharState его добавляют в список states, а текущий символ добавляется в словарь prev с индексом текущего символа в качестве значения.

#Наконец, функция возвращает сумму значений атрибута cnt всех объектов CharState в списке states. Это значение сохраняется в переменной result.

#Далее код открывает файл input.txt для чтения, считывает строку из него и присваивает её переменной message. Затем вызывается функция decode с этой строкой в качестве аргумента, и результат сохраняется в переменной result.

#Наконец, код открывает файл output.txt для записи, записывает значение переменной result в файл и закрывает его.

