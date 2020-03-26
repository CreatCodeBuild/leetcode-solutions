class LinkedList:

    def __init__(self):
        self.head

class Node:

    def __init__(self, v):
        self.v = v
        self.next = None

    def add(self, v):
        if self.next:
            self.next.add(v)
        else:
            self.next = Node(v)

    def delete(self, index):
        pass

    def length(self):
        if self.next:
            return 1 + self.next.length()
        return 1
        