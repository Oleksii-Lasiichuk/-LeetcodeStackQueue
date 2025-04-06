class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        if self.head is None:
            self.tail = Node(item)
            self.head = self.tail
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    def pop(self):
        if self.head:
            item = self.head.item  # Return the item, not the Node
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return item
        raise ValueError('Queue is empty.')

    @property
    def peek(self):
        if self.head:
            return self.head.item  # Return the item, not the Node
        raise ValueError('Queue is empty.')

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def __bool__(self):
        return not self.is_empty()

    def __str__(self):
        s = ''
        current = self.head
        while current is not None:
            s += str(current.item) + ' '
            current = current.next
        return f'start -> {s}<- end'

class MyStack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x: int) -> None:
        self.queue1.add(x)

    def pop(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.add(self.queue1.pop())
        item = self.queue1.pop()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return item

    def top(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.add(self.queue1.pop())
        item = self.queue1.peek
        self.queue2.add(self.queue1.pop())
        self.queue1, self.queue2 = self.queue2, self.queue1
        return item

    def empty(self) -> bool:
        return not self.queue1 and not self.queue2