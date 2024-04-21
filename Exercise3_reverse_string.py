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
    """
    Prompt the user to enter a text, reverse it, and print the result.

    This function prompts the user to enter a text via the standard input (stdin). 
    It then calls the `reverse_string` function to reverse the input text and 
    prints the reversed text to the standard output (stdout).

    Returns:
    - None: This function does not return any value.
    """
    
    ask_user = input("Enter the text you want to reverse: ")
    
    result = reverse_string(ask_user)
    
    print(result)
    
if __name__ == "__main__":
    main()