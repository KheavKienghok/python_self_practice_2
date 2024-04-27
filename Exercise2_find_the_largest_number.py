def largest_number(lst: list) -> int:
    # return max([number for number in lst])
    
    """
    Find the largest number in a list.

    Args:
    - lst (list): A list of numbers.

    Returns:
    - int: The largest number in the list.

    This function iterates over the elements of the input list and 
    returns the largest number found. It initializes a variable 
    `largest_number` with the first element of the list and compares 
    it with each subsequent element. If a larger element is found, 
    it replaces the current largest number. The final largest number 
    is returned.
    """
    
    largest_number = lst[0]

    for number in lst:
        if number > largest_number:
            largest_number = number
            
    return largest_number



def main() -> None:
    
    ask_user = input("Enter the number (seperate by comma): ").split(",")
    
    number = [eval(number.strip()) for number in ask_user]
    
    result = largest_number(number)
    
    print(result)
    
if __name__ == "__main__":
    main()