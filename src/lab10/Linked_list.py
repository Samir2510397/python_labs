class Node:#узел
    def __init__(self, value, next=None):
        self.value = value #данные узла
        self.next = next #ссылка на след. узел


class SinglyLinkedList:
    def __init__(self):
        self.head = None #указатель первого узла
        self.tail = None #указатель последнего узла
        self._size = 0 # кол-во элементов

    def append(self, value):#добавляем элемент в конец
        new_n = Node(value)# создаем новый узел
        if self.head == None:#если список пуст, новый узел становится и головой и хвостом
            self.head = new_n
            self.tail = new_n
        else:#если не пуст
            self.tail.next = new_n #старых хвост теперь не хвост
            self.tail = new_n # новый узел теперь хвост
        self._size += 1 # увеличиваем размер

    def prepend(self, value):#добавление элемента в начало
        new_n = Node(value)#создаем новый узел
        if self.head == None:
            self.head = new_n
            self.tail = new_n
        new_n.next = self.head#новый узел ссылается на старую голову
        self.head = new_n#новый узел становится головой
        self._size += 1 # увеличиваем размер

    def insert(self, idx: int, value):#вставка по индексу
        if idx < 0 or idx > self._size:# проверка индекса
            raise IndexError
        new_n = Node(value)
        if idx == 0:#вставка в начало
            new_n.next = self.head
            self.head = new_n
            self._size += 1
            return
        if idx == self._size:#вставка в конец
            self.tail.next = new_n
            self.tail = new_n
            self._size += 1
            return
        c = 0 #вставка в середину
        prev = None
        curr = self.head
        while curr != None:
            if c == idx:
                prev.next = new_n
                new_n.next = curr

                break
            prev = curr
            curr = curr.next
            c += 1

        self._size += 1 #увеличиваем размер

    def remove_at(self, idx: int):#удаление по индексу
        if idx < 0 or idx >= self._size:#проверка индекса
            raise IndexError
        if idx == 0:#удаление головы
            self.head = self.head.next
            self._size -= 1
            return

        curr = self.head#удаление середины и конца
        for i in range(idx-1):
            curr = curr.next

        value = self.head.value

        if curr.next == self.tail:#удаление конца
            self.tail = curr

        curr.next = curr.next.next
        self._size -= 1
        return


    def __iter__(self):#итератор
        curr = self.head
        while curr != None:
            yield curr.value
            curr = curr.next

    def __len__(self):
        return self._size

    def __repr__(self):#строковое представление для вывода
        return f"SinglyLinkedList({list(self)})"


# test SinglyLinkedList
sll = SinglyLinkedList()
print(f"1. Пустой список: {sll}")
sll.append(7)
sll.append(8)
sll.append(10)
sll.append(20)
sll.append(30)
print(f"2. Добавление в конец (10, 20, 30): {sll}")
sll.prepend(5)
print(f"3. Добавление в начало (5): {sll}")
sll.insert(2, 15)
print(f"4. Вставка 15 по индексу 2: {sll}")
sll.insert(0, 1)
print(f"5. Вставка 1 по индексу 0: {sll}")
sll.insert(8, 100)
print(f"6. Вставка 100 в конец: {sll}")
sll.remove_at(4)
print(f"7. Удаление 8 (середина): {sll}")
sll.remove_at(0)
print(f"8. Удаление 1 (голова): {sll}")
sll.remove_at(6)
print(f"9. Удаление 100 (хвост): {sll}")
print(f"10. Размер: {len(sll)}")
print(f"11. Пуст ли список? {len(sll) == 0}")

