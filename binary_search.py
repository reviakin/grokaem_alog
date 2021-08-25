def binary_search(input_list, item):
    left = 0
    right = len(input_list) - 1

    while left != right: 
        mid = left + right // 2

        if input_list[mid] == item:
            return mid
        elif input_list[mid] > item: 
            right = mid
        else:
            left = mid


    return None


print(binary_search([1, 2, 3, 4, 5], 9)== None)
print(binary_search([1, 2, 3, 4, 5], 3) == 2)
print(binary_search([1, 2, 3, 4, 5], 1) == 0)
print(binary_search([1, 2, 3, 4, 5], 5) == 4)
