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

    def set_union(self, set2):
        union = PowerSet()
        union.storage = self.storage.copy()
        for val in set2.storage:
            if self.get(val) is False:
                union.put(val)
        return union

    def union(self, set2):
        if self.size() > set2.size():
            return self.set_union(set2)
        else:
            return set2.set_union(self)

    def difference(self, set2):
        difference = PowerSet()
        difference.storage = self.storage.copy()
        for val in set2.storage:
            index = difference.get_index(val)
            if index is not None:
                difference.storage.pop(index)
        return difference

    def issubset(self, set2):
        for val in set2.storage:
            if self.get(val) is False:
                return False
        return True

    def print_set(self):
        for val in self.storage:
            print(val, end=' ')
        print()


while True:
    print("\n1. Intersection of sets\n2. Union of sets\n3. Difference of sets\n"
          "4. Subset\n0. Exit")
    ch = input("Select operation: ")
    if ch == '0':
        break

    print("Enter elements of set A: ")
    set1 = PowerSet()
    set1.create()

    print("Enter elements of set B: ")
    set2 = PowerSet()
    set2.create()

    if ch == '1':
        print("Intersection of sets A and B:")
        set1.intersection(set2).print_set()

    elif ch == '2':
        print("Union of sets A and B:")
        set1.union(set2).print_set()

    elif ch == '3':
        print("Difference of sets A and B:")
        set1.difference(set2).print_set()

    elif ch == '4':
        print("B is subset of A:")
        print(set1.issubset(set2))

    else:
        break
