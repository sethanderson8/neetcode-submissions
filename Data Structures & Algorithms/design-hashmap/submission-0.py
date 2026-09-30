class MyHashMap:

    def __init__(self):
        # -1 since that is returned for when not found and values cannot be less than 0
        self.vals = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.vals[key] = value

    def get(self, key: int) -> int:
        return self.vals[key]

    def remove(self, key: int) -> None:
        self.vals[key] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)