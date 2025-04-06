class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        self.head = Node(item, self.head)

    def pop(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        item = self.head.item
        self.head = self.head.next
        return item

    @property
    def peek(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        else:
            return self.head.item

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count +=1
            current = current.next
        return count

    def __str__(self):
        s = ''
        current = self.head
        while current is not None:
            s = str(current.item) + ' ' +s
            current = current.next
        return 'bottom -> '+ s+'<- top'

class MyQueue:

    def __init__(self):
        self.stack1 = []  # For pushing elements
        self.stack2 = []  # For popping/peeking elements

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2
        





         