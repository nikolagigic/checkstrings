def check_strings(string1, string2):
    sorted_string2 = sorted(string2)
    
    while len(sorted_string2) > 0:
        first_char = sorted_string2[0]
        
        if (string1.count(first_char) != sorted_string2.count(first_char)):
            return False
        
        sorted_string2 = list(filter(lambda x: x != first_char, sorted_string2))
    
    return True