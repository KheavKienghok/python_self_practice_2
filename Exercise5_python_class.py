class Stack_data():   
    
    def __init__(self):
        self.item = []
        
    def push_item(self, item):
        """
        Push an item onto the stack.

        Args:
        - self: The instance of the class.
        - item: The item to be pushed onto the stack.
        """
        
        self.item.append(item)
        
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
        
        if not self.is_empty():
            return self.item.pop()
        
        return None
    
    def is_empty(self) -> None:
        """
        Check if the stack is empty.

        Returns:
        - True if the stack is empty, False otherwise.
        """
        
        return len(self.item) == 0
    
    
def main():
    # Create an instance of the Stack_data class
    stack = Stack_data()
    
    while True:
        ask_user = input("Enter the command (add, pop, quit): ")
        
        if ask_user in ["quit", "q"]:
            break
        
        elif ask_user == "add":
            ask_add = input("Enter the item you want to add: ")
            stack.push_item(ask_add)
            print(f"{ask_add} has been added!")
        
        elif ask_user == "pop":
            popped_item = stack.pop_item()
            if popped_item is not None:
                print(f"{popped_item} has been removed!")
            else:
                print("Stack is empty!")
            
        else:
            print("Invalid input!!")
    
if __name__ == "__main__":
    main()