class Stack_data():   
    
    """
    A simple stack implementation using a list.

    This class represents a stack data structure where items are 
    added and removed according to the Last-In-First-Out (LIFO) 
    principle.

    Example usage:
    ```
    stack = Stack_data()
    stack.push_item(1)
    stack.push_item(2)
    stack.push_item(3)
    print(stack.pop_item())  # Output: 3
    print(stack.pop_item())  # Output: 2
    print(stack.pop_item())  # Output: 1
    print(stack.pop_item())  # Output: None
    ```

    """


    def __init__(self):
        pass
        
    def push_item(self, item):
        """
        Push an item onto the stack.

        Args:
        - self: The instance of the class.
        - item: The item to be pushed onto the stack.
        """
        pass
     
        
    def pop_item(self) -> None:
        """
        Pop an item from the stack.

        If the stack is not empty, it removes and returns the top item from the stack.
        If the stack is empty, it returns None.

        Args:
        - self: The instance of the class.

        Returns:
        - The popped item from the stack, or None if the stack is empty.
        """
        pass
    
    def is_empty(self) -> None:
        """
        Check if the stack is empty.

        Returns:
        - True if the stack is empty, False otherwise.
        """
        pass
    
    
def main():
    # Create an instance of the Stack_data class
    stack = Stack_data()
    pass

if __name__ == "__main__":
    main()