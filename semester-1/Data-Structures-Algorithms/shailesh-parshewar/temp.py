
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None
    def push(self, node):
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

n1 = Node(0)
n2 = Node(2)
n3 = Node(5)
n4 = Node(45)

li = linked_list()
li.push(n1)
li.push(n2)
li.push(n3)
li.push(n4)
li.print()