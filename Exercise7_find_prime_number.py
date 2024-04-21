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
    print(find_prime_number([0, 100])) 

    
if __name__ == "__main__":
    main()