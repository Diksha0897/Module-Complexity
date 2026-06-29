class Node:
    __slots__ = ("value", "prev", "next")

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, value):
        node = Node(value)

        if self.head is None:
            self.head = self.tail = node
            return node

        node.next = self.head
        self.head.prev = node
        self.head = node
        return node

    def pop_tail(self):
        if self.tail is None:
            return None

        node = self.tail
        value = node.value

        if node.prev is None:
            self.head = self.tail = None
        else:
            self.tail = node.prev
            self.tail.next = None

        return value

    def remove(self, handle):
        if handle is None:
            return

        # reconnect prev
        if handle.prev:
            handle.prev.next = handle.next
        else:
            self.head = handle.next

        # reconnect next
        if handle.next:
            handle.next.prev = handle.prev
        else:
            self.tail = handle.prev

        handle.prev = None
        handle.next = None