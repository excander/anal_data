from collections import deque

class Node:
    def __init__(self, value):
        self.l = None
        self.r = None
        self.data = value

class BinarySearchTree():

    def __init__(self, value = None):
        self._deq = deque()
        if value is None:
            self.root = None
        else:
            self.root = Node(value)
            self._deq.append(self.root)

    def append(self, value):
        if(self.root is None):
            self.root = Node(value)
            self._deq.append(self.root)
        else:
            self._add(value, self.root)


    def _add(self, value, node):
        if(value < node.data):
            if(node.l is not None):
                self._add(value, node.l)
            else:
                node.l = Node(value)
        else:
            if(node.r is not None):
                self._add(value, node.r)
            else:
                node.r = Node(value)

    def __contains__(self, value):
        if(self.root is not None):
            return self._find(value, self.root)
        else:
            return False
    
    def _find(self, value, node):
        if node.data == value:
            return True
        elif value < node.data:
            if node.l is None:
                return False
            else:
                return self._find(value, node.l)
        elif value > node.data:
            if node.r is None:
                return False
            else:
                return self._find(value, node.r)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._deq):
            return self._bfs(self._deq.popleft())
        else:
            if self.root is not None:
                self._deq.append(self.root) 
            raise StopIteration

    def _bfs(self, node):
        if node.l is not None:
            self._deq.append(node.l)
        if node.r is not None:
            self._deq.append(node.r)
        return node.data




# if __name__ == '__main__':
#     tree = BinarySearchTree()
#     for v in [5, 0, 6, 2, 1, 3]:
#         tree.append(v)

#     for v in [6, 12]:
#         print(v in tree)

#     print(*tree)

if __name__ == '__main__':
    tree = BinarySearchTree()
    for v in [8, 3, 10, 1, 6, 4, 14, 13, 7, 9]:
        tree.append(v)

    for v in [8, 0, 13]:
        print(v in tree)

    print(*tree)