"""
Problem Statement:
------------------
Least Recently Used (LRU) is a common caching strategy. It defines the policy
to evict elements from the cache to make room for new elements when the cache
is full, meaning it discards the least recently used items first.

Example: Let’s take an example of a cache that has a capacity of 4 elements
--------
1. We cache elements 1, 2, 3 and 4.
   1 -> 2 -> 3 -> 4
2. Now need to cache another element 5.
    2 -> 3 -> 4 -> 5


In LRU cache, we evict the least recently used element (in this case “1”) in
case a new element needs to be cached. Now “2” is next in line to be evicted
if a new element needs to be cached. Let’s see what happens when “2” is
accessed again.

    3 -> 4 -> 5 -> 2


Solution Explanation:
---------------------
Runtime Complexity:
  get (hashset): O(1) in the average case, O(n) in the worst case
  set (hashset): Constant, O(1)

  deletion at head when adding a new element (linked list): Constant, O(1)
  search for deleting and adding to tail (linked list): O(n)

Memory Complexity:
Linear, O(n) where n is the size of cache.


-------------------------------------------------------------------------------

Caching is a technique to store data in a faster storage (usually RAM) to serve
future requests faster. Below are some common examples where cache is used:

    1. A processor cache is used to read data faster from main memory (RAM).
    2. Cache in RAM can be used to store part of disk data in RAM and serve
       future requests faster.
    3. Network responses can be cached in RAM to avoid too many network calls.

However, cache store is usually not big enough to store the full data set. So
we need to evict data from the cache whenever it becomes full. There are a
number of caching algorithms to implement a cache eviction policy. LRU is very
simple and a commonly used algorithm. The core concept of the LRU algorithm is
to evict the oldest data from the cache to accommodate more data.

To implement an LRU cache we use two data structures: a hashmap and a doubly
linked list. A doubly linked list helps in maintaining the eviction order and a
hashmap helps with O(1) lookup of cached keys. Here goes the algorithm for LRU
cache.

*** Note that the doubly linked list is used to keep track of the most recently
accessed elements. The element at the tail of the doubly linked list is the
most recently accessed element. All newly inserted elements (in put) go the
tail of the list. Similarly, any element accessed (in get operation) goes to
the tail of the list.
"""


class LinkedNode(object):
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookup = {}
        self.dummy = LinkedNode(0, 0)
        self.head = self.dummy.next
        self.tail = self.dummy.next

    def remove_head_node(self):
        if not self.head:
            return
        prev = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        del prev

    def append_new_node(self, new_node):
        """  add the new node to the tail end
        """
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = self.tail.next

    def unlink_cur_node(self, node):
        """ unlink current linked node
        """
        if self.head is node:
            self.head = node.next
            if node.next:
                node.next.prev = None
            return

        # removing the node from somewhere in the middle; update pointers
        prev, nex = node.prev, node.next
        prev.next = nex
        nex.prev = prev

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1

        node = self.lookup[key]

        if node is not self.tail:
            self.unlink_cur_node(node)
            self.append_new_node(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.lookup[key].val = value
            self.get(key)
            return

        if len(self.lookup) == self.capacity:
            # remove head node and correspond key
            self.lookup.pop(self.head.key)
            self.remove_head_node()

        # add new node and hash key
        new_node = LinkedNode(val=value, key=key)
        self.lookup[key] = new_node
        self.append_new_node(new_node)


obj = LRUCache(capacity=5)
obj.put("Rohit", 1)
print(obj.get("Rohit"))