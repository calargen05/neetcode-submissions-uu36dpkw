class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}  # Maps key -> Node
        
        # Create dummy boundaries
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """Helper to splice a node out of the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_tail(self, node: Node) -> None:
        """Helper to insert a node right before the dummy tail (Most Recently Used)."""
        prev_node = self.tail.prev
        
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            # Move to tail because it was recently accessed
            self._remove(node)
            self._add_to_tail(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            # Key exists: update value and move to tail
            node = self.map[key]
            node.val = value
            self._remove(node)
            self._add_to_tail(node)
        else:
            # New key: check capacity first
            if len(self.map) == self.capacity:
                # Evict the LRU node (right after dummy head)
                lru_node = self.head.next
                self._remove(lru_node)
                del self.map[lru_node.key]
                
            # Insert the new node
            new_node = Node(key, value)
            self._add_to_tail(new_node)
            self.map[key] = new_node