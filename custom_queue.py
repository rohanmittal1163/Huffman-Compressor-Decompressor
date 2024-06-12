class QueueNode:
    def __init__(self, node, code: str):
        self.node = node
        self.code = code


class Queue:
    def __init__(self):
        self.q = []

    def push(self, ele):
        self.q.append(ele)

    def pop(self):
        if len(self.q) == 0:
            raise IndexError("pop from empty queue")
        x = self.q[0]
        self.q.pop(0)
        return x

    def size(self):
        return len(self.q)

    def empty(self):
        return not len(self.q)

    def front(self):
        if len(self.q) == 0:
            raise IndexError("front from empty queue")
        return self.q[0]
