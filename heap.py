class Node:
    def __init__(self, key: str, val: int):
        self.left = None
        self.right = None
        self.val = val
        self.key = key


class minHeap:
    def __init__(self):
        self.arr = []

    def __heapify_down(self, n: int, i: int) -> None:
        smallest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and self.arr[l].val < self.arr[smallest].val:
            smallest = l
        if r < n and self.arr[r].val < self.arr[smallest].val:
            smallest = r
        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.__heapify_down(n, smallest)

    def __heapify_up(self, n: int):
        while n >= 2 and self.arr[n // 2 - 1].val > self.arr[n - 1].val:
            self.arr[n // 2 - 1], self.arr[n - 1] = (
                self.arr[n - 1],
                self.arr[n // 2 - 1],
            )
            n //= 2

    def push(self, node: Node) -> None:
        self.arr.append(node)
        n = len(self.arr)
        self.__heapify_up(n)

    def pop(self) -> Node:
        if len(self.arr) == 0:
            raise IndexError("pop from empty heap")
        x = self.arr[0]
        n = len(self.arr)
        self.arr[n - 1], self.arr[0] = self.arr[0], self.arr[n - 1]
        self.arr.pop()
        n -= 1
        self.__heapify_down(n, 0)
        return x

    def top(self) -> Node:
        if len(self.arr) == 0:
            raise IndexError("top from empty heap")
        return self.arr[0]

    def size(self) -> int:
        return len(self.arr)

    def empty(self) -> bool:
        return len(self.arr) == 0
