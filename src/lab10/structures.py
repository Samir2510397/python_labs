from collections import deque


class Stack:#Создаем пустой стек
    def __init__(self):
        self._data = []#пустой список для хранения

    def push(self, item):#добавляем элемент на вершину
        self._data.append(item)

    def pop(self):#удаляем элементы с вершины(без элементов удаляет последний)
        if self.is_empty():
            raise IndexError("Стек пуст, удалять нечего")
        return self._data.pop()

    def peek(self):#показывает эелент вершины без удаления
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self):#проверяем пустоту стека
        return len(self._data) == 0

    def __len__(self):#кол-во элементов в стеке
        return len(self._data)


class Queue:#создаем пустую куешку
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):#добавляем элемент в конец куешки
        self._data.append(item)

    def dequeue(self):#удаляем и выводим элемент из начала куешки
        if self.is_empty():
            return IndexError
        return self._data.popleft()

    def peek(self):#смотрим первый элемент куешки
        if not self._data:
            return None
        return self._data[0]

    def is_empty(self) -> bool:#проверка на пустоту
        return not self._data

    def __len__(self):#кол-во элементов в куешке
        return len(self._data)


if __name__ == '__main__':#проверка
    s = Stack()
    s.push(6)
    s.push(3)
    print(s.pop())
    print(s.peek())
    print(s.__len__())
    print(s.is_empty())
    s.pop()
    print(s.is_empty())

    q = Queue()
    q.enqueue(6)
    q.enqueue(4)
    print(q.dequeue())
    print(q.peek())
    print(q.__len__())
    print(q.is_empty())
    q.dequeue()
    print(q.is_empty())