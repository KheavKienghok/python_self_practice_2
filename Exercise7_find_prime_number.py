def find_prime_number(lst: list) -> list:
    
    total = []
    for x in lst:
        key = True
        if x < 2:
            continue
        
        for y in range(2, x):
            if x % y == 0:
                key = False
                break
                
        if key:
            total.append(x)
            
    return total


def main() -> None:
    
    ask_user = input("Enter the range of number (comma to seperate): ").split(",")
    
    lst_num = [int(num.strip()) for num in ask_user]

    result = find_prime_number(lst_num)
    
    if result:
        print(f"The prime are {result}")
    else:
        print("There are None Prime Number.")
    
if __name__ == "__main__":
    main()