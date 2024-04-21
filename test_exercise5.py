import unittest
from Exercise5_python_class import Stack_data


class TestStackData(unittest.TestCase):
    
    # Define a nested class Stack that inherits from Stack_data
    class Stack(Stack_data):
        def __init__(self) -> None:
            super().__init__()

    # Set up the stack instance before each test method
    def setUp(self):
        self.stack = self.Stack()

    # Test pushing items onto the stack
    def test_push_item(self):
        # Push items onto the stack
        self.stack.push_item(1)
        self.stack.push_item(2)
        self.stack.push_item(3)
        
        # Check if items were added correctly
        self.assertEqual(self.stack.item, [1, 2, 3])

    # Test popping an item from the stack
    def test_pop_item(self):
        # Push items onto the stack
        self.stack.push_item(1)
        self.stack.push_item(2)
        
        # Pop an item from the stack
        popped_item = self.stack.pop_item()
        
        # Check if the popped item is correct
        self.assertEqual(popped_item, 2)
        
        # Check if the stack is updated correctly
        self.assertEqual(self.stack.item, [1])

    # Test checking if the stack is empty
    def test_is_empty(self):
        # Check if the stack is initially empty
        self.assertTrue(self.stack.is_empty())
        
        # Push an item onto the stack
        self.stack.push_item(1)
        
        # Check if the stack is not empty after pushing an item
        self.assertFalse(self.stack.is_empty())
        
        # Pop the item from the stack
        self.stack.pop_item()
        
        # Check if the stack is empty after popping the item
        self.assertTrue(self.stack.is_empty())

    # Test pushing a string item onto the stack
    def test_push_item_string(self):
        # Push a string item onto the stack
        self.stack.push_item("hat")
        
        # Check if the item "hat" was added correctly
        self.assertEqual(self.stack.item, ["hat"])

    # Test popping an item from an empty stack
    def test_pop_item_empty_stack(self):
        # Pop an item from an empty stack
        popped_item = self.stack.pop_item()
        
        # Check if the popped item is None
        self.assertIsNone(popped_item)
        
        # Check if the stack remains empty
        self.assertTrue(self.stack.is_empty())
