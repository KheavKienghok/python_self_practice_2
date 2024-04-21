def find_common_num(lst1: list, lst2: list) -> list:
    # return [number2 for number1 in lst1 for number2 in lst2 if number2 == number1]
    
    result = []
    for x in lst1:
        for y in lst2:
            if y == x:
                result.append(y)
    
    return result
    
   
    
print(find_common_num([3, 8, 12, 17, 22],[8, 12, 15, 20, 25]))