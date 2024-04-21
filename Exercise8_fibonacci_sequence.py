def fibonacci_sequence(number: int) -> list:
    
    # total = []
    # for x in range(number):
    #     if x < 2:
    #         total.append(x)
    #     else:
    #         total.append(total[-1] + total[-2])
            
    # return total
    
    if number < 0:
        return "Invalid input!"
    
    sequence = [0, 1]
    while len(sequence) < number:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
        
    return sequence[:number]

def main() -> None:
    
    ...
    
if __name__ == "__main__":
    main()