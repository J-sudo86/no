class Queue:
    def __init__(max, self):
        self._max = max
        self._list = [None] * max
        self._front = 0
        self._rear = 0 
        self._avaliable = max
    def enter(self, value):
        if self._available == 1:
            if self.front != 0:
                
        if self._available == 0:
            return
        self._list[self._rear] = value
        self._rear += 1
        self._availble -= 1
    def dequeue(self):
        if self._available == self._max:
            return
        self._list[self._front] = None
        self._front += 1
        self._available += 1
    def display(self):
        return self._list
    def front_value(self):
        return self._list[self._front]
    def rear_value(self):
        return self._list[self._rear]

queue = Queue