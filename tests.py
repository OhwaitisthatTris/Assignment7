# tests.py
# Tests of Stack and Queue
# Please exercise them enough to
# show they work under different combinations
# of operations and different orders of those operations
# Modified by: Tristan Crawford
import unittest
from stack import Stack
from que import Queue
 
 
class TestStack(unittest.TestCase):
    def test_stack_with_ints(self):
        stack = Stack()
        self.assertTrue(stack.is_empty)
        self.assertEqual(len(stack), 0)
        self.assertRaises(IndexError, stack.pop)
        self.assertRaises(IndexError, stack.peek)
 
        for i in range(1, 4):
            stack.push(i)
            self.assertEqual(stack.peek(), i)
            self.assertEqual(len(stack), i)
        self.assertFalse(stack.is_empty)
 
        self.assertEqual(stack.peek(), 3)
        self.assertEqual(len(stack), 3)
 
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(len(stack), 1)
 
        stack.push(10)
        self.assertEqual(stack.peek(), 10)
        self.assertEqual(stack.pop(), 10)
        self.assertEqual(stack.pop(), 1)
 
        self.assertTrue(stack.is_empty)
        self.assertEqual(len(stack), 0)
        self.assertRaises(IndexError, stack.pop)
        self.assertRaises(IndexError, stack.peek)
 
        stack.push(0)
        stack.push(-5)
        self.assertEqual(stack.pop(), -5)
        self.assertEqual(stack.pop(), 0)
 
        # a larger number of items
        for i in range(100):
            stack.push(i)
        for i in range(99, -1, -1):
            self.assertEqual(stack.pop(), i)
        self.assertTrue(stack.is_empty)
 
    def test_stack_with_strings(self):
        stack = Stack()
        self.assertTrue(stack.is_empty)
 
        for word in ["apple", "banana", "cherry"]:
            stack.push(word)
            self.assertEqual(stack.peek(), word)
        self.assertEqual(len(stack), 3)
 
        self.assertEqual(stack.pop(), "cherry")
        self.assertEqual(stack.peek(), "banana")
 
        stack.push("banana")
        stack.push("")
        self.assertEqual(len(stack), 4)
        self.assertEqual(stack.pop(), "")
        self.assertEqual(stack.pop(), "banana")
        self.assertEqual(stack.pop(), "banana")
        self.assertEqual(stack.pop(), "apple")
 
        self.assertTrue(stack.is_empty)
        self.assertRaises(IndexError, stack.pop)
        self.assertRaises(IndexError, stack.peek)
 
        for letter in "stack":
            stack.push(letter)
        reversed_word = ""
        while not stack.is_empty:
            reversed_word += stack.pop()
        self.assertEqual(reversed_word, "kcats")
 
 
class TestQueue(unittest.TestCase):
 
    def test_queue_with_ints(self):
        queue = Queue()
        self.assertTrue(queue.is_empty)
        self.assertEqual(len(queue), 0)
        self.assertRaises(IndexError, queue.pop)
        self.assertRaises(IndexError, queue.peek)
 
        for i in range(1, 4):
            queue.push(i)
            self.assertEqual(queue.peek(), 1)
            self.assertEqual(len(queue), i)
        self.assertFalse(queue.is_empty)
 
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(len(queue), 3)
 
        self.assertEqual(queue.pop(), 1)
        self.assertEqual(queue.pop(), 2)
        self.assertEqual(len(queue), 1)
 
        queue.push(10)
        self.assertEqual(queue.peek(), 3)
        self.assertEqual(queue.pop(), 3)
        self.assertEqual(queue.pop(), 10)
 
        self.assertTrue(queue.is_empty)
        self.assertEqual(len(queue), 0)
        self.assertRaises(IndexError, queue.pop)
        self.assertRaises(IndexError, queue.peek)
 
        queue.push(0)
        queue.push(-5)
        self.assertEqual(queue.pop(), 0)
        self.assertEqual(queue.pop(), -5)
 
        # a larger number of items
        for i in range(100):
            queue.push(i)
        for i in range(100):
            self.assertEqual(queue.pop(), i)
        self.assertTrue(queue.is_empty)
 
    def test_queue_with_strings(self):
        queue = Queue()
        self.assertTrue(queue.is_empty)
 
        # push words: the front is always the first word added
        for word in ["apple", "banana", "cherry"]:
            queue.push(word)
            self.assertEqual(queue.peek(), "apple")
        self.assertEqual(len(queue), 3)
 
        # first in, first out
        self.assertEqual(queue.pop(), "apple")
        self.assertEqual(queue.peek(), "banana")
 
        queue.push("banana")
        queue.push("")
        self.assertEqual(len(queue), 4)
        self.assertEqual(queue.pop(), "banana")
        self.assertEqual(queue.pop(), "cherry")
        self.assertEqual(queue.pop(), "banana")
        self.assertEqual(queue.pop(), "")
 
        self.assertTrue(queue.is_empty)
        self.assertRaises(IndexError, queue.pop)
        self.assertRaises(IndexError, queue.peek)
 
        for name in ["Ann", "Bob", "Cy"]:
            queue.push(name)
        served = []
        while not queue.is_empty:
            served.append(queue.pop())
        self.assertEqual(served, ["Ann", "Bob", "Cy"])
 
 
if __name__ == '__main__':
    unittest.main()
