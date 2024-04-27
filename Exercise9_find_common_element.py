def find_common_num(lst1: list, lst2: list) -> list:
    # return [number2 for number1 in lst1 for number2 in lst2 if number2 == number1]
    
    """
    Find common numbers between two lists.

    Args:
        lst1 (list): The first list of numbers.
        lst2 (list): The second list of numbers.

    Returns:
        list: A list containing the numbers that are common between lst1 and lst2.
    """
    
    result = []
    for x in lst1:
        for y in lst2:
            if y == x:
                result.append(y)
    
    return list(set(result))
    


def main() -> None:
    ask_num1 = input("Enter the first numbers (seperate by comma): ").split(",")
    ask_num2 = input("Enter the second numbers (seperate by comma): ").split(",")
    
    lst_num1 = [int(num.strip()) for num in ask_num1]
    lst_num2 = [int(num.strip()) for num in ask_num2]
    
    result = find_common_num(lst_num1, lst_num2)
    
    if result:
        print(f"The common number are {result}")
    else:
        print("There is no common number.")
    
    
if __name__ == "__main__":
    main()