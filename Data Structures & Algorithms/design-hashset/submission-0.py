class MyHashSet:
    # since we know we will only have 1000000 keys,
    # we can just make an array of False that marks whether or not this is in our set
    # constant times for all since we have a constant mem allocation (Still not the best)

    def __init__(self):
        self.nums = [False] * 1000001

    def add(self, key: int) -> None:
        self.nums[key] = True
        

    def remove(self, key: int) -> None:
        self.nums[key] = False

    def contains(self, key: int) -> bool:
        return self.nums[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)