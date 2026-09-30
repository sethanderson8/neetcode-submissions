class MyHashSet:

    def __init__(self):
        # key is in the range [0, 1000000]
        # 31251 * 32 = 1000032
        # Array of 31,251 integers. Each integer acts as a bucket holding 32 boolean switches (bits).
        # We reconstruct a key's value using its exact coordinates in memory.
        # Formula: (Array Index * 32) + Bit Position = Key
        # Example: If the 3rd bit inside self.set[1] is flipped ON, it represents key 35 ((1 * 32) + 3 = 35).
        self.set = [0] * 31251

    # Bitwise OR (|) stacks the mask onto the current bucket, forcing the target bit to 1.
    # Since it compares column by column, all other 31 switches are left exactly as they are.
    # If the key is already in the set, the switch is already 1, and since 1 | 1 evaluates to 1,
    # it natively handles duplicate additions without needing to check if the key exists first.
    def add(self, key: int) -> None:
        self.set[key // 32] |= self.getMask(key)

    # Bitwise XOR (^) acts exactly like a != operator.
    # If the box bit != mask bit, it outputs 1.
    # If the box bit == mask bit, it outputs 0.
    # We must check contains() first so we only compare 
    # 1 == 1 (which safely flips the target to 0).
    # If we didn't check, comparing 0 != 1 would 
    # accidentally add the key by flipping it to 1.
    def remove(self, key: int) -> None:
        if self.contains(key):
            self.set[key // 32] ^= self.getMask(key)
        
    # Bitwise AND (&) isolates the target bit by applying a mask of 0s to all other positions,
    # forcing them to evaluate to 0. If the target bit is 1, the entire binary sequence evaluates
    # to a non-zero integer, meaning the key exists (True). If the target bit is 0, the sequence
    # evaluates to mathematically 0, meaning the key does not exist (False).
    def contains(self, key: int) -> bool:
        return self.set[key // 32] & self.getMask(key) != 0

    # Create a 32-bit stencil by taking a single '1' at the 0th position 
    # and sliding it to the left by the key's exact bit slot (0-31).
    # We then stack this stencil on top of the target bucket (self.set[key // 32]) using bitwise operators.
    # Example for key 35: 35 % 32 = 3. Shifting '1' left by 3 (1 << 3) generates the mask ...00001000.
    def getMask(self, key: int) -> int:
        return 1 << (key % 32)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)