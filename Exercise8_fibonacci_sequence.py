def fibonacci_sequence(number: int) -> list:
    
    # total = []
    # for x in range(number):
    #     if x < 2:
    #         total.append(x)
    #     else:
    #         total.append(total[-1] + total[-2])
            
    # return total
    
    """
    Generate a Fibonacci sequence up to a given number of terms.

    Args:
        number (int): The number of terms in the Fibonacci sequence to generate.

    Returns:
        list: A list containing the Fibonacci sequence up to the specified number of terms.
    """
    
    if number < 0:
        return "Invalid input!"
    
    sequence = [0, 1]
    while len(sequence) < number:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
        
    return sequence[:number]

def main() -> None:
    
    ask_user = int(input("Enter the number: "))
    
    result = fibonacci_sequence(ask_user)
    
    if result:
        print(f"The fibonacci sequence are {result}")
    else:
        print("There are None sequence.")
    
    
if __name__ == "__main__":
    main()