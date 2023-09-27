class Node:
    def __init__(self, key,value):
        self.key, self.val  = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev= self.right, self.left


    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next=next
        next.prev=prev
        return node
    
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next=node
        next.prev=node
        node.prev, node.next=prev, next

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.remove(self.cache[key])
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
             self.remove(self.cache[key])
        self.cache[key]= Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache)>self.capacity:
            node = self.left.next
            self.remove(node)
            del self.cache[node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)