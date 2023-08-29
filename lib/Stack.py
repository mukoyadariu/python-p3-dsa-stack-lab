class Stack:

    def __init__(self, items=None, limit=100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            print("Stack is full. Cannot push item.")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop item.")
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("Stack is empty. Cannot peek item.")
            return None

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        if target in self.items:
            return self.items.index(target)
        return -1


class TestStack:

    def test_search(self):
        '''Test Stack search() method'''
        stk = Stack([5, 6, 7, 8, 9, 10])

        assert stk.search(5) == stk.size() - 1  # 5 is at the bottom, so size - 1
        assert stk.search(6) == stk.size() - 2
        assert stk.search(7) == stk.size() - 3
        assert stk.search(8) == stk.size() - 4
        assert stk.search(9) == stk.size() - 5
        assert stk.search(10) == stk.size() - 6  # 10 is at the top, so size - 6
        assert stk.search(15) == -1  # Not found

    def run_tests(self):
        self.test_search()
        # Call other test methods here


if __name__ == "__main__":
    tester = TestStack()
    tester.run_tests()
    print("All tests passed!")
