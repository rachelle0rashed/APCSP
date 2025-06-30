def remove_all_from_string(main_string, string_remove):
    if len(string_remove) == 0:
        return main_string
    result_string = main_string
    
    while True:
        found_index = result_string.find(string_remove)
        
        if found_index != -1:
            result_string = result_string[:found_index] + result_string[found_index + len(string_remove): ]
        else:
            break
    return result_string
user_input_string = input("Enter the main string: ")
user_string_remove = input("Enter the string or letter to remove: ")

final_result = remove_all_from_string(user_input_string, user_string_remove)
print("Result", final_result)