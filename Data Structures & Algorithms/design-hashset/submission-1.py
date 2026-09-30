class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        # If no root yet, return new node
        if not root:
            return TreeNode(key)
        elif key < root.key:
            # left
            root.left = self.insert(root.left, key)
        else: 
            # right
            root.right = self.insert(root.right, key)

        return root

    def delete(self, root, key):
        if not root:
            # if no root, nothing to delete
            return None
        elif key < root.key:
            # left - recurse on the left to find and delete it
            root.left = self.delete(root.left, key)
        elif key > root.key: 
            # right - recurse on the right to find and delete it
            root.right = self.delete(root.right, key)
        else:
            # this is when we actually find the node to delete
            # If only one child or no childs
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # Case where there are two children
            # temp value for the in order sucessor, the min value on the right side
            temp = self.minValueNode(root.right)

            # we then set our root key to the temp (min val on right side) key
            root.key = temp.key

            # Now we go ahead and delete the (temp's og node, min val on right side)
            # since it will only have 0 or 1 child
            root.right = self.delete(root.right, temp.key)
        return root
        
    def minValueNode(self, root):
        while root.left:
            root = root.left
        return root

    def search(self, root, key):
        if not root:
            return False
        elif key == root.key:
            return True
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def add(self, key: int) -> None:
        self.root = self.insert(self.root, key)

    def remove(self, key: int) -> None:
        self.root = self.delete(self.root, key)

    def contains(self, key: int) -> bool:
        return self.search(self.root, key)

    
# this is solving the fact that you only need 10,000 slots to store 1,000,000 keys
# saves a lot of memory in comparison to a full 1 mil array of bools. The issue though
# is collisions where there are more keys than slots
# this is seperate chaining technique
class MyHashSet:

    # size of 10,000 to keep keys spread out and less sollisions
    def __init__(self):
        self.size = 10000
        # Each bucket is a BST to store multiple values at that spot
        # since we are using a BST and not a LinkedList, we have faster lookups here
        # since BST lookup is O(log K) time. K is num of items in that bucket
        self.buckets = [BinarySearchTree()] * self.size

    # Hash function that uses the remainder is not bad here since it will
    # relatively spread it all out equally
        # using '_' to denote its a private method and to avoid collision
    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        idx = self._hash(key)
        if not self.contains(key):
            self.buckets[idx].add(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        self.buckets[idx].remove(key)
        

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return self.buckets[idx].contains(key)
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)