class Stack:
    # инициализация
    def __init__(self):
        self.items = []

    # помещение в стек
    def push(self, item):
        self.items.append(item)

    # извлечение из стека
    def pop(self):
        return self.items.pop()

    # проверка на пустоту стека
    def is_empty(self):
        return self.items == []
