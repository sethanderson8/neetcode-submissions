class LRUCache:
    class ListNode:
        def __init__(self,key=0, val=0, prev=None, next=None):
            self.key = key
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = self.ListNode(-1, -1)
        self.tail = self.ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_to_node = {}
        
    # This is much better that using put as it does not require allocating more memory to a new node to be
    # placed in the list
    def _add_to_front(self, cur_node: ListNode):
        # Link node with head and the old first node
        cur_node.next = self.head.next
        cur_node.prev = self.head
        
        # Rewire self.head and the old first node's prev
        self.head.next.prev = cur_node
        self.head.next = cur_node

    def get(self, key: int) -> int:
        cur_pointer = self.key_to_node.get(key, None)

        if cur_pointer:
            # Manually delete it, no need to access the map via the delete method. 
            # we are just deleting it in the list to then add it to the front
            cur_pointer.prev.next = cur_pointer.next
            cur_pointer.next.prev = cur_pointer.prev
            # adding to the front here, also manually, in order to prevent extra memory allocation
            self._add_to_front(cur_pointer)
            return cur_pointer.val
        return -1

    def delete(self, cur_node: ListNode):
        del self.key_to_node[cur_node.key]
        cur_node.prev.next = cur_node.next
        cur_node.next.prev = cur_node.prev

    # cache: {2=20, 1=10}
    # cache: {3=30, 2=20}, key=1 was evicted
    def put(self, key: int, value: int) -> None:
        cur_node = self.key_to_node.get(key, None)
        if cur_node:
            # We are just replacing the val and putting this at front of linked list
            # first delete cur node
            self.delete(cur_node)

        else:
            if len(self.key_to_node) >= self.capacity:
                # delete LRU
                self.delete(self.tail.prev)        
        # put or new kv
        new_node = self.ListNode(key, value, self.head, self.head.next)
        self.key_to_node[key] = new_node
        self.head.next = new_node
        new_node.next.prev = new_node

    


        
