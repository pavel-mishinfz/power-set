class PowerSet:
    def __init__(self):
        self.storage = []

    def create(self):
        for val in input().split():
            self.put(int(val))

    def size(self):
        return self.storage.__len__()

    def put(self, value):
        if self.get(value):
            return
        if self.size() == 0 or self.storage[-1] < value:
            self.storage.append(value)
            return
        if self.storage[0] > value:
            self.storage.insert(0, value)
            return

        left, right = 0, self.size()
        while left < right:
            mid = (left + right) // 2
            if self.storage[mid] < value:
                left = mid + 1
            else:
                right = mid
        self.storage.insert(left, value)

    def get(self, value):
        return self.get_index(value) is not None

    def get_index(self, value):
        left, right = 0, self.size()
        while left < right:
            mid = (left + right) // 2
            if self.storage[mid] < value:
                left = mid + 1
            elif self.storage[mid] > value:
                right = mid
            else:
                return mid
        return None

    def remove(self, value):
        index = self.get_index(value)
        if index is not None:
            self.storage.pop(index)
            return True
        return False

    def set_intersection(self, set2):
        intersection = PowerSet()
        for val in self.storage:
            if set2.get(val):
                intersection.put(val)
        return intersection

    def intersection(self, set2):
        if self.size() > set2.size():
            return self.set_intersection(set2)
        else:
            return set2.set_intersection(self)
