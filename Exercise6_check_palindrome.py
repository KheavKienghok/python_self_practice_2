def check_palindrome(word: str) -> str:
    # return True if word == word[::-1] else False
    
    """
    Check if a word is a palindrome.

    Args:
    - word: A string representing the word to be checked.

    Returns:
    - True if the word is a palindrome, False otherwise.
    """
    
    result = [char.lower() for char in word if char.isalnum()]

    words = "".join(result)
    
    return words == words[::-1]

def main() -> None:
    
    ask_user = input("Enter the word: ")
    
    if check_palindrome(ask_user):
        print(f"'{ask_user}' is a palindrome.")
    else:
        print(f"'{ask_user}' is not a palindrome.")

if __name__ == "__main__":
    main()
