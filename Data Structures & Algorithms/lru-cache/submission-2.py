class LRUCache:
    class ListNode:
        def __init__(self,key=0, val=0, prev=None, next=None):
            self.key = key
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cur_capacity = 0
        self.head = self.ListNode(-1, -1)
        self.tail = self.ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_to_node = {}
        

    def get(self, key: int) -> int:
        cur_pointer = self.key_to_node.get(key, None)

        if cur_pointer:
            # delete it in the doubly linked list
            self.delete(cur_pointer)
            self.put(cur_pointer.key, cur_pointer.val)
            return cur_pointer.val
        else:
            return -1

    def delete(self, cur_node: ListNode):
        self.cur_capacity -= 1
        del self.key_to_node[cur_node.key]
        cur_node.prev.next = cur_node.next
        cur_node.next.prev = cur_node.prev

    # cache: {2=20, 1=10}
    # cache: {3=30, 2=20}, key=1 was evicted
    def put(self, key: int, value: int) -> None:
        cur_node = self.key_to_node.get(key, None)
        self.cur_capacity += 1
        if cur_node:
            # We are just replacing the val and putting this at front of linked list
            # first delete cur node
            self.delete(cur_node)

        else:
            if self.cur_capacity > self.capacity:
                # delete LRU
                self.delete(self.tail.prev)        
        # put or new kv
        new_node = self.ListNode(key, value, self.head, self.head.next)
        self.key_to_node[key] = new_node
        self.head.next = new_node
        new_node.next.prev = new_node

    


        
