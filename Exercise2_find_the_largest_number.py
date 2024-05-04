def largest_number(lst: list) -> int:
    """
    Args:
    - lst (list): A list of numbers.

    Returns:
    - int: The largest number in the list.

    Example:
    ```
    >>> find_largest([1, 5, 3, 9, 7])
    9
    ```
    """
    result = lst[0]
    for number in lst:
        if number > result:
            result = number
            
    return result



def main() -> None:
    pass
    
if __name__ == "__main__":
    main()