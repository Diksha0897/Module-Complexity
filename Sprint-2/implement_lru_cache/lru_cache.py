class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LruCache:
    def __init__(self, limit: int):
        if limit <= 0:
            raise ValueError("limit must be greater than 0")

        self.limit = limit
        self.map = {}

        # dummy head/tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _move_to_front(self, node: Node):
        self._remove(node)
        self._add_to_front(node)

    def _evict_if_needed(self):
        if len(self.map) > self.limit:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]

    def get(self, key):
        node = self.map.get(key)
        if not node:
            return None

        self._move_to_front(node)
        return node.value

    def set(self, key, value):
        node = self.map.get(key)

        if node:
            node.value = value
            self._move_to_front(node)
        else:
            node = Node(key, value)
            self.map[key] = node
            self._add_to_front(node)
            self._evict_if_needed()