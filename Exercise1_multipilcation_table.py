def multiplication(number: int) -> str:
    """
    Generate a multiplication table for the given number.

    Args:
    - number (int): The number for which to generate the multiplication table.

    Returns:
    - str: A string representing the multiplication table for the given number.

    The function generates a multiplication table for the specified number,
    ranging from 1 to 10. Each line of the table contains the multiplication
    expression in the format "number * x = result", where 'number' is the
    specified number, 'x' ranges from 1 to 10, and 'result' is the product
    of 'number' and 'x'. The table is returned as a single string, with each
    line separated by a newline character.
    """
    
    table = ""
    
    for x in range(1, 11):
        table += f"{number:<2} * {x:<2} = {number * x}\n"
        
    return table


        
def main() -> None:
    """
    Prompt the user to enter a number, generate its multiplication table,
    and print the result.

    This function prompts the user to enter a number via the standard input (stdin),
    then generates the multiplication table for the entered number using the
    multiplication function. It prints the generated multiplication table to
    the standard output (stdout).

    Returns:
    - None: This function does not return any value.
    """
    
    ask_user = int(input("Enter the number: "))
    
    result = multiplication(ask_user)
    
    print(result)
    
    
if __name__ == "__main__":
    main()