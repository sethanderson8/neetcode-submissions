
# BST approach
class TreeNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root: TreeNode, key: int, value: int):
        # If no root yet, return new node
        if not root:
            return TreeNode(key, value)
        elif key < root.key:
            # left
            root.left = self.insert(root.left, key, value)
        elif key == root.key:
            # If the key already exists, update its value and stop.
            root.value = value
        elif key > root.key:
            root.right = self.insert(root.right, key, value)
        else: 
            # right
            root.right = self.insert(root.right, key, value)

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
            root.value = temp.value

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

    def get(self, root, key) -> TreeNode:
        if not root:
            return None
        elif key == root.key:
            return root
        elif key < root.key:
            return self.get(root.left, key)
        else:
            return self.get(root.right, key)

    def find_and_get(self, key: int) -> TreeNode:
        return self.get(self.root, key)

    def add(self, key: int, value: int) -> None:
        self.root = self.insert(self.root, key, value)

    def remove(self, key: int) -> None:
        self.root = self.delete(self.root, key)

    def contains(self, key: int) -> bool:
        return self.search(self.root, key)

class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.buckets = [BinarySearchTree()] * self.size

    def _hash(self, key: int):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        self.buckets[idx].add(key, value)

    def get(self, key: int) -> int:
        idx = self._hash(key)
        if not self.buckets[idx].contains(key):
            return -1
        return self.buckets[idx].find_and_get(key).value

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        self.buckets[idx].remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)