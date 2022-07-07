from Stack import Stack  # импорт стека
from pprint import pprint  # импорт красивого вывода (стандартная библиотека)

# в скрипте вершины начинаются с 0, данная переменная для улучшения вывода
PRINTABLE_ADD = 1


# преобразование матрицы в список смежности
def matrix_to_list(matrix):
    # список смежности
    li = []
    # перебор строк матрицы
    for i in range(len(matrix)):
        # список потомков
        line = []
        # перебор элементов строки
        for j in range(len(matrix[i])):
            # если на пересечении 1, то добавить в потомки
            if matrix[i][j] == 1:
                line.append(j)  # append - добавляет элемент в массив потомков

        # добавить список потомков в список смежности
        li.append(line)

    return li


# метод поиска в глубину
def dfs(x):
    global rec_level

    # увеличиваем глубину рекурсии и соответствующие глубинные значения
    rec_level += 1
    Dnum[x] = rec_level
    Low[x] = rec_level

    # если узел изолированный
    if len(graph[x]) == 0:
        all_blocks.append([x + PRINTABLE_ADD])
        return

    # помещение x в стек
    S.push(x)

    # перебор смежных вершин x
    for y in graph[x]:
        # если вершина не посещалась
        if Dnum[y] == 0:
            dfs(y)

            # изменение наименьшей глубинны вершины
            Low[x] = min(Low[x], Low[y])

            # если глубина родителя == минимальной глубине потомка,
            # то создаётся новый блок
            if Low[y] == Dnum[x]:
                all_blocks.append(new_block(x, y))
        else:
            # изменение наименьшей глубинны вершины
            Low[x] = min(Low[x], Dnum[y])


# метод создания блока
def new_block(x, y) -> list:
    # временный блок
    B = [x + PRINTABLE_ADD]

    while True:
        # защита от пустого стека
        if S.is_empty():
            return B

        # извлечение из стека
        z = S.pop()
        # помещение вершины в блок
        B.append(z + PRINTABLE_ADD)

        # условие выхода из цикла
        if z == y:
            return B


# **********************************************************************************************************************
# ******************************************* запуск скрпита  **********************************************************
# **********************************************************************************************************************
if __name__ == '__main__':
    # массив для хранения графа
    matrix_graph = []

    # чтение из файла
    with open('matrix.txt', 'r') as f:
        lines = [row.strip() for row in f]
        for line in lines:
            matrix_graph.append(list(map(int, line.split())))

    # вывод считанного графа
    pprint(matrix_graph)

    # матрица -> список смежности
    graph = matrix_to_list(matrix_graph)

    # обнуление переменных
    S = Stack()               # стек
    Dnum = [0] * len(graph)   # глубинный номер
    Low = [0] * len(graph)    # наименьшие из глубинных номеров вершин
    all_blocks = []           # список для хранения блоков
    rec_level = 0             # уровень рекурсии (c)

    # проход по вершинам
    for x in range(len(graph)):
        if Dnum[x] == 0:
            dfs(x)

    # вывод полученных блоков
    print(all_blocks)
