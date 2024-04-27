def sum_2d_list(lst: list) -> int:
    # return sum([number for numbers in lst for number in numbers])
    
    """
    Sums up all the numbers in a 2D list.

    Args:
    - lst (list): A 2D list of numbers.

    Returns:
    - int: The sum of all numbers in the 2D list.
    """
    
    total = 0
    for numbers in lst:
        for number in numbers:
            total += number
            
    return total
    
    
def main() -> None:

    ask_user = input("Enter numbers for the 2D list (separated by comma): ").split(",")
    
    user_input = []
    numbers = [int(num.strip()) for num in ask_user]
    user_input.append(numbers)
    
    result = sum_2d_list(user_input)
    
    print("The sum of the 2D list is:", result)

if __name__ == "__main__":
    main()