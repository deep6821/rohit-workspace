"""
- A Least Recently Used (LRU) Cache organizes items in order of use,
- To quickly identify which item is being used for the recent amount of time & which items are used for the least
amount of time.
- A Cache is a temporary storage. Reading from Cache takes less time than going all over the network again and
again. But Cache has limited memory.
- LRU Cache is an efficient data structure that can be used to figure out what we should evict when the cache
is full.

** The goal is always to have the least recently used item accessible in O(1) time. We also want to insert into
the cache in O(1) time. Therefore, get, set should always run in constant time.
** This is the reason we use a hash map or a static array (of a given size with an appropriate hash function) to
retrieve items in constant time.
** LRU cache is built by combining two data structure: Doubly Linked List and Hash Map
** spacc: O(n) in worst Case

Examples:
Recent Files in our Desktop
Amazon Prime, Netflix have LRU Cache Memory.
"""
from collections import OrderedDict


class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity > 0")

        self.capacity = capacity
        self.current_size = 0
        self.hash_map = dict()
        self.head = None
        self.tail = None

    def _add(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.prev = self.head
            self.head.next = node
            self.head = node

        self.current_size += 1

    def _remove(self, node):
        if not self.head:
            return

        # Removing the node from somewhere in the middle; update pointers
        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        # head = tail = node
        if not node.next and not node.prev:
            self.head = None
            self.tail = None

        # If the node we are removing is the one at the end, update the new end
        # also not completely necessary but set the new end's previous to be NULL
        if self.tail == node:
            self.tail = node.next
            self.tail.prev = None

        self.current_size -= 1
        return node

    def get(self, key):
        node = self.hash_map[key]
        if key not in self.hash_map:
            return -1

        # Just return the value if we are already looking at head
        if self.head == node:
            return node.value

        self._remove(node)
        self._add(node)
        return node.value

    def set(self, key, value):
        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value

            # Update pointers only if this is not head; otherwise return
            if self.head != node:
                self._remove(node)
                self._add(node)
        else:
            new_node = Node(key, value)
            if self.current_size == self.capacity:
                del self.hash_map[self.tail.key]
                self._remove(self.tail)

            self._add(new_node)
            self.hash_map[key] = new_node


class LRUCache2:
    def __init__(self, capacity: int):  # capacity: 2
        self.cache = OrderedDict()
        self.capacity = capacity

    # We return the value of the key that is queried in O(1) and return -1 if we don't find the key in out
    # dict / cache. And also move the key to the end to show that it was recently used.
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    # First, we add / update the key by conventional methods.
    # And also move the key to the end to show that it was recently used.
    # But here we will also check whether the length of our
    # ordered dictionary has exceeded our capacity,
    # If so we remove the first key (least recently used)
    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


if __name__ == "__main__":
    cache = LRUCache(3)
    cache.set(1, 1)
    cache.set(10, 15)
    cache.set(15, 10)
    cache.set(10, 10)
    print(cache.get(1))
    print(cache.get(15))
