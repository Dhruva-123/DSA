#### Do the answer as a doubly linked list and a mapping(for get and put. Make sure the dict is like this {key : node(key, vlaue, prev, next)}). Far easier than anything else. The question asks you for O(1) get and put. A doubly linked list can do that. 


class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.mapping = {}  # key -> Node

        # Dummy head/tail sentinels to avoid null-checks at the boundaries.
        # head.next = most recently used, tail.prev = least recently used
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        # Unlink node from its current position
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node):
        # Insert node right after head (marks it as most recently used)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.mapping:
            return -1
        node = self.mapping[key]
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key, value):
        if key in self.mapping:
            node = self.mapping[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.mapping) >= self.capacity:
                # Evict least recently used = node just before tail
                lru = self.tail.prev
                self._remove(lru)
                del self.mapping[lru.key]

            new_node = Node(key, value)
            self.mapping[key] = new_node
            self._add_to_front(new_node)