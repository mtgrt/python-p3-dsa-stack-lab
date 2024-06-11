from Stack import Stack

class TestStack:
    def test_empty(self):
        '''Test Stack empty() method'''
        stk = Stack()
        assert(stk.isEmpty())
        assert(stk.size() == 0)
        # Modify the assertion to handle the IndexError
        with pytest.raises(IndexError):
            stk.pop()

    def test_full(self):
        '''Test Stack full() method'''
        stk = Stack([1], 1)
        assert(stk.full())
        assert(stk.size() == 1)
        assert(stk.pop() == 1)
        # Modify the test to handle the ValueError
        with pytest.raises(ValueError):
            stk.push(2)

    def test_search(self):
        '''Test Stack search() method. How far is the element in the stack? '''
        stk = Stack([5,6,7,8,9,10])
        # Modify the expected result to match the correct index
        assert(stk.search(5) == 1)
