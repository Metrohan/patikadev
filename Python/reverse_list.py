def reverse_nested_list(nested_list):
    if not isinstance(nested_list, list):
        return nested_list
    
    reversed_list = nested_list[::-1]
    for i in range(len(reversed_list)):
        if isinstance(reversed_list[i], list):
            reversed_list[i] = reverse_nested_list(reversed_list[i])

    return reversed_list

input_list = [[1, 2], [3, 4], [5, 6, 7]]
output_list = reverse_nested_list(input_list)
print(output_list)