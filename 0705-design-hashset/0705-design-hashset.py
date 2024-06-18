class MyHashSet:

    def __init__(self):
        self.hashSet = {}

    def add(self, key: int) -> None:
        if key in self.hashSet:
            return
        self.hashSet[key]=1

    def remove(self, key: int) -> None:
        if key in self.hashSet:
            self.hashSet.pop(key)
        else: return

    def contains(self, key: int) -> bool:
        if key in self.hashSet:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)