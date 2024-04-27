def reverse_string(words: str) -> str:
    """
    Reverse a string.

    Args:
    - words (str): The string to be reversed.

    Returns:
    - str: The reversed string.

    This function takes a string as input and returns the reverse 
    of that string using Python's slicing notation. It reverses 
    the order of characters in the input string and returns the 
    result.
    """
    
    return words[::-1]


def main() -> None:
    
    ask_user = input("Enter the text you want to reverse: ")
    
    result = reverse_string(ask_user)
    
    print(result)
    
if __name__ == "__main__":
    main()