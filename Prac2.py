class ArrayQueue:

    DEFAULT_CAPACITY = 10

    def _init_(self):

        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        self._back = 0

    def _len_(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._data[self._front]

    def dequeueFirst(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        self._back = (self._front + self._size - 1) % len(self._data)
        return answer

    def dequeueBack(self):

        if self.is_empty():
            raise Empty('Queue is empty')
        back = (self._front + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None
        self._front = self._front
        self._size -= 1
        self._back = (self._front + self._size - 1) % len(self._data)
        return answer

    def enqueuelast(self, e):

        if self._size == len(self._data):
            self._resize(2 * len(self.data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
        self._back = (self._front + self._size - 1) % len(self._data)

    def enqueueFirst(self, e):

        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        avail = (self._front + self._size) % len(self._data)
        self._data[self._front] = e
        self._size += 1
        self._back = (self._front + self._size - 1) % len(self._data)

    def _resize(self, cap):

        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
        self._back = (self._front + self._size - 1) % len(self._data)

    def display(self):
        return self._data


l1 = ArrayQueue()
l1.enqueueFirst(3)
l1.enqueueFirst(5)
l1.enqueueFirst(6)
l1.enqueuelast(7)
l1.enqueuelast(8)

print(f"full lisr {l1._data()}")
print(f"len of list {l1._len_()}")
print(
    f"first value is {l1._data[l1._front]} last value is {l1._data[l1._back]}")

l1.dequeueFirst(3)
l1.dequeuelast(7)
l1.dequeuelast(8)

print(f"full lisr {l1._data()}")
print(f"len of list {l1._len_()}")
print(
    f"first value is {l1._data[l1._front]} last value is {l1._data[l1._back]}")
