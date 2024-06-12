from custom_queue import Queue, QueueNode
from heap import minHeap, Node


class BinaryTree:
    def __init__(self, pq: minHeap):
        self.root = None
        self.pq = pq

    def build_binary_tree(self) -> None:
        while self.pq.size() != 1:
            t1 = self.pq.top()
            self.pq.pop()
            t2 = self.pq.top()
            self.pq.pop()
            node = Node(None, t1.val + t2.val)
            node.left = t1
            node.right = t2
            self.pq.push(node)
        self.root = self.pq.top()

    def inorder(self) -> None:
        curr = self.root
        while curr:
            if curr.left == None:
                print(curr.val)
                curr = curr.right
            else:
                temp = curr.left
                while temp.right and temp.right != curr:
                    temp = temp.right
                if temp.right:
                    temp.right = None
                    print(curr.val)
                    curr = curr.right
                else:
                    temp.right = curr
                    curr = curr.left

    def preorder(self) -> None:
        curr = self.root
        while curr:
            if curr.left == None:
                print(curr.val)
                curr = curr.right
            else:
                temp = curr.left
                while temp.right and temp.right != curr:
                    temp = temp.right
                if temp.right:
                    temp.right = None
                    curr = curr.right
                else:
                    temp.right = curr
                    print(curr.val)
                    curr = curr.left

    def postorder(self) -> None:
        curr = self.root
        while curr:
            if curr.right == None:
                print(curr.val)
                curr = curr.left
            else:
                temp = curr.right
                while temp.left and temp.left != curr:
                    temp = temp.left
                if temp.left:
                    temp.left = None
                    curr = curr.left
                else:
                    temp.left = curr
                    print(curr.val)
                    curr = curr.right

    def extract_code(self) -> dict:
        q = Queue()
        node = self.root
        queNode = QueueNode(node, "")
        q.push(queNode)
        code_dict = {}
        while q.empty() == False:
            queNode = q.front()
            q.pop()
            node = queNode.node
            code = queNode.code
            if node.key == None:
                if node.left:
                    q.push(QueueNode(node.left, code + "0"))
                if node.right:
                    q.push(QueueNode(node.right, code + "1"))
            else:
                code_dict[node.key] = code

        return code_dict
